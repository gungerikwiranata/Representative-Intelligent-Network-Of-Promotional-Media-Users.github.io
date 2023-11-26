from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', message='No file part')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', message='No selected file')

    if file:
        df = pd.read_excel(file)
        # Lakukan apa yang Anda inginkan dengan dataframe (df) di sini
        return df.to_html()

if __name__ == '__main__':
    app.run(debug=True)
