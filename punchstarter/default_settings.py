import os

DEBUG=True
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///%s/app.db" % (BASE_DIR)
SQLALCHEMY_TRACK_MODIFICATIONS = True