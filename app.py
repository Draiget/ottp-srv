import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8756)

@app.route('/')
def hello_world():
    return jsonify(error = True, message = "stub_page")

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        file = request.files['image']
        file.read()
        # f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

        # Here file is
        # file.save(f)
        return jsonify(error = False, body = {
            "description": "empty",
            "name": "empty",
            "price": 0,
            "body": "unknown",
            "color": "transparent",
            "transmission": "auto",
            "engine": "empty",
            "rudder": "empty",
        })
    except:
        return jsonify(error=False, message="stub_page")