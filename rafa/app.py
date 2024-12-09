from flask import Flask
from database import init_db
from controller import biblioteca_controller

app = Flask(__name__)

app.register_blueprint(biblioteca_controller)

if __name__ == "__main__":
    app.run(debug=True) 
    init_db(app)