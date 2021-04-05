import pyrebase

config = {
    "apiKey": "AIzaSyC-ZcUe-TdCuHij2n0S4DXibz6XWVsgxrA",
    "authDomain": "tractor-c5bfe.firebaseapp.com",
    "databaseURL": "https://tractor-c5bfe-default-rtdb.firebaseio.com",
    "projectId": "tractor-c5bfe",
    "storageBucket": "tractor-c5bfe.appspot.com",
    "messagingSenderId": "754238013820",
    "appId": "1:754238013820:web:5a0384ffcae695b8d1a4f9",
    "measurementId": "G-LKYJT1N737"  
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def basic():
    consumerSizeOBJ =  db.child("consumers").child("size").get()
    currentSize = consumerSizeOBJ.val().get("count", 0)
    return str(currentSize)

if __name__ == "__main__":
    app.run(debug=True)
