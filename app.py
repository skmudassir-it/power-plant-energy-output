from flask import Flask, redirect, render_template, request, url_for
import joblib
#import numpy as np
app = Flask(__name__)
solve = joblib.load('model')

@app.route('/', methods=['POST','GET'])
def home():
    eo = ''
    if request.method == 'POST' and 'temperature' in request.form and 'vacuum' in request.form and 'pressure' in request.form and 'humidity' in request.form:
        Temperature = float(request.form.get('temperature'))
        Vacuum = float(request.form.get('vacuum'))
        Pressure = float(request.form.get('pressure'))
        Humidity = float(request.form.get('humidity'))
        m = [[Temperature,Vacuum,Pressure,Humidity]]
        eo = solve.predict(m)
    return render_template('index.html',eo = eo)

if __name__ == '__main__':
    app.run(debug=True)
