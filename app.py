from flask import Flask, render_template, request
from calculator import *
import pandas as pd
import webbrowser as wb
# from flaskwebgui import FlaskUI

# from flask_socketio import SocketIO
app=Flask(__name__)
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# ui = FlaskUI(app, width=500, height=500) 
def get_output(p, r, t, abc, m, n, output_type):
    m = float(m)
    if abc=="m":
        con=m
    if abc=="y":
        con=m/12
    answer = ci(p, n, r, t, con)
    principle = answer['Principle']
    roi = answer['Rate of interest']
    amount_invested = answer['Total amount invested']
    amount_got = answer['Total amount received']
    interest = answer['Compound interest']
    profit = answer['All over profit']
    # output = f"Principle Amount: {principle}\n Rate of interest: {roi}\nTotal amount invested = {amount_invested}\nTotal return = {amount_got}\nCompound interest = {interest}\nAll oveer profit = {profit}"
    if output_type=="listr":
        output = [f"Principle Amount: {principle}",
                  f"Rate of interest: {roi}",
                  f"Total amount invested = {amount_invested}",
                  f"Total return = {amount_got}",
                  f"Compound interest = {interest}",
                  f"All over profit = {profit}"]
    elif output_type == "dictr":
        output = answer
    return output
    
    

@app.route("/", methods=['GET', 'POST'])
def first_page():
    if request.method == 'POST':
        p =request.form['p']
        r = request.form['r']
        t =request.form['t']
        abc =request.form['abc']
        m =request.form['m']
        n =request.form['xyz']
        p = float(p)
        r = float(r)
        t = float(t)
        m = float(m)
        n = float(n)
        
        data_list = get_output(p, r, t, abc, m, n, "listr")
        
        return render_template('index.html', output=data_list, flash_message="True")
        
    return render_template('index.html', flash_message="False")
# get_output(p, r, t, abc, m, n)
# /p-'m/y'-m-y-r-'y/h/q/m/d'
@app.route("/api/<string:stringgg>/")
def api(stringgg):
    string_list = stringgg.split('-')
    if len(string_list) == 6:
        pass
    else:
        return "Error found enter the api properly\n Example:- <initial investment>-<m for monthly contributuon and y for yearly contribution>-<contributuon amount>-<length of time in years>-<rate of interest>-<y/h/q/m/d for compound frequency>" 
    p = float(string_list[0])
    r = float(string_list[4])
    t = float(string_list[3])
    abc = string_list[1]
    m = float(string_list[2])
    n_index =string_list[5]
    if n_index == "y":
        output = get_output(p, r, t, abc, m, 1, "dictr")
    elif n_index == "h":
        output = get_output(p, r, t, abc, m, 2, "dictr")
    elif n_index == "q":
        output = get_output(p, r, t, abc, m, 4, "dictr")
    elif n_index == "m":
        output = get_output(p, r, t, abc, m, 12, "dictr")
    elif n_index == "d":
        output = get_output(p, r, t, abc, m, 365, "dictr")    
    return output
    
    

# answer = ci(10000, 1, 10, 10, 1000)

# print(answer)

if __name__ == '__main__':
    
    wb.open_new('http://localhost:9999')
    app.run(port = "9999")
    # ui.run()
    # FlaskUI(app, socketio=socketio, start_server="flask-socketio").run()