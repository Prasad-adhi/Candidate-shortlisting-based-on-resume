from flask import Flask, render_template, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Scanner import similarity
import sqlite3

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
      f = request.files['file']
      f.save(secure_filename(f.filename))
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