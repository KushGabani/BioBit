import io
import warnings
import shutil
from flask import Flask, url_for, request, render_template
from werkzeug.utils import secure_filename

warnings.filterwarnings("ignore")

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('leaf-classification.html')

if __name__ == "__main__":
    app.run(debug=True)