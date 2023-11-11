
from flask import Flask
from dotenv import load_dotenv
import os

#Load .env file
dotenv_path = dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))
load_dotenv(dotenv_path)

# Create the application
def create_app():
    app = Flask(__name__)

    # Add any necessary configuration here
    app.config['SECRET_KEY'] = os.getenv('PYTHIN2_SECRET_KEY')
    
    # Add any necessary routes here

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
