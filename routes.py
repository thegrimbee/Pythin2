from flask import Flask, Blueprint

app = Flask(__name__)
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Hello, World!'

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
