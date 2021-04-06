from flask import Flask,request
from flask_bcrypt import *


app = Flask(__name__)
bcrypt = Bcrypt(app)

key = "22059512"

@app.route("/encrypt",methods=['POST'])
def encrypt():
    data_hash = bcrypt.generate_password_hash(request.form['data'])
    return data_hash

@app.route("/decrypt",methods=['POST'])
def decrypt():
    data_hash_check = bcrypt.check_password_hash(request.form['data'],key)
    return str(data_hash_check)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
