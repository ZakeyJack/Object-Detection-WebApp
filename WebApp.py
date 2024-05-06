from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from werkzeug.utils import secure_filename
from datetime import timedelta
import os

app = Flask(__name__)
app.config['MODEL_FOLDER'] = 'models/'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def home():
    up_model = session.get('up_model', 'No model uploaded')
    up_file = session.get('up_file', 'No file uploaded')
    if up_file != 'No file uploaded':
        return render_template('homepage.html', up_model=up_model, up_file=up_file, file_name=session['up_file'], file_type=session['up_file_type'])
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
    session['up_file_type'] = file.filename.split('.')[-1]
    session['file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
    file.save(session['file_path'])
    return redirect(url_for('home'))

@app.route('/serve_image/<filename>', methods=['GET'])
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)