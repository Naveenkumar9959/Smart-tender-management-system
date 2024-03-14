from flask import Flask,url_for,render_template,flash,session,redirect,request
import mysql.connector
import pandas as pd
import random
from datetime import datetime
from datetime import date
from datetime import timedelta
import smtplib
import hashlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
app=Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="smart_tender")
cursor = mydb.cursor()
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/mansonry')
def mansonry():
    return render_template('masonry.html')
@app.route('/grid')
def grid():
    return render_template('grid.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/tender')
def tender():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c=a+b
    print(a)
    return render_template('tender.html',a=a,b=b,c=c)

@app.route('/tenderback',methods = ["POST"])
def tenderback():
    print("*******************")
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        pwd=request.form['pwd']
        cpwd=request.form['cpwd']
        pno=request.form['pno']
        addr=request.form['addr']
        print("&&&&&&&&&")
        sql = "select * from tenders"
        result = pd.read_sql_query(sql, mydb)
        email1 = result['email'].values
        print(email1)
        if email in email1:
            flash("email already existed","warning")
            return render_template('tender.html')
        if (pwd == cpwd):
            sql = "INSERT INTO tenders (name,email,pwd,addr,pno) VALUES (%s,%s,%s,%s,%s)"
            val = (name, email, pwd, addr, pno)
            cursor.execute(sql, val)
            mydb.commit()
            flash("Successfully Registered", "warning")
            return render_template('tender.html')
        else:
            flash("Password and Confirm Password not same")
        return render_template('tender.html')

    return render_template('tender.html')

@app.route('/loginback',methods=['POST', 'GET'])
def loginback():
    if request.method == "POST":

        email = request.form['email']
        capt = request.form['capt']
        c = request.form['c']
        password1 = request.form['pwd']

        sql = "select * from tenders where email='%s' and pwd='%s' " % (email, password1)
        print('q')
        x = cursor.execute(sql)
        print(x)
        results = cursor.fetchall()
        print(results)
        global name
        name = results[0][1]
        print(name)
        session['fname'] = results[0][1]
        session['email'] = email
        if(capt==c):
            if len(results) > 0:
                flash("Welcome to website", "primary")
                return render_template('tenderhome.html', msg=results[0][1])

            else:
                flash("Login failed", "warning")
                return render_template('tender.html', msg="Login Failure!!!")
        else:
            flash("Captcha value mismatches please try again", "danger")
            return render_template('tender.html', msg="invalid value")

    return render_template('tender.html')


@app.route('/tenderhome')
def tenderhome():
    return render_template('tenderhome.html')

@app.route('/notification')
def notification():
    return render_template('notification.html')

@app.route('/notiback', methods=['POST','GET'])
def notiback():
    if request.method=='POST':
        now = datetime.now()
        email=session.get('email')
        currentDay = datetime.now().strftime('%Y-%m-%d')
        print(currentDay)
        edate=request.form['edate']
        obj=request.form['obj']
        cost=request.form['cost']
        print("***************")
        print(edate)
        if currentDay < edate:
            sql="insert into notifications(email,obj,cost,sdate,edate) values(%s,%s,%s,%s,%s)"
            val=(email,obj,cost,currentDay,edate)
            cursor.execute(sql,val)
            mydb.commit()
            flash("Notification submitted","success")
        else:
            flash("Previous data not allowed so please select valid data","danger")
            return render_template("notification.html")
        return redirect('notification')


@app.route('/bid')
def bid():
    return render_template('bid.html')



@app.route('/bidback',methods = ["POST"])
def bidback():
    print("*******************")
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        pwd=request.form['pwd']
        cpwd=request.form['cpwd']
        pno=request.form['pno']
        addr=request.form['addr']
        print("&&&&&&&&&")
        sql = "select * from tenders"
        result = pd.read_sql_query(sql, mydb)
        email1 = result['email'].values
        print(email1)
        if email in email1:
            flash("email already existed","warning")
            return render_template('bid.html')
        if (pwd == cpwd):
            sql = "INSERT INTO bidders (name,email,pwd,addr,pno) VALUES (%s,%s,%s,%s,%s)"
            val = (name, email, pwd, addr, pno)
            cursor.execute(sql, val)
            mydb.commit()
            flash("Successfully Registered", "warning")
            return render_template('bid.html')
        else:
            flash("Password and Confirm Password not same")
        return render_template('bid.html')

    return render_template('bid.html')

@app.route('/bidlog',methods=['POST', 'GET'])
def bidlog():
    if request.method == "POST":

        email = request.form['email']
        password1 = request.form['pwd']

        sql = "select * from bidders where email='%s' and pwd='%s' " % (email, password1)
        print('q')
        x = cursor.execute(sql)
        print(x)
        results = cursor.fetchall()
        print(results)
        global name
        name = results[0][1]
        print(name)
        session['fname'] = results[0][1]
        session['email'] = email

        if len(results) > 0:
            flash("Welcome to website", "primary")
            return render_template('bidhome.html', msg=results[0][1])

        else:
            flash("Login failed", "warning")
            return render_template('bid.html', msg="Login Failure!!!")

    return render_template('bid.html')

@app.route('/bidhome')
def bidhome():
    return render_template('bidhome.html')
@app.route('/vnot')
def vnot():
    today = date.today()
    yesterday = today - timedelta(days=1)
    if today > yesterday:
        sql ="select * from notifications"
        x = pd.read_sql_query(sql, mydb)
        return render_template("vnot.html", cal_name=x.columns.values, row_val=x.values.tolist())
    else:
        flash("No tenders are available","warning")
        return render_template("vnot.html")
    return render_template("vnot.html")

@app.route('/maketender/<s>/<s1>/<s2>/<s3>/<s4>/<s5>')
def maketender(s=0,s1='',s2='',s3='',s4='',s5=''):
    print(s)
    return render_template('maketender.html', a=s,s1=s1,s2=s2,s3=s3,s4=s4,s5=s5)

@app.route('/maketenderback', methods=['POST','GET'])
def maketenderback():
    if request.method=='POST':
        a1 = request.form['a']
        s1 = request.form['s1']
        s2 = request.form['s2']
        s3 = request.form['s3']
        s4 = request.form['s4']
        s5 = request.form['s5']
        pan = request.form['pan']
        adhar = request.form['adhar']
        file =request.form['file']

        dd = "text_files/" + file
        print(dd)
        f = open(dd, "r")
        data = f.read()
        now = datetime.now()
        a=random.randint(500, 50000)
        email = session.get('email')

        datalen = int(len(data) / 2)
        print(datalen, len(data))
        g = 0
        a = ''
        b = ''
        c = ''
        for i in range(0, 2):
            if i == 0:
                a = data[g: datalen:1]
                # a=a.decode('utf-8')
                print(a)
                result = hashlib.sha1(a.encode())
                hash1 = result.hexdigest()

                print(hash1)
                print("===================================")
                # result = hashlib.sha1(a.encode())
                # hash1 = result.hexdigest()
                # print(hash1)
                print("++++++++++++++++++++++++++")
                # print(g)
                # print(len(data))
                # b = data[g: len(data):1]
                # print(c)

        print(g)
        print(len(data))
        c = data[datalen: len(data):1]
        # c = c.decode('utf-8')
        print(c)
        print("===================================")
        print("*****************************")
        result = hashlib.sha1(c.encode())
        hash2 = result.hexdigest()
        print(hash2)
        currentDay = datetime.now().strftime('%Y-%m-%d')
        t1 = datetime.now().strftime('%H:%M:%S')

        sql = "INSERT INTO tender_files (tid,temail,obj,cost,sdate,edate,email,pan,adhar,file,hash1,hash2,date,time1) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,AES_ENCRYPT(%s,'lakshmi'),%s,%s,%s,%s)"
        val = (a1, s1,s2,s3,s4,s5,email,pan,adhar,data, hash1, hash2, currentDay, t1)
        cursor.execute(sql, val)
        mydb.commit()
        sql = "select * from tender_files where time1='%s' " % (t1)
        x = pd.read_sql_query(sql, mydb)
        print("^^^^^^^^^^^^^")
        print(type(x))
        print(x)
        # x = x.drop(['demail'], axis=1)
        x = x.drop(['email'], axis=1)
        x = x.drop(['temail'], axis=1)
        x = x.drop(['hash1'], axis=1)
        x = x.drop(['hash2'], axis=1)
        x = x.drop(['id'], axis=1)
        x = x.drop(['time1'], axis=1)
        x = x.drop(['file'], axis=1)
        x = x.drop(['pan'], axis=1)
        x = x.drop(['adhar'], axis=1)
        flash("Tender submitted to tender office", "success")
        return render_template("maketender1.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/viewnot')
def viewnot():
    email=session.get('email')
    today = date.today()
    yesterday = today - timedelta(days=1)
    if today > yesterday:
        sql ="select * from notifications where email='%s'" %(email)
        x = pd.read_sql_query(sql, mydb)
        x = x.drop(['email'], axis=1)
        return render_template("viewnot.html", cal_name=x.columns.values, row_val=x.values.tolist())
    else:
        flash("No tenders are available","warning")
        return render_template("viewnot.html")
    return render_template("viewnot.html")


@app.route('/update/<s>/<s1>/<s2>/<s3>/<s4>')
def update(s=0,s1='',s2='',s3='',s4=''):
    print(s)
    return render_template('update.html', a=s,s1=s1,s2=s2,s3=s3,s4=s4)

@app.route("/upback", methods=['POST',"GET"])
def upback():
    if request.method=="POST":
        a=request.form['id']
        b=request.form['obj']
        c=request.form['cost']
        d=request.form['sdate']
        e=request.form['edate']
        sql = "update notifications set obj='%s',cost='%s',sdate='%s',edate='%s' where id='%s' " % (b, c, d, e, a)
        cursor.execute(sql)
        mydb.commit()
        flash("Successfully data updated", "success")
        return redirect(url_for('viewnot'))

@app.route('/delete/<s>')
def delete(s=0):
    x=s
    sql="delete from notifications where id='%s'" %(x)
    cursor.execute(sql)
    mydb.commit()
    flash("Successfully data deleted", "success")
    return redirect(url_for('viewnot'))

@app.route('/viewbid')
def viewbid():
    today = date.today()
    yesterday = today - timedelta(days=1)
    email=session.get('email')
    if today > yesterday:
        sql ="select * from tender_files where temail='%s'"%(email)
        x = pd.read_sql_query(sql, mydb)
        x = x.drop(['tid'], axis=1)
        x = x.drop(['time1'], axis=1)
        x = x.drop(['file'], axis=1)
        x = x.drop(['status'], axis=1)
        x = x.drop(['sdate'], axis=1)
        x = x.drop(['edate'], axis=1)
        x = x.drop(['obj'], axis=1)
        x = x.drop(['temail'], axis=1)
        return render_template("viewbid.html", cal_name=x.columns.values, row_val=x.values.tolist())
    else:
        flash("No bidders are available","warning")
        return render_template("viewbid.html")
    return render_template("viewbid.html")

@app.route('/vbidinfo/<s>/<s1>/<s2>')
def vbidinfo(s=0,s1='',s2=''):
    print(s)
    return render_template('vbidinfo.html', a=s,s1=s1,s2=s2)

@app.route("/down",methods=['POST','GET'])
def down():
    if request.method == 'POST':
        hash1 = request.form['s1']
        id = request.form['a']
        hash2 = request.form['s2']

        # sql = "select count(*),CONCAT(block1,block2,'') from reports where hash1='"+hash1+"' and hash2='"+hash2+"' and id='"+id+"' "
        sql= "select count(*), aes_decrypt(file, 'lakshmi') from tender_files where hash1 = '"+hash1+"' and hash2 = '"+hash2+"' and id='"+id+"'"
        x = pd.read_sql_query(sql, mydb)
        count=x.values[0][0]
        print(count)
        asss=x.values[0][1]
        asss=asss.decode('utf-8')

        print("^^^^^^^^^^^^^")
        if count==0:
            flash("Something wrong tray again","danger")
            return render_template("viewbid.html")
        if count==1:
            return render_template("downfile.html", msg=asss)

    return render_template("viewbid.html")

@app.route('/finalised/<s>/<s1>')
def finalised(s=0,s1=''):
    email=session.get('email')
    sql="select count(*) from tender_files where temail='%s' and email='%s'" %(email,s1)
    x = pd.read_sql_query(sql, mydb)
    count = x.values[0][0]
    print(x)
    if count==1:
        msg = 'Thanks for choosing online smart tender.'
        otp = "Congratuaations for woning this tender. "
        t = 'Regards,'
        t1 = 'Tender Officer.'
        mail_content = msg + '\n' + otp +'\n' + '\n' + t + '\n' + t1
        sender_address = 'harshar72888@gmail.com'
        sender_pass = 'BD9C31903203D58FBE509F99F48427A4D2D7'
        receiver_address = s1
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Smart Tender/Contract Management System Using Blockchain'

        message.attach(MIMEText(mail_content, 'plain'))
        ses = smtplib.SMTP('smtp.elasticemail.com', 2525)
        ses.starttls()
        ses.login(sender_address, sender_pass)
        text = message.as_string()
        ses.sendmail(sender_address, receiver_address, text)
        ses.quit()
        sql = "update tender_files set status='Completed' where id='%s'" % (s)
        cursor.execute(sql, mydb)
        mydb.commit()
        if count!=0:
            sql = "update tender_files set status='Cancel' where temail='%s' and email != '%s'" % (email,s1)
            cursor.execute(sql, mydb)
            mydb.commit()
            flash("Opinion sended to Bidders","Success")
            return redirect(url_for('viewbid'))
        return redirect(url_for('viewbid'))
    return redirect(url_for('viewbid'))

@app.route('/vresult')
def vresult():
    email=session.get("email")
    sql="select * from tender_files where status!='pending' and email='%s'" %(email)
    x = pd.read_sql_query(sql, mydb)
    x = x.drop(['id'], axis=1)
    x = x.drop(['tid'], axis=1)
    x = x.drop(['file'], axis=1)
    x = x.drop(['hash2'], axis=1)
    x = x.drop(['sdate'], axis=1)
    x = x.drop(['edate'], axis=1)
    x = x.drop(['hash1'], axis=1)
    x = x.drop(['temail'], axis=1)
    x = x.drop(['email'], axis=1)
    x = x.drop(['pan'], axis=1)
    x = x.drop(['adhar'], axis=1)


    return render_template('vresult.html', cal_name=x.columns.values, row_val=x.values.tolist())


if __name__=='__main__':
    app.run(debug=True)