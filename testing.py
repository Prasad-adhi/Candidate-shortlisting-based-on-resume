import sqlite3
query="SELECT * FROM Candidate"
#query="DELETE FROM Candidate"
conn=None
try:
    conn = sqlite3.connect("Candidates.db")
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    cur.close
except:
    print("Error")
finally:
    if (conn):
        conn.close()
