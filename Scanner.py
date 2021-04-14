import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def similarity():
    f = open("database.txt", "r")
    score=[]
    names=f.readlines()
    for line in names:
        resume = docx2txt.process(line[:len(line)-1])
        job_desc = docx2txt.process("job_description.docx")
        text = [resume,job_desc]
        cv=CountVectorizer()
        count_matrix=cv.fit_transform(text)
        score.append(cosine_similarity(count_matrix)[0][1])
    for i in range(0,len(names)-1):
        for j in range(0,len(names)-i-1):
            if(score[j]<score[j+1]):
                temp1=score[j]
                score[j]=score[j+1]
                score[j+1]=temp1
                temp2=names[j]
                names[j]=names[j+1]
                names[j+1]=temp2
    output={}
    output['Names'],output['Score']=names,score
    return output

print(similarity())