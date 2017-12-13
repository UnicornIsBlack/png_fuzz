import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECURE_KEY = os.environ.get('SECURE_KEY') or 'Merry Christmas'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = os.environ.get('DEV_DATABASE_URL') or \
        'mysql://root:chai@localhost/fuzz_png'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URL = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql://root:chai@localhost/fuzz_png'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URL = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql://root:chai@localhost/fuzz_png'

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}
