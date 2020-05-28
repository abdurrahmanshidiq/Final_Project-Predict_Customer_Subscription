from flask import Flask, render_template, url_for, request, send_from_directory
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/')
def home ():
    return render_template('prediction.html')

@app.route('/insight')
def insight ():
    return render_template('insight_plot.html')

# @app.route('/storage/<path:x>')
# def storage(x):
#     return send_from_directory("storage", x)

@app.route('/result', methods=['POST', 'GET'])
def result ():
    if request.method == 'POST':
        input = request.form
        #dayofweek
        dayofweek = input['dayofweek']
        strDay = ''
        day = int()
        if dayofweek == 'sun':
            day = 0
            strDay = 'Sunday'
        elif dayofweek == 'mon':
            day = 1
            strDay = 'Monday'
        elif dayofweek == 'tue':
            day = 2
            strDay = 'Tuesday'
        elif dayofweek == 'wed':
            day = 3
            strDay = 'Wednesday'
        elif dayofweek == 'thu':
            day = 4
            strDay = 'Thursday'
        elif dayofweek == 'fri':
            day = 5
            strDay = 'Friday'
        else:
            day = 6
            strDay = 'Saturday'

        #minigame
        minigame = input['minigame']
        strGame = ''
        mg = int()
        if minigame == 'y':
            mg = 1
            strGame = 'Yes'
        else:
            mg = 0
            strGame = 'No'
        #used premium feature
        used_premium_feat = input['used_premium_feat']
        strFeat = ''
        feat = int()
        if used_premium_feat == 'y':
            feat = 1
            strFeat = 'Yes'
        else:
            feat = 0
            strFeat = 'No'
        #like
        like = input['like']
        strLike = ''
        lk = int()
        if like == 'y':
            lk = 1
            strLike = 'Yes'
        else:
            lk = 0
            strLike = 'No'
        #hour
        hour = int(input['hour'])
        #Age
        age = int(input['age'])
        #numscreens
        nmsc = int(input['numscreens'])

        # screens
        # screens = input['screens']




        datainput = [[day,hour,age,nmsc,mg,feat,lk]]
        pred = coba.predict(datainput)[0]
        proba = coba.predict_proba(datainput)[0]
        if pred == 0:
            prbb = round((proba[0]*100), 1)
            rslt = "Not Subscribe"
            color = "tomato"
        else:
            prbb = round((proba[1]*100), 1)
            rslt = "Subscribe"
            color = "mediumaquamarine"
        
        # return render_template('result.html')
        return render_template(
            'result.html', dayofweek=strDay, hour=hour, age=age, numscreens=nmsc, minigame=strGame, used_premium_feat=strFeat, 
            like=strLike,result= rslt, proba = prbb, color = color)


if __name__ == '__main__':
    coba = joblib.load('model_cobain')
    app.run(debug=True, port=4400)