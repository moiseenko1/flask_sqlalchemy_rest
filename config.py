import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration(object):
    # DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    # TEMPLATES_AUTO_RELOAD = True
