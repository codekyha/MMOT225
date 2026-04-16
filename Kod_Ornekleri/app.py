from flask import Flask
app = Flask(__name__)

@app.route('/topla/<a>/<b>')
def topla(a, b):
    sonuc = int(a) + int(b)
    return f"<h1>Hesap Makinesi: {a} + {b} = {sonuc}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)