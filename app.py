import os
import warnings
import shutil
from flask import Flask, url_for, request, render_template
from werkzeug.utils import secure_filename

warnings.filterwarnings("ignore")

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('leaf-classification.html')

@app.route("/predict", methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        print("Reached Here")
        f = request.files['file']
        print("Reached Here")
        file_path = os.path.join(os.path.dirname(__file__), 'uploads', secure_filename(f.filename))
        f.save(file_path)
        return render_template("leaf-classification.html")
        # prediction = get_prediction_from_cnn(file_path)
        # return prediction
    else:
        print("Else here")
        return "hi"

if __name__ == "__main__":
    app.run(debug=True)