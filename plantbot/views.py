from flask import request, jsonify, render_template, session, redirect, url_for, make_response
from plantbot import app
from plantbot.plant_identify import allowed_image, allowed_image_filesize, send_image
from werkzeug.utils import secure_filename
from plantbot.dialogflow import detect_intent_texts, get_response
import os, base64, json
from .model import get_plant, get_plants

# with open('data.txt') as json_file:
#     data = json.load(json_file)

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

                    filename = secure_filename(image.filename)
                    # image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

                    # with open(app.config["IMAGE_UPLOADS"]+"/"+filename, "rb") as file:
                    # with open(image, "rb") as file:
                    image = [base64.b64encode(image.read()).decode("ascii")]

                        
                    response = send_image(image)
                    # plant_identify = {'id': 14143522, 'plant_name': 'Rosmarinus officinalis', 'plant_details': {'scientific_name': 'Rosmarinus officinalis', 'structured_name': {'genus': 'rosmarinus', 'species': 'officinalis'}, 'common_names': ['Rosemary', 'Salvia rosmarinus', 'Anthos'], 'url': 'http://en.wikipedia.org/wiki/Rosmarinus_officinalis', 'wiki_description': {'value': 'Salvia rosmarinus, commonly known as rosemary, is a woody, perennial herb with fragrant, evergreen, needle-like leaves and white, pink, purple, or blue flowers, native to the Mediterranean region. Until 2017, it was known by the scientific name Rosmarinus officinalis, now a synonym.\nIt is a member of the mint family Lamiaceae, which includes many other herbs. The name "rosemary" derives from Latin ros marinus ("dew of the sea"). The plant is also sometimes called anthos, from the ancient Greek word ἄνθος, meaning "flower". Rosemary has a fibrous root system.', 'citation': 'http://en.wikipedia.org/wiki/Rosmarinus_officinalis', 'license_name': 'CC BY-SA 3.0', 'license_url': 'https://creativecommons.org/licenses/by-sa/3.0/'}, 'taxonomy': {'kingdom': 'Plantae', 'phylum': 'Tracheophyta', 'class': 'Magnoliopsida', 'order': 'Lamiales', 'family': 'Lamiaceae', 'genus': 'Rosmarinus'}}, 'probability': 0.8978623588873735, 'confirmed': False, 'similar_images': [{'id': '84a3079304551a37b1a6b762f0bb09ff', 'similarity': 0.8775884678848236, 'url': 'https://storage.googleapis.com/plant_id_images/similar_images/2019_05/images/Rosmarinus officinalis/84a3079304551a37b1a6b762f0bb09ff.jpg', 'url_small': 'https://storage.googleapis.com/plant_id_images/similar_images/2019_05/images/Rosmarinus officinalis/84a3079304551a37b1a6b762f0bb09ff.small.jpg'}, {'id': '5ab0817f2cf6a205195d1ce1740bfb63', 'similarity': 0.8766923338234861, 'url': 'https://storage.googleapis.com/plant_id_images/similar_images/2019_05/images/Rosmarinus officinalis/5ab0817f2cf6a205195d1ce1740bfb63.jpg', 'url_small': 'https://storage.googleapis.com/plant_id_images/similar_images/2019_05/images/Rosmarinus officinalis/5ab0817f2cf6a205195d1ce1740bfb63.small.jpg'}]}
                    plant_identify =response['suggestions'][0]
                    print(plant_identify)
                    
                    for i, plant in enumerate(get_plants()) :
                        print(i)
                        if session.get('plant_index') is not None:
                            break
                        print(plant)
                        names = plant_identify['plant_name'].split(' ')
                        for name in names:
                            print(name)
                            if name.lower() in  plant['plant name'].lower():
                                print('in if ==========')
                                session['plant_index'] = (i+1)
                                break
                            
                    # session['plant_index'] = 2
                    # os.remove(os.path.join(app.config["IMAGE_UPLOADS"], filename))    
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

