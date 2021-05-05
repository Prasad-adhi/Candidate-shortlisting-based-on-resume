import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sqlite3

def similarity():
    query="SELECT * FROM Candidate"
    conn=None
    rows=[]
    score=[]
    try:
        conn = sqlite3.connect("Candidates.db")
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        conn.commit()
        cur.close
    except:
        print("Error")
    finally:
        if (conn):
            conn.close()
    for line in rows:
        resume = docx2txt.process(line[3])
        job_desc = docx2txt.process("job_description.docx")
        text = [resume,job_desc]
        cv=CountVectorizer()
        count_matrix=cv.fit_transform(text)
        score.append(cosine_similarity(count_matrix)[0][1])
    for i in range(0,len(rows)-1):
        for j in range(0,len(rows)-i-1):
            if(score[j]<score[j+1]):
                temp1=score[j]
                score[j]=score[j+1]
                score[j+1]=temp1
                temp2=rows[j]
                rows[j]=rows[j+1]
                rows[j+1]=temp2
    output={}
    output['Names'],output['Contact'],output['Email'],output['File'],output['Score']=[],[],[],[],score
    for i in range(len(rows)):
        output['Names'].append(rows[i][0])
        output['Contact'].append(rows[i][1])
        output['Email'].append(rows[i][2])
        output['File'].append(rows[i][3])
    return output
