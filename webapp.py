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
        screens = request.form.getlist('multi_screens')
        strScreens = []
        if 'about' in screens:
            about = 1
            strScreens.append('about')
        else:
            about = 0
        if 'accountview' in screens:
            accountview = 1
            strScreens.append('accountview')
        else :
            accountview = 0
        if 'addproperty' in screens:
            addproperty = 1
            strScreens.append('addproperty')
        else:
            addproperty = 0
        if 'addvehicle' in screens:
            addvehicle = 1
            strScreens.append('addvehicle')
        else:
            addvehicle = 0
        if 'adverseactions' in screens:
            adverseactions = 1
            strScreens.append('adverseactions')
        else:
            adverseactions = 0
        if 'alerts' in screens:
            alerts = 1
            strScreens.append('alerts')
        else:
            alerts = 0
        if 'bankverification' in screens:
            bankverification = 1
            strScreens.append('bankverification')
        else:
            bankverification = 0
        if 'boostfriendslist' in screens:
            boostfriendslist = 1
            strScreens.append('boostfriendslist')
        else:
            boostfriendslist = 0
        if 'bvplaidlinkcontainer' in screens:
            bvplaidlinkcontainer = 1
            strScreens.append('bvplaidlinkcontainer')
        else:
            bvplaidlinkcontainer = 0
        if 'bvstats' in screens:
            bvstats = 1
            strScreens.append('bvstats')
        else:
            bvstats = 0
        if 'camerascreen' in screens:
            camerascreen = 1
            strScreens.append('camerascreen')
        else:
            camerascreen = 0
        if 'cc1' in screens:
            cc1 = 1
            strScreens.append('cc1')
        else:
            cc1 = 0
        if 'cc1category' in screens:
            cc1category = 1
            strScreens.append('cc1category')
        else:
            cc1category = 0
        if 'cc3' in screens:
            cc3 = 1
            strScreens.append('cc3')
        else:
            cc3 = 0
        if 'communityandinvites' in screens:
            communityandinvites = 1
            strScreens.append('communityandinvites')
        else:
            communityandinvites = 0
        if 'contactinfoconfirm' in screens:
            contactinfoconfirm = 1
            strScreens.append('contactinfoconfirm')
        else:
            contactinfoconfirm = 0
        if 'credit1' in screens:
            credit1 = 1
            strScreens.append('credit1')
        else:
            credit1 = 0
        if 'credit2' in screens:
            credit2 = 1
            strScreens.append('credit2')
        else:
            credit2 = 0
        if 'credit3' in screens:
            credit3 = 1
            strScreens.append('credit3')
        else:
            credit3 = 0
        if 'credit3alerts' in screens:
            credit3alerts = 1
            strScreens.append('credit3alerts')
        else:
            credit3alerts = 0
        if 'credit3container' in screens:
            credit3container = 1
            strScreens.append('credit3container')
        else:
            credit3container = 0
        if 'credit3cta' in screens:
            credit3cta = 1
            strScreens.append(credit3cta)
        else:
            credit3cta = 0
        if 'credit3dashboard' in screens:
            credit3dashboard = 1
            strScreens.append('credit3dashboard')
        else:
            credit3dashboard = 0
        if 'credits' in screens:
            credits = 1
            strScreens.append('credits')
        else:
            credits = 0
        if 'cycle' in screens:
            cycle = 1
            strScreens.append('cycle')
        else:
            cycle = 0
        if 'editprofile' in screens:
            editprofile = 1
            strScreens.append('editprofile')
        else:
            editprofile = 0
        if 'employmentinfo' in screens:
            employmentinfo = 1
            strScreens.append('employmentinfo')
        else:
            employmentinfo = 0
        if 'employmentsummary' in screens:
            employmentsummary = 1
            strScreens.append('employmentsummary')
        else:
            employmentsummary = 0
        if 'finances' in screens:
            finances = 1
            strScreens.append('finances')
        else:
            finances = 0
        if 'findfriendscycle' in screens:
            findfriendscycle = 1
            strScreens.append('findfriendscycle')
        else:
            findfriendscycle = 0
        if 'forgotpassword' in screens:
            forgotpassword = 1
            strScreens.append('forgotpassword')
        else:
            forgotpassword = 0
        if 'groupedinstitutions' in screens:
            groupedinstitutions = 1
            strScreens.append('groupedinstitutions')
        else:
            groupedinstitutions = 0
        if 'history' in screens:
            history = 1
            strScreens.append('history')
        else:
            history = 0
        if 'home' in screens:
            home = 1
            strScreens.append('home')
        else:
            home = 0
        if 'idandselfiecamerascreen' in screens:
            idandselfiecamerascreen = 1
            strScreens.append('idandselfiecamerascreen')
        else:
            idandselfiecamerascreen = 0
        if 'identityverification' in screens:
            identityverification = 1
            strScreens.append('identityverification')
        else:
            identityverification = 0
        if 'idscreen' in screens:
            idscreen = 1
            strScreens.append('idscreen')
        else:
            idscreen = 0
        if 'instantloanssn' in screens:
            instantloanssn = 1
            strScreens.append('instantloanssn')
        else:
            instantloanssn = 0
        if 'instantoffercreateaccount' in screens:
            instantoffercreateaccount = 1
            strScreens.append('instantoffercreateaccount')
        else:
            instantoffercreateaccount = 0
        if 'institutions' in screens:
            institutions = 1
            strScreens.append('institutions')
        else:
            institutions = 0
        if 'joinscreen' in screens:
            joinscreen = 1
            strScreens.append('joinscreen')
        else:
            joinscreen = 0
        if 'landingscreen' in screens:
            landingscreen = 1
            strScreens.append('landingscreen')
        else:
            landingscreen = 0
        if 'leaderboard' in screens:
            leaderboard = 1
            strScreens.append('leaderboard')
        else:
            leaderboard = 0
        if 'listpicker' in screens:
            listpicker = 1
            strScreens.append('listpicker')
        else:
            listpicker = 0
        if 'llloanamount' in screens:
            llloanamount = 1
            strScreens.append('llloanamount')
        else:
            llloanamount = 0
        if 'loan' in screens:
            loan = 1
            strScreens.append('loan')
        else:
            loan = 0
        if 'loan1' in screens:
            loan1 = 1
            strScreens.append('loan1')
        else:
            loan1 = 0
        if 'loan2' in screens:
            loan2 = 1
            strScreens.append('loan2')
        else:
            loan2 = 0
        if 'loan3' in screens:
            loan3 = 1
            strScreens.append('loan3')
        else:
            loan3 = 0
        if 'loan4' in screens:
            loan4 =1
            strScreens.append('loan4')
        else:
            loan4 = 0
        if 'loanappagreement' in screens:
            loanappagreement = 1
            strScreens.append('loanappagreement')
        else:
            loanappagreement = 0
        if 'loanappbankinfo' in screens:
            loanappbankinfo = 1
            strScreens.append('loanappbankinfo')
        else:
            loanappbankinfo = 0
        if 'loanappconfirmwithdrawal' in screens:
            loanappconfirmwithdrawal =1 
            strScreens.append('loanappconfirmwithdrawal')
        else:
            loanappconfirmwithdrawal = 0
        if 'loanappdenied' in screens:
            loanappdenied =1
            strScreens.append('loanappdenied')
        else:
            loanappdenied = 0
        if 'loanappesign' in screens:
            loanappesign = 1
            strScreens.append('loanappesign')
        else:
            loanappesign = 0
        if 'loanapploan4' in screens:
            loanapploan4 =1
            strScreens.append('loanapploan4')
        else:
            loanapploan4 =0
        if 'loanapppaymentschedule' in screens:
            loanapppaymentschedule =1
            strScreens.append('loanapppaymentschedule')
        else:
            loanapppaymentschedule=0
        if 'loanapppromocode' in screens:
            loanapppromocodea = 1
            strScreens.append('loanapppromocodea')
        else:
            loanapppromocodea =0
        if 'loanappreasons' in screens:
            loanappreasons = 1
            strScreens.append('loanappreasons')
        else:
            loanappreasons = 0
        if 'loanapprequestamount' in screens:
            loanapprequestamount = 1
            strScreens.append('loanapprequestamount')
        else:
            loanapprequestamount =0
        if 'loanappschedulecall' in screens:
            loanappschedulecall =1
            strScreens.append('loanappschedulecall')
        else:
            loanappschedulecall =0
        if 'loanappsuccess' in screens:
            loanappsuccess =1
            strScreens.append('loanappsuccess')
        else:
            loanappsuccess =0
        if 'loanappverifybankinfo' in screens:
            loanappverifybankinfo =1
            strScreens.append('loanappverifybankinfo')
        else:
            loanappverifybankinfo = 0
        if 'loanappwithdrawn' in screens:
            loanappwithdrawn = 1
            strScreens.append('loanappwithdrawn')
        else:
            loanappwithdrawn = 0
        if 'location' in screens:
            location =1
            strScreens.append('location')
        else:
            location = 0
        if 'login' in screens:
            login =1
            strScreens.append('login')
        else:
            login = 0
        if 'loginform' in screens:
            loginform = 1
            strScreens.append('loginform')
        else:
            loginform = 0
        if 'managefinances' in screens:
            managefinances =1
            strScreens.append('managefinances')
        else:
            managefinances =0
        if 'mlwebview' in screens:
            mlwebview =1
            strScreens.append('mlwebview')
        else:
            mlwebview = 0
        if 'networkfailure' in screens:
            networkfailure = 1
            strScreens.append('networkfailure')
        else:
            networkfailure = 0
        if 'networkuser' in screens:
            networkuser = 1
            strScreens.append('networkuser')
        else:
            networkuser = 0
        if 'newcontactlistinvite' in screens:
            newcontactlistinvite = 1
            strScreens.append('newcontactlistinvite')
        else:
            newcontactlistinvite =0
        if 'payoff' in screens:
            payoff =1
            strScreens.append('payoff')
        else:
            payoff =0
        if 'product_review' in screens:
            product_review = 1
            strScreens.append('product_review')
        else:
            product_review =0
        if 'product_review2' in screens:
            product_review2 =1
            strScreens.append('product_review2')
        else:
            product_review2 = 0
        if 'product_review3' in screens:
            product_review3 =1
            strScreens.append('product_review3')
        else:
            product_review3 = 0
        if 'product_review4' in screens:
            product_review4 =1
            strScreens.append('product_review4')
        else:
            product_review4 = 0
        if 'product_review5' in screens:
            product_review5 =1
            strScreens.append('product_review5')
        else:
            product_review5 = 0
        if 'profileannualincome' in screens:
            profileannualincome =1
            strScreens.append('profileannualincome')
        else:
            profileannualincome =0
        if 'profilechildren' in screens:
            profilechildren = 1
            strScreens.append('profilechildren')
        else:
            profilechildren =0
        if 'profilecompanyname' in screens:
            profilecompanyname = 1
            strScreens.append('profilecompanyname')
        else:
            profilecompanyname =0
        if 'profileeducation' in screens:
            profileeducation = 1
            strScreens.append('profileeducation')
        else:
            profileeducation =0
        if 'profileeducationmajor' in screens:
            profileeducationmajor =1
            strScreens.append('profileeducationmajor')
        else:
            profileeducationmajor = 0
        if 'profileemploymentlength' in screens:
            profileemploymentlength = 1
            strScreens.append('profileemploymentlength')
        else:
            profileemploymentlength = 0
        if 'profilejobtitle' in screens:
            profilejobtitle = 1
            strScreens.append('profilejobtitle')
        else:
            profilejobtitle = 0
        if 'profilemaritalstatus' in screens:
            profilemaritalstatus =1
            strScreens.append('profilemaritalstatus')
        else:
            profilemaritalstatus = 0
        if 'profilepage' in screens:
            profilepage = 1
            strScreens.append('profilepage')
        else:
            profilepage = 0
        if 'profileproduct_review' in screens:
            profileproduct_review =1
            strScreens.append('profileproduct_review')
        else:
            profileproduct_review = 0
        if 'profileverifyincometype' in screens:
            profileverifyincometype = 1
            strScreens.append('profileverifyincometype')
        else:
            profileverifyincometype =0
        if 'profileverifyssn' in screens:
            profileverifyssn =1
            strScreens.append('profileverifyssn')
        else:
            profileverifyssn = 0
        if 'providerlist' in screens:
            providerlist =1
            strScreens.append('providerlist')
        else:
            providerlist = 0       
        
        



        


        
        
        






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