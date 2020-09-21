from flask import Flask
import os

app=Flask(__name__, instance_relative_config=True)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

import views

if __name__ == "__main__":
    app.run(debug=True)