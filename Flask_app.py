from flask import Flask, render_template, request,jsonify
from flask import send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Scanner import similarity
import sqlite3
import os

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///./Candidates.db"

db = SQLAlchemy(app)
class Candidate(db.Model):
    name=db.Column(db.String(300))
    contactno=db.Column(db.Numeric(10))
    emailid=db.Column(db.String(50),primary_key=True)
    filename=db.Column(db.String(50))

@app.route('/')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      app.config['UPLOAD_FOLDER']="./resumes"
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
      name=request.form['cname']
      number=request.form['c-cno']
      email=request.form['cemail']
      query="INSERT INTO Candidate(name,contactno,emailid,filename) VALUES ("+"'"+name+"',"+"'"+str(number)+"',"+"'"+email+"',"+"'"+f.filename+"')"
      conn=None
      try:
         conn = sqlite3.connect("Candidates.db")
         cur = conn.cursor()
         cur.execute(query)
         conn.commit()
         cur.close
      except:
         print()
      finally:
         if (conn):
            conn.close()
      
      return render_template('message.html')

@app.route('/login')
def login():
   return render_template('Login.html')

@app.route('/job_upload',methods=["GET","POST"])
def job_upload():
   if request.method == 'POST':
      app.config['UPLOAD_FOLDER']="./jobs"
      f = request.files['file']
      f.filename="job_description.docx"
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
      text={}
      text["text"]="File uploaded successfully"
      return jsonify(text)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/Result')
def Result():
   output = similarity()
   return jsonify(output)

@app.route('/resumes/<path:filename>')
def download(filename):
   return send_from_directory(directory="./resumes", filename=filename)

		
if __name__ == '__main__':
   app.run(debug = True)