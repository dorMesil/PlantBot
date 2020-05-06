from plantbot import app
import requests


def allowed_image_filesize(filesize):
    
    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False

def allowed_image(filename):
    """
    validate image extension
    """
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

def send_image(image):
    json_data = {
        "images": image,
        "modifiers": ["similar_images"],
        "plant_details": ["common_names", "url", "wiki_description", "taxonomy"]
    }

    response = requests.post(
        "https://api.plant.id/v2/identify",
        json=json_data,
        headers={
            "Content-Type": "application/json",
            "Api-Key": app.config["API_KEY"]
        }).json()
    if response["suggestions"] is not None:
        return response
    else:
        return False