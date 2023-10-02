import sys
import os
import logging
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import model_from_json
import json
from flask_cors import CORS
from flask import Flask, request, render_template, send_from_directory
from get_dataset import get_img
from predict import predict

#application settings
app = Flask(__name__)
CORS(app)

# Application directory for inputs and training: comment this if testing without docker
app.config['model'] = "Model/model.json"
app.config['weights'] = "Model/weights.h5"
app.config['input_image'] = "Input"
app.config["server_ip"] = "localhost" # use "localhost" for testing on local environment

# to take absolute path irrespective of OS
os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    """Return a friendly HTTP greeting."""
    return 'Image Classification API is running'

@app.route('/Input')
def get_file(path='input.jpg'):
    return send_from_directory('Input/', path)

@app.route('/classification', methods=["GET", "POST"])
def classification():
    if request.method == "POST":
        if request.files:
            img = request.files['image']
            img.filename = "input.jpg"
            file_path = os.path.join(app.config['input_image'], img.filename)
            img.save(file_path)

            img = get_img(img)
            X = np.zeros((1, 64, 64, 3), dtype='float64')
            X[0] = img

            # Getting model:
            model_file = open(app.config['model'], 'r')
            model = model_file.read()
            model_file.close()
            model = model_from_json(model)

            # Getting weights
            model.load_weights(app.config['weights'])
            
            # Running predictions
            Y = predict(model, X)

            return render_template('predict.html', output=Y)
            # return json.dumps({"status": "success", "output": Y})
    else:
        return render_template('predict.html')

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return json.dumps({'status':'failed','message':
        """An internal error occurred: <pre>{}</pre>See logs for full stacktrace.""".format(e),
                       'result': []})

if __name__ == '__main__':
    app.run(host=app.config["server_ip"], port=8188)