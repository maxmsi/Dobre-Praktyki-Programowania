from flask import Flask,jsonify,request
from flask.sqlalchemy import SQLAlchemy

import os



basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)



#First page
@app.route("/")
def first_page():
  return "Aplikacja do ankietyzowania"





#Get all activities

@app.route('/harmodb/activities',methods=['GET'])
def getAllActivities():

    return jsonify({'Activities':harmonogramDB})



#Get specified activity by id

@app.route('/harmodb/activities/<HarmId>',methods=['GET'])
def getDayActivity(HarmId):

    harmo = [ harmoid for harmoid in harmonogramDB if (harmoid['id'] == HarmId) ]
    return jsonify({'Activites':harmo})



@app.route('/harmodb/activities/<HarmId>',methods=['PUT'])
def updateHarm(HarmId):

    em = [emp for emp in harmonogramDB if (emp['id'] == HarmId)]

    if 'day' in request.json:
        em[0]['day'] = request.json['day']

    if 'id' in request.json:
        em[0]['id'] = request.json['id']

    if 'activity' in request.json:

        em[0]['activity'] = request.json['activity']

    return jsonify({'Harmonogram': em[0]})




#new records
@app.route('/harmodb/activities',methods=['POST'])
def createHarm():

    dat = {

        'id': request.json['id'],
        'day': request.json['day'],
        'month': request.json['month'],
        'activity': request.json['activity'],
        'hour': request.json['hour']
    }
    harmonogramDB.append(dat)
    return jsonify(dat)


#delete elem
@app.route('/harmodb/activities/<elemId>',methods=['DELETE'])
def deleteHarm(elemId):

    elem = [el for el in harmonogramDB if (el['id'] == elemId)]
    harmonogramDB.remove(elem[0])

    return jsonify({'response':'Success'})


#local activites databse
harmonogramDB =[

      {
        'id': '0701',
        'day': '23.01.19',
        'hour': '13-14',
        'activity': 'Football training'

      },

      {
	    'id': '0702',
        'day': 'WT',
        'hour': '14:00',
        'month': 'July',
        'activity': 'Football training2'

      }

    ]

if __name__ == '__main__':
    app.run(debug=True)

