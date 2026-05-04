from flask import Flask, render_template, request
import os
from model import detect_anomalies

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        df, anomalies = detect_anomalies(file_path)

        return render_template('result.html',
                               total=len(df),
                               fraud=len(anomalies),
                               data=anomalies.to_html())

    return "File upload failed"

if __name__ == '__main__':
    app.run(debug=True)