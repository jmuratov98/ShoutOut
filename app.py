# external imports
from flask import Flask, request, render_template
from flask_cors import CORS

# internal imports
import model as dbHandler

app = Flask(__name__)

CORS(app)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "GET":
        pass

    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        dbHandler.insertUser(email, password)

    users = dbHandler.getUser()
    return render_template('index.html', users=users)

@app.route('/users/')
def users():
    users = dbHandler.getUser()
    return render_template('users.html', users=users)

if __name__ == "__main__":
    app.run(debug = True)