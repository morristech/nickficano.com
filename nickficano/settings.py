class Default(object):
    DEBUG = False
    TESTING = False


class Prod(Default):
    DEBUG = False


class Dev(Default):
    DEBUG = True
    SERVER_NAME = '0.0.0.0:5000'
