from flask import Flask , render_template , request
import pandas as pd
data = pd.read_csv('data.csv')
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
@app.route("/account" , methods=['GET' , 'POST'])
def account():
    global data
    form = request.form
    form = dict(form)
    form = list(form.values())
    first_name = [str(i) for i in data['first name']]
    last_name = [str(i) for i in data['first name']]
    phone_number = [str(i) for i in data['phone number']]
    username = [str(i) for i in data['username']]
    password = [str(i) for i in data['password']]
    if len(form) == 2:
        if form[0] in username and form[1] in password and username.index(form[0]) == password.index(form[1]):
            return render_template("account.html" , name = first_name[username.index(form[0])])
        else:
            return redirect(url_for('login'))
    elif len(form) == 6:
        if form[3] not in username and form[2] not in phone_number and form[-1]==form[-2] and form[-2] not in password:
            new_data = pd.DataFrame({'first name' : [form[0]] , 'last name' : [form[1]] , 'phone number' : [form[2]] , 'username' : [form[3]] , 'password' :  [form[4]]})
            new_data.to_csv('data.csv' , mode='a' , header=False , index=False)
            data = pd.read_csv(data.csv)

            return render_template('account.html' , name=form[0])
        else:
            return redirect(url_for('signin') ,)
    else:
        return 'error' 
if __name__ == '__main__':
    app.run()
if False:
    cities = ['a' , 'b' , 'c' , 'd' , 'e' , 'f']
    flies = ['a->b' , 'b->c' , 'c->d' , 'd->e' , 'e->f']
    def check_fly(mabda , maghsad , city , fly):
        mabdaha = [i[0] for i in flies]
        maghsadha = [i[-1] for i in flies]
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
                return 'ma hamchin parvazi nadarim'
        elif mabda not in mabdaha:
            return 'ma hamchin parvazi nadarim'
    check_fly('a' , 'd' , cities , flies)