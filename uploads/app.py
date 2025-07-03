from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "supersecretkey"  # needed for flash messages

UPLOAD_FOLDER = 'A/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/logout')
def logout():
    # This should ideally show the actual prediction result.
    result = request.args.get('result')
    return render_template('logout.html', result=result)

@app.route('/predict', methods=['POST'])
def predict():
    if 'pollenImage' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['pollenImage']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # TODO: Load your model and do actual prediction here
        # For now, let's pretend the model predicted "Pine Pollen"
        predicted_class = "Pine Pollen"

        return redirect(url_for('logout', result=predicted_class))

    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)


if __name__ == '__main__':
    app.run(debug=True)

