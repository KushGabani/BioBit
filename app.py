import os
import warnings
from flask import Flask, url_for, request, render_template
from werkzeug.utils import secure_filename
import tensorflow as tf
import numpy as np
import cv2

warnings.filterwarnings("ignore")

app = Flask(__name__)

categories = ["Cercospora", "Healthy", "Powder Mildew", "Yellow Mosaic"]


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        f = request.files['file']
        file_path = os.path.join(os.path.dirname(
            __file__), 'uploads', secure_filename(f.filename))
        f.save(file_path)

        img = cv2.imread(file_path)
        img = cv2.resize(img, (256, 256))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = np.expand_dims(img, axis=0)
        model = tf.keras.models.load_model("./nn_model/combined.hdf5")
        prediction = model.predict(img)
        result = str(np.max(prediction) * 100) + "% " + \
            categories[np.argmax(prediction)]

        return render_template('leaf-classification.html', result=result)
    else:
        return render_template('leaf-classification.html', result="")


if __name__ == "__main__":
    app.run(debug=True)
