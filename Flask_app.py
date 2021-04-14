from flask import Flask, render_template, request,jsonify
from werkzeug.utils import secure_filename
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Scanner import similarity

app = Flask(__name__)

@app.route('/')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      f1 = open("database.txt", "a")
      f1.write(f.filename)
      f1.write("\n")
      f1.close()
      return 'file uploaded successfully'

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/Result')
def Result():
    output = similarity()
    return jsonify(output)
		
if __name__ == '__main__':
   app.run(debug = True)