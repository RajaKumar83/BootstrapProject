from flask import Flask, render_template, request
import sqlite3
import json
# from werkzeug import secure_filename

app=Flask(__name__)

# open json file
f=open('config.json', 'r')

# load json file
params=json.load(f)['params']

@app.route('/')
def index():
    return render_template('index.html', params=params)

@app.route('/about')
def about():
    return render_template('about.html', params=params)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method=='POST':
        with sqlite3.connect("my_database.db") as con:
            # create a cursor
            c = con.cursor()
            n=request.form.get('name')
            e = request.form.get('email')
            p = request.form.get('phone')
            m = request.form.get('msg')
            # c.execute("INSERT INTO contacts (name, email, phone, msg) VALUES ('"+n+"','"+e+"',"+p+",'"+m+"')")
            c.execute("INSERT INTO contacts(name,email,phone,msg) VALUES(?, ?, ?, ?)", (n, e, p, m))
            con.commit()
            print('Command Executed Successfuly...')
    return render_template('contact.html', params=params)

@app.route('/post')
def post():
    return render_template('post.html', params=params)

if __name__ == '__main__':
    app.run(host ='127.0.0.1', port = 5000, debug = True)