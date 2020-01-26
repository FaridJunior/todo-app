import os
dbpath = os.path.join(os.path.abspath(os.curdir),"todo/todo.db")
SECRET_KEY = "secert"
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(dbpath)
SQLALCHEMY_TRACK_MODIFICATIONS = True
POSTS_PER_PAGE = 10
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
ADMINS = ['mhmdmedo820@gmail.com']
POSTS_PER_PAGE = 25

