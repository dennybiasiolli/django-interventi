from .settings_base import *


DEBUG = False

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
    'utils.api.BrowsableAPIRendererWithoutForms',
)
