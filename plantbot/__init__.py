from flask import Flask, request, jsonify, render_template,session, redirect, url_for, make_response
from werkzeug.utils import secure_filename
import json, requests, os, base64, random
import numpy as np


    
# def allowed_image_filesize(filesize):

#     if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
#         return True
#     else:
#         return False

# def allowed_image(filename):
#     """
#     validate image extension
#     """
#     if not "." in filename:
#         return False

#     ext = filename.rsplit(".", 1)[1]

#     if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
#         return True
#     else:
#         return False

# def send_image(image):
#     json_data = {
#         "images": image,
#         "modifiers": ["similar_images"],
#         "plant_details": ["common_names", "url", "wiki_description", "taxonomy"]
#     }

#     response = requests.post(
#         "https://api.plant.id/v2/identify",
#         json=json_data,
#         headers={
#             "Content-Type": "application/json",
#             "Api-Key": app.config["API_KEY"]
#         }).json()
#     if response["suggestions"] is not None:
#         return response
#     else:
#         return False



app = Flask(__name__,template_folder="templates",static_folder="static", instance_relative_config=True)


app.config.from_object('config')
app.config.from_pyfile('config.py')

import plantbot.views

# @app.route('/', methods=['GET', 'POST'])
# def upload_image(**kwargs):
    
#     error = ""
#     if session.get('error'):
#         error = session['error']
        
#     if request.method == "POST":
#         if request.files:

#             if "filesize" in request.cookies:

#                 if not allowed_image_filesize(request.cookies["filesize"]):
#                     error= "Filesize exceeded maximum limit"
#                     print("Filesize exceeded maximum limit")
#                     session['error'] = error
#                     return redirect(request.url)

#                 image = request.files["image"]

#                 if image.filename == "":
#                     error= "No fileName"
#                     print("No filename")
#                     session['error'] = error
#                     return redirect(request.url)

#                 if allowed_image(image.filename):

#                     filename = secure_filename(image.filename)
#                     image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

#                     with open(app.config["IMAGE_UPLOADS"]+"/"+filename, "rb") as file:
#                         image = [base64.b64encode(file.read()).decode("ascii")]

                        
#                         # response = send_image(image)
#                         # # print('response: ========== \n', response)
#                         # plant =response['suggestions'][0]
#                         # print('plant =========\n',plant)
#                         # name = plant["plant_name"]
#                         # plant_name = name.split(' ')
                        
#                         # for i, plant in enumerate(data['plants']) :
#                         #     print(plant)
#                         #     if session.get('plant_index') is not None:
#                         #         break
#                         #     for name in plant_name:
#                         #         print('name =========== ', name)
                                
#                         #         if name.lower() in  plant['plant name'].lower():
#                         #             print('in if ########################', plant['plant name'])
                                    
#                         #             session['plant_index'] = i
#                         #             break
                            
#                         session['plant_index'] = 2
                        
#                     if session.get('plant_index') == None:   
#                         return render_template("upload_image.html", error="not found plant")
#                     # session['error'] = 'can`t open file'    
#                     return redirect(url_for('loading_bot'))


#                 else:
#                     session['error'] = 'That file extension is not allowed'
#                     print("That file extension is not allowed")
#                     return redirect("/")
#         else:
#             session['error'] = 'file not found'
#     session['plant_index'] = None
#     return render_template("upload_image.html", error=error)

# @app.route('/loading_bot',methods = ['POST', 'GET'])
# def loading_bot():
    
#     session['session_id'] = '12345678'
#     return render_template('chat.html', plant=data['plants'][session.get('plant_index')]['plant name'])

# @app.route('/send_message', methods=['POST'])
# def send_message():
#     plant_index = session.get('plant_index')
#     session_id= session.get('session_id')
#     message = request.form['message']
#     fulfillment_text = detect_intent_texts(plant=plant_index, session_id=session_id, text=message)
#     response_text = { "message":  fulfillment_text }
#     return jsonify(response_text)
    
    


# # create a route for webhook
# @app.route('/webhook', methods=['GET', 'POST'])
# def webhook():
#     # return response
#     return make_response(jsonify(get_response()))


# if __name__ == "__main__":
#     app.run(threaded=True, debug=True)

