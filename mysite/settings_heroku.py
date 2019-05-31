import django_heroku

from .settings_prod import *


django_heroku.settings(locals())

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
    'utils.api.BrowsableAPIRendererWithoutForms',
)
