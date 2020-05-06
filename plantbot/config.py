import  os


DEBUG = True
MONGO_DBNAME = 'plants'
MONGO_URI = 'mongodb+srv://admin:admin1234@cluster0-rsh71.mongodb.net/test?retryWrites=true&w=majority' 
ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG"]
MAX_IMAGE_FILESIZE = 100 * 1024 * 1024
IMAGE_UPLOADS = 'tmp'
API_KEY ='uPNlLvtXfhpnqQqEHuQx8jwwxvWUPW7ix0U9aIFGlcsiOdKYrd'
SECRET_KEY = b'dor9dor'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "plant-bot.json"
os.environ["FLASK_APP"] = 'plantbot'
os.environ["FLASK_ENV"] = 'development'
