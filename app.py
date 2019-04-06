import ntpath
import os
import urllib.request

import request
import traceback

from flask import Flask, render_template, request, jsonify
from flask_cors import cross_origin

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/')
def hello_world():
    return jsonify(error = False, message = "stub_page")

# @cross_origin()
# @app.route('/api/obtain/', methods=['POST'])
# def obtain_file():
#     try:
#         file = request.form['img']
#         print("Getting file from %s" % file)
#
#         open(ntpath.basename(file), 'wb').write(urllib.request.urlopen(file).read())
#
#         # Here file is
#         # file.save(f)
#         return jsonify(error = False, body = {
#             "car_brand": "Audi",
#             "car_model": "empty",
#             "price": 0,
#             "year": 0,
#             "body": "empty",
#             "color": "transparent",
#             "engine_volume": "empty",
#             "engine_power": "empty",
#             "engine_type": "empty",
#             "transmission": "empty",
#             "rudder": "empty",
#             "to_download": file
#         })
#     except Exception as e:
#         print(traceback.format_exc())
#         return jsonify(error = True, message = str(e))

@cross_origin(origins="*")
@app.route('/api/upload/', methods=['OPTIONS'])
def upload_file_opts():
    return jsonify(error = False, message = "dummy_options")

@cross_origin(origins="*")
@app.route('/api/upload/', methods=['POST'])
def upload_file():
    try:
        file = request.files['file']
        file.read()
        # f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

        # Here file is
        # file.save(f)
        return jsonify(error = False, body = {
            "car_brand": "Audi",
            "car_model": "empty",
            "price": 0,
            "year": 0,
            "body": "empty",
            "color": "transparent",
            "engine_volume": "empty",
            "engine_power": "empty",
            "engine_type": "empty",
            "transmission": "empty",
            "rudder": "empty",
        })
    except Exception as e:
        print(traceback.format_exc())
        return jsonify(error = True, message = str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8756)