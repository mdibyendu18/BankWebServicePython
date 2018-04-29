from .base import *

DEBUG = False
ALLOWED_HOSTS = [
	'bankservicepython.herokuapp.com'
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd71blt8cbq54i7',
        'USER': 'mofmmarumxhoao',
        'PASSWORD': '435eb5192ebcb3682a306004ad1c85f84473bdceb504488417a49276fa2fcde9',
        'HOST': 'ec2-54-83-1-94.compute-1.amazonaws.com',
        'PORT': '5432',
        'URI': 'postgres://mofmmarumxhoao:435eb5192ebcb3682a306004ad1c85f84473bdceb504488417a49276fa2fcde9@ec2-54-83-1-94.compute-1.amazonaws.com:5432/d71blt8cbq54i7'
    }
}