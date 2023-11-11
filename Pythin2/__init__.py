
from flask import Flask
from dotenv import load_dotenv
from .main import main_bp as main_blueprint
import os

#Load .env file
dotenv_path = dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))
load_dotenv(dotenv_path)

# Create the application
def create_app():
    app = Flask(__name__)
    
    # App configurations
    app.config['SECRET_KEY'] = os.getenv('PYTHIN2_SECRET_KEY')
    app.debug = True

    # Register blueprints
    app.register_blueprint(main_blueprint)

    # Print routes
    print("Routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule}")

    # Debugging
    print("App created succesfully")

    return app
