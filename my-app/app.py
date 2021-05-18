import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from flask import send_file, make_response


app=Flask(__name__, template_folder='./templates')

app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

# Make directory if uploads is not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extension you can set your own
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'log'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#@app.route('/')
#def upload_form():
#    return render_template('upload.html')
@app.route('/get/<filename>', methods=["GET"])
def getfile(filename):
    file_path = UPLOAD_FOLDER + '/' + filename
    print(file_path)
    if os.path.exists(file_path):
        return make_response(send_file(file_path, attachment_filename = filename, add_etags = False, cache_timeout = 0))
    else:
        return "404"

@app.route('/upload', methods=['POST'])
def upload_file():
  if request.method == 'POST':
  
  #        if 'files[]' not in request.files:
  #            flash('No file part')
  #            return redirect(request.url)
  
      files = request.files.getlist('files')
      print(files)
  
      for file in files:
          if file and allowed_file(file.filename):
              filename = secure_filename(file.filename)
      #flash(filename)
              file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  
      #flash('File(s) successfully uploaded')
  #        return redirect('/')
  return {'msg':'File uploaded successfully'}

if __name__ == "__main__":
    app.run(host='172.16.21.14',port=5001,debug=True,threaded=True)
