from flask import Flask
from flask import request
from flask import Response
import json 
import mysql.connector
import datetime



app = Flask(__name__)

#class Task(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #titre = db.Column(db.String(20), nullable=False)
    #description = db.Column(db.Text)
    #date_posted = db.Column(db.DateTime, default=datetime.today().date(), nullable=False)
    #date_due = db.Column(db.DateTime, nullable=False)
    #time = db.Column(db.Time, nullable=False)
    
liste_tache = [{'id':1, 'titre': "Faire le TP", 'description': "web service",'deadline':"20210226", 'done':1}, {'id':2, 'titre': "Python", 'description': "Epsi",'deadline':"20210227", 'done':0}]


@app.route('/todo', methods = ['GET','POST'])
def taches_faire():
    if request.method == 'GET':
        json_liste = json.dumps(liste_tache, ensure_ascii=False).encode('utf8')
        return Response(json_liste, mimetype ='text/json')

    elif request.method == 'POST':
        return '"id":'+id+',"titre":'+titre+',"description"='+description+',"deadline":'+deadline+''


@app.route('/todo/<id>', methods = ['GET','POST'])
def infos ():
    if request.method == 'POST':
        return Response(json, mimetype ='text/json')
    else :
        return 'db.Model'


@app.route('/todo/?date', methods = ['GET','POST'])
def date_choisie ():
    if request.method =='GET':
        return Response(json, mimetype ='text/json')
    else :
        return 'date_due'

@app.route('/todo/create', methods = ['GET','POST'])
def create ():
    if request.method == 'POST':
        my_list = ['id', 'titre', 'description','deadline','done'] 
        my_list.append('id', 'titre', 'description','deadline','done') 
        print (my_list)
        if request.get_json(silent=True) is not None:
            params = reqest.get_json()
            params1 = params['id']
            params1 = params['titre']
            params2 = params['description']
            params3 = params['deadline']
            params3 = params['done']
        elif request.form.get('param') is not None:
            param = request.form.get('param')

    else :
        return 'Error not found', 404


@app.route('/todo/<modify>', methods = ['PUT','PATCH'])
def modifier():
    liste_tache = [{'id', 'titre', 'description','date_posted'}]
    if request.method == 'PATCH':
        #liste_tache['id' 1] = 4
        print (liste_tache)
    
    else:  
        return 'Error not found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=8080,
    user="",
    password="s3cre3t!")

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT CURDATE()")

# Fetch one result
row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

# Close connection
cnx.close()