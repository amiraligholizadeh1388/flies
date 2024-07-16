from flask import Flask , render_template , request , redirect , url_for , flash
import pandas as pd
Bool = False
af = False
ac = False
form = [None , None , None , None , None]
data_flies = pd.read_csv('data_flies.csv')
cities = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
data = pd.read_csv('data.csv')
def check_fly(mabda , maghsad , city , flies):
    city = [i for i in city]
    flies = [i for i in flies]
    mabdaha = [i[0] for i in flies]
    maghsadha = [i[-1] for i in flies]
    if mabda and maghsad in city:
        if mabda in mabdaha:
            if maghsad in maghsadha:
                if f'{mabda}->{maghsad}' in flies:
                    return f'{mabda}->{maghsad}'
                else:
                    
                    his = [mabda]
                    a = mabda
                    while a != maghsad:
                        a = maghsadha[mabdaha.index(a)]
                        if a not in his:
                            his.append(a)
                        else:
                            his = his[0 : his.index(a)+1]
                    ticket = str(his)
                    ticket = ticket.replace('[' , '')
                    ticket = ticket.replace(']' , '')
                    ticket = ticket.replace(',' , '->')
                    ticket = ticket.replace(' ' , '')
                    ticket = ticket.replace("'" , '')
                    return ticket
            elif maghsad not in maghsadha:
                return 'ما همچین پروازی نداریم' + '1111'
        elif mabda not in mabdaha:
            return 'ما همچین پروازی نداریم' + '2222'
    elif mabda or maghsad not in city:
        return 'ما همچین پروازی نداریم' + '3333'

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/signin')
def signin():
    return render_template('signin.html')
@app.route('/admin')
def admin():
    if form[-2] == 'Amirali@1388' and form[-1] == '33259634a':
        return render_template("admin.html" , af=False , ac=False)
    else:
        return 'error 403 vorod gheyr ghanoni'

@app.route('/adding-fly' , methods=['GET', 'POST'])
def adding_fly():
    global data_flies
    if request.form['fly'] in data_flies['fly']:
        return render_template('info.html' , result='عملیات نا موفق بود:همچین پروازی وجود دارد')
    new_data_flies = pd.DataFrame({'fly' : [request.form['fly']]})
    new_data_flies.to_csv('data_flies.csv' , mode='a' , header=False , index=False)
    data_flies = pd.read_csv('data_flies.csv')
    return render_template('info.html' , result='عملیات موفقیت آمیز')

@app.route('/delete-fly' , methods=['GET', 'POST'])
def delete_fly():
    global data_flies
    data_flies = data_flies[data_flies['fly'] != str(request.form['del-fly'])]
    data_flies.to_csv('data_flies.csv', mode='w' , index=False)
    data_flies = pd.read_csv('data_flies.csv')
    return render_template('info.html' , result='عملیات موفقیت آمیز')
@app.route("/account" , methods=['GET' , 'POST'])
def account():
    global data , form , Bool
    form = request.form
    form = dict(form)
    form = list(form.values())
    first_name = [str(i) for i in data['first name']]
    last_name = [str(i) for i in data['first name']]
    phone_number = [str(i) for i in data['phone number']]
    username = [str(i) for i in data['username']]
    password = [str(i) for i in data['password']]
    if len(form) == 2:
        if form[0] in username and form[1] in password and username.index(form[0]) == password.index(form[1]) and form[0] == 'Amirali@1388' and form[1] == '33259634a':
            Bool = True
            return redirect(url_for('admin'))    
        if form[0] in username and form[1] in password and username.index(form[0]) == password.index(form[1]):
            return render_template("account.html" , name = first_name[username.index(form[0])])
        else:
            return redirect(url_for('login'))
    elif len(form) == 6:
        if form[3] not in username and form[2] not in phone_number and form[-1]==form[-2] and form[-2] not in password:
            new_data = pd.DataFrame({'first name' : [form[0]] , 'last name' : [form[1]] , 'phone number' : [form[2]] , 'username' : [form[3]] , 'password' :  [form[4]]})
            new_data.to_csv('data.csv' , mode='a' , header=False , index=False)
            data = pd.read_csv('data.csv')

            return render_template('account.html' , name=form[0])
        else:
            return redirect(url_for('signin') ,)
    else:
        return 'error' 
@app.route('/info' ,methods=['POST' , 'GET'])
def info():
    form2 = request.form
    form2 = dict(form2)
    form2 = list(form2.values())
    result = str(check_fly(form2[0], form2[1] , cities , data_flies['fly']))
    return render_template('info.html' , result=result)
if __name__ == '__main__':
    app.run()

