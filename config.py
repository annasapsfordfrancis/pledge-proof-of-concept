import os

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    DEBUG = False
    pass

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True

class TestingConfig(Config):
    TESTING = True
