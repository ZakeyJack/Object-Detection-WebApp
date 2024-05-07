from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, send_file
from werkzeug.utils import secure_filename
from datetime import timedelta
import os

from PIL import Image
from ultralytics import YOLO

app = Flask(__name__)
app.config['MODEL_FOLDER'] = 'models/'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['RESULT_FOLDER'] = 'results/'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def home():
    up_model = session.get('up_model', 'No model uploaded')
    up_file = session.get('up_file', 'No file uploaded')
    result_file = session.get('result_file', '')

    if up_file != 'No file uploaded':
        if result_file == '':
            return render_template('homepage.html', up_model=up_model, up_file=up_file, file_name=session['up_file'], file_type=session['up_file_type'], result_file='', result_file_type='')
        else:
            return render_template('homepage.html', up_model=up_model, up_file=up_file, file_name=session['up_file'], file_type=session['up_file_type'], result_file=session['result_file'], result_file_type=session['result_file_type'])
    else:
        return render_template('homepage.html', up_model=up_model, up_file=up_file, file_name='', file_type='')

@app.route('/model_upload', methods=['POST'])
def model_upload():
    model = request.files['model']
    session['up_model'] = secure_filename(model.filename)
    session['model_path'] = os.path.join(app.config['MODEL_FOLDER'], secure_filename(model.filename))
    model.save(session['model_path'])
    return redirect(url_for('home'))

@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    session['up_file'] = secure_filename(file.filename)
    session['up_file_type'] = file.filename.split('.')[-1].lower()
    session['file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
    file.save(session['file_path'])
    return redirect(url_for('home'))

@app.route('/serve_image/<filename>', methods=['GET'])
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/serve_video/<filename>')
def serve_video(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), mimetype=f"video/{session['up_file_type']}")

@app.route('/server_result_image/<filename>')
def serve_result_image(filename):
    return send_from_directory(app.config['RESULT_FOLDER'], f"predict/{filename}")

@app.route('/start', methods=['POST'])
def start_process():

    model_process = YOLO(session['model_path'])
    file = session['up_file']
    # # file = session['up_file'].replace(f".{session['up_file_type']}", ".avi")

    # result = model_process.predict(session['file_path'], save=True, project=app.config['RESULT_FOLDER'], name="predict")

    # session['result_file'] = file
    # session['result_file_path'] = os.path.join(app.config['RESULT_FOLDER'], f"predict/{file}")
    # session['result_file_type'] = session['result_file'].split('.')[-1]

    ...

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)