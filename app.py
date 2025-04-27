from flask import Flask, render_template, jsonify, send_from_directory
import os
import pandas as pd
from io import StringIO

app = Flask(__name__)

# Load and clean the CSV
with open("Anniversary.csv", "rb") as f:
    content = f.read()
    decoded = content.decode("utf-8", errors="replace")
    df = pd.read_csv(StringIO(decoded))

# Replace goblin chars like â¦ with hyphen
for col in df.columns:
    df[col] = df[col].astype(str).str.replace("â¦", "-", regex=False)

df = df.fillna("")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/map')
def map_view():
    return render_template('map.html')

@app.route('/clues')
def clues():
    return jsonify(df.to_dict(orient='records'))

@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'media'), filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
