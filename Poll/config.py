import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    TWILIO_ACCOUNT_SID = 'AC1378ad49596398eea7656c9143c59bf3'
    TWILIO_AUTH_TOKEN = 'f86c33d52f9cd710203692d8d2bcb521'
    TWILIO_NUMBER = '+919934785875'


Config_test = False