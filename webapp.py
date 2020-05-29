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
            loanapppromocode = 1
            strScreens.append('loanapppromocodea')
        else:
            loanapppromocode =0
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
        if 'referralcontainer' in screens:
            referralcontainer = 1
            strScreens.append('referralcontainer')
        else:
            referralcontainer =0
        if 'referrals' in screens:
            referrals =1
            strScreens.append('referrals')
        else:
            referrals =0
        if 'referralscreen' in screens:
            referralscreen=1
            strScreens.append('referralscreen')
        else:
            referralscreen=0
        if 'resendtoken' in screens:
            resendtoken = 1
            strScreens.append('resendtoken')
        else:
            resendtoken = 0
        if 'reviewcreditcard' in screens:
            reviewcreditcard =1
            strScreens.append('reviewcreditcard')
        else:
            reviewcreditcard =0
        if 'rewarddetail' in screens:
            rewarddetail = 1
            strScreens.append('rewarddetail')
        else:
            rewarddetail = 0
        if 'rewardjoinscreen' in screens:
            rewardjoinscreen = 1
            strScreens.append('rewardjoinscreen')
        else:
            rewardjoinscreen = 0
        if 'rewards' in screens:
            rewards = 1
            strScreens.append('rewards')
        else:
            rewards = 0
        if 'rewardscontainer' in screens:
            rewardscontainer = 1
            strScreens.append('rewardscontainer')
        else:
            rewardscontainer =0
        if 'saving1' in screens:
            saving1 = 1
            strScreens.append('saving1')
        else:
            saving1 = 0
        if 'saving10' in screens:
            saving10 = 1
            strScreens.append('saving10')
        else:
            saving10 = 0
        if 'saving2' in screens:
            saving2 = 1
            strScreens.append('saving2')
        else:
            saving2 = 0
        if 'saving2amount' in screens:
            saving2amount = 1
            strScreens.append('saving2amount')
        else:
            saving2amount=0
        if 'saving4' in screens:
            saving4 =1
            strScreens.append('saving4')
        else:
            saving4 = 0
        if 'saving5' in screens:
            saving5 =1
            strScreens.append('saving5')
        else:
            saving5=0
        if 'saving6' in screens:
            saving6 = 1
            strScreens.append('saving6')
        else:
            saving6=0
        if 'saving7' in screens:
            saving7 =1
            strScreens.append('saving7')
        else:
            saving7=0
        if 'saving8' in screens:
            saving8 =1
            strScreens.append('saving8')
        else:
            saving8 = 0
        if 'saving9' in screens:
            saving9 = 1
            strScreens.append('saving9')
        else:
            saving9=0
        if 'savinggoaledit' in screens:
            savinggoaledit = 1
            strScreens.append('savinggoaledit')
        else:
            savinggoaledit = 0
        if 'savinggoalincomesalary' in screens:
            savinggoalincomesalary = 1
            strScreens.append('savinggoalincomesalary')
        else:
            savinggoalincomesalary=0
        if 'savinggoalother' in screens:
            savinggoalother=1
            strScreens.append('savinggoalother')
        else:
            savinggoalother=0
        if 'savinggoalpreview' in screens:
            savinggoalpreview = 1
            strScreens.append('savinggoalpreview')
        else:
            savinggoalpreview=0
        if 'scanpreview' in screens:
            scanpreview =1
            strScreens.append('scanpreview')
        else:
            scanpreview=0
        if 'securitymodal' in screens:
            securitymodal=1
            strScreens.append('securitymodal')
        else:
            securitymodal=0
        if 'selectinstitution' in screens:
            selectinstitution =1
            strScreens.append('selectinstitution')
        else:
            selectinstitution=0
        if 'settings' in screens:
            settings=1
            strScreens.append('settings')
        else:
            settings=0
        if 'signup' in screens:
            signup =1
            strScreens.append('signup')
        else:
            signup=0
        if 'signupemail' in screens:
            signupemail = 1
            strScreens.append('signupemail')
        else:
            signupemail=0
        if 'signupname' in screens:
            signupname=1
            strScreens.append('signupname')
        else:
            signupname=0
        if 'splash' in screens:
            splash=1
            strScreens.append('splash')
        else:
            splash=0
        if 'transactionlist' in screens:
            transactionlist=1
            strScreens.append('transactionlist')
        else:
            transactionlist=0
        if 'verifyannualincome' in screens:
            verifyannualincome =1
            strScreens.append('verifyannualincome')
        else:
            verifyannualincome=0
        if 'verifybankinfo' in screens:
            verifybankinfo=1
            strScreens.append('verifybankinfo')
        else:
            verifybankinfo=0
        if 'verifycountry' in screens:
            verifycountry=1
            strScreens.append('verifycountry')
        else:
            verifycountry=0
        if 'verifydateofbirth' in screens:
            verifydateofbirth=1
            strScreens.append('verifydateofbirth')
        else:
            verifydateofbirth=0
        if 'verifyhousing' in screens:
            verifyhousing=1
            strScreens.append('verifyhousing')
        else:
            verifyhousing=0
        if 'verifyhousingamount' in screens:
            verifyhousingamount =1
            strScreens.append('verifyhousingamount')
        else:
            verifyhousingamount=0
        if 'verifyincometype' in screens:
            verifyincometype=1
            strScreens.append('verifyincometype')
        else:
            verifyincometype=0
        if 'verifymobile' in screens:
            verifymobile=1
            strScreens.append('verifymobile')
        else:
            verifymobile=0
        if 'verifyphone' in screens:
            verifyphone=1
            strScreens.append('verifyphone')
        else:
            verifyphone=0
        if 'verifyssn' in screens:
            verifyssn=1
            strScreens.append('verifyssn')
        else:
            verifyssn=0
        if 'verifytoken' in screens:
            verifytoken=1
            strScreens.append('verifytoken')
        else:
            verifytoken=0
        if 'webview' in screens:
            webview=1
            strScreens.append('webview')
        else:
            webview=0
        if 'welcomebankverification' in screens:
            welcomebankverification=1
            strScreens.append('welcomebankverification')
        else:
            welcomebankverification=0
        if 'yournetwork' in screens:
            yournetwork=1
            strScreens.append('yournetwork')
        else:
            yournetwork=0
        
        

        datainput = [[day,hour,age,nmsc,mg,feat,lk, about, accountview, addproperty, addvehicle, adverseactions, alerts, bankverification, 
        boostfriendslist, bvplaidlinkcontainer, bvstats, camerascreen, cc1, cc1category, cc3, communityandinvites, contactinfoconfirm, 
        credit1, credit2, credit3, credit3alerts, credit3container, credit3cta, credit3dashboard, credits, cycle, editprofile, 
        employmentinfo, employmentsummary, finances, findfriendscycle, forgotpassword, groupedinstitutions, history, home, 
        idandselfiecamerascreen, identityverification, idscreen, instantloanssn, instantoffercreateaccount, institutions, joinscreen, 
        landingscreen, leaderboard, listpicker, llloanamount, loan, loan1, loan2, loan3, loan4, loanappagreement, loanappbankinfo, 
        loanappconfirmwithdrawal, loanappdenied, loanappesign, loanapploan4, loanapppaymentschedule, loanapppromocode, 
        loanappreasons, loanapprequestamount, loanappschedulecall, loanappsuccess, loanappverifybankinfo, loanappwithdrawn, location, login, 
        loginform, managefinances, mlwebview, networkfailure, networkuser, newcontactlistinvite, payoff, product_review, product_review2, 
        product_review3, product_review4, product_review5, profileannualincome, profilechildren, profilecompanyname, profileeducation, 
        profileeducationmajor, profileemploymentlength, profilejobtitle, profilemaritalstatus, profilepage, profileproduct_review, 
        profileverifyincometype, profileverifyssn, providerlist, referralcontainer, referrals, referralscreen, resendtoken, reviewcreditcard, 
        rewarddetail, rewardjoinscreen, rewards, rewardscontainer, saving1, saving10, saving2, saving2amount, saving4, saving5, saving6, 
        saving7, saving8, saving9, savinggoaledit, savinggoalincomesalary, savinggoalother, savinggoalpreview, scanpreview, securitymodal, 
        selectinstitution, settings, signup, signupemail, signupname, splash, transactionlist, verifyannualincome, verifybankinfo, 
        verifycountry, verifydateofbirth, verifyhousing, verifyhousingamount, verifyincometype, verifymobile, verifyphone, verifyssn, 
        verifytoken, webview, welcomebankverification, yournetwork]]


        pred = gradient.predict(datainput)[0]
        proba = gradient.predict_proba(datainput)[0]
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
            like=strLike, screens=strScreens, result= rslt, proba = prbb, color = color)


if __name__ == '__main__':
    coba = joblib.load('model_cobain')
    gradient = joblib.load('model_gradient')
    app.run(debug=True, port=4400)