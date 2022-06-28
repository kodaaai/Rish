from .base import *
import environ

env = environ.Env()

HostName = env('P_HOST_NAME')
Engine = env('P_ENGINE')
Name = env('P_NAME')
User = env('P_USER')
PassWord = env('P_PASS')
Port = env('P_PORT')
Secret_Key = env("SECRET_KEY")

ALLOWED_HOSTS = ["rish-ryukyu.com"]

SECRET_KEY = Secret_Key

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': Engine,
        'NAME': Name,
        'USER': User,
        'PASSWORD': PassWord,
        'HOST': HostName,
        'PORT': Port,
    }
}

# アカウントメール認証
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_REQUIRED = True
