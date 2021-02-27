import os
from skyway_connect.app import create_app
from skyway_connect.settings import DevConfig, ProdConfig

CONFIG = ProdConfig if os.environ.get('FLASK_DEBUG') == '0' else DevConfig

app = create_app(CONFIG)
