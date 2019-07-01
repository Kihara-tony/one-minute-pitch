import os

class Config:
    '''
    general configuration
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgres://tony:tonyqtjds2@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static'
    # email configurations
    MAIL_SERVER = 'smtp.gmailemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX ='pitch'
    SENDER_EMAIL ='tonykiharatonkin6@gmail.com'
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    production configuration child class
    '''


class DevConfig(Config):
    '''
    development configuration child class
    '''
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tony:tonyqtjds2@localhost/pitch_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tony:tonyqtjds2@localhost/pitch'
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
