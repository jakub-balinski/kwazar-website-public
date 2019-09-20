import os
import json

with open('../kwazar-website/config.json') as config_file:
    config = json.load(config_file)


class Config:
    SECRET_KEY = config.get('SECRET_KEY')
    SEND_FILE_MAX_AGE_DEFAULT = 604800
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = config.get('MAIL_SERVER')
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_USERNAME = config.get('EMAIL_USER')
    MAIL_PASSWORD = config.get('EMAIL_PASS')
    RECAPTCHA_USE_SSL = True
    RECAPTCHA_PUBLIC_KEY = config.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = config.get('RECAPTCHA_PRIVATE_KEY')
    RECAPTCHA_OPTIONS = {'theme': 'white'}
    RECAPTCHA_PARAMETERS = {'hl': 'pl'}
