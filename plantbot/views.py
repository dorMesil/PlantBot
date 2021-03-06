from flask import request, jsonify, render_template, session, redirect, url_for, make_response
from plantbot import app
from plantbot.plant_identify import allowed_image, allowed_image_filesize, send_image
from plantbot.dialogflow import detect_intent_texts, get_response
import os, base64, json, random
from .model import get_plant, get_plants

@app.route('/', methods=['GET', 'POST'])
def upload_image(**kwargs):
    
    error = ""
    if session.get('error'):
        error = session['error']
        
    if request.method == "POST":
        if request.files:

            if "filesize" in request.cookies:

                if not allowed_image_filesize(request.cookies["filesize"]):
                    error= "Filesize exceeded maximum limit"
                    print("Filesize exceeded maximum limit")
                    session['error'] = error
                    return redirect(request.url)

                image = request.files["image"]

                if image.filename == "":
                    error= "No fileName"
                    print("No filename")
                    session['error'] = error
                    return redirect(request.url)

                if allowed_image(image.filename):

                    image = [base64.b64encode(image.read()).decode("ascii")]

                        
                    # response = send_image(image)
                    # print('print api response\n',response)
                    # plant_identify =response['suggestions'][0]
                    
                    # for i, plant in enumerate(get_plants()) :
                    #     if session.get('plant_index') is not None:
                    #         break
                    #     names = plant_identify['plant_name'].split(' ')
                    #     for name in names:
                    #         if name.lower() in  plant['plant name'].lower():
                    #             session['plant_index'] = (i+1)
                    #             break
                            
                    session['plant_index'] = random.randint(1, 6)
                      
                    if session.get('plant_index') == None:   
                        return render_template("upload_image.html", error="not found plant")
                        
                    return redirect(url_for('loading_bot'))


                else:
                    session['error'] = 'That file extension is not allowed'
                    print("That file extension is not allowed")
                    return redirect("/")
        else:
            session['error'] = 'file not found'
    session['plant_index'] = None
    return render_template("upload_image.html", error=error)

@app.route('/loading_bot',methods = ['POST', 'GET'])
def loading_bot():
    
    session['session_id'] = '12345678'
    print('seesion index = ', session.get('plant_index'))
    plant = get_plant(session.get('plant_index'))
    print('print plant====\n', plant)
    return render_template('chat.html', plant=plant['plant name'])

@app.route('/send_message', methods=['POST'])
def send_message():
    plant_index = session.get('plant_index')
    session_id= session.get('session_id')
    message = request.form['message']
    fulfillment_text = detect_intent_texts(plant=plant_index, session_id=session_id, text=message)
    response_text = { "message":  fulfillment_text }
    return jsonify(response_text)
    
    

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(get_response()))

