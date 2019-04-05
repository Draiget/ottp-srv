import os
import traceback

from flask import Flask, render_template, request, jsonify, logging
from flask_cors import cross_origin

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/')
def hello_world():
    return jsonify(error = False, message = "stub_page")

@cross_origin()
@app.route('/api/upload/', methods=['POST'])
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
    except Exception as e:
        logging.error(traceback.format_exc())
        return jsonify(error = True, message = e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8756)