import tensorflow as tf
from flask import Flask,url_for,redirect,Request,render_template,request


def main(a):
    model = tf.keras.models.load_model("S:/project/ml projects/project for upload/heart problem project/heart_problem")
    pred = model.predict(tf.expand_dims(a,axis=0))
    pred = int(tf.round(pred))
    return pred

    

app = Flask(__name__)

@app.route('/')
def walcome():
    return render_template('index.html')


@app.route('/output/<int:result>')
def output(result):
    if (result==0):
        results =  "Be carefull!\n You can get some heart problems in future."
    else:
        results = "Congratulations! \n You have less chanses to get any heart problem."
    return render_template('results.html',results=results)
    

@app.route('/submit',methods=['POST','GET'])
def submit():
    res =''
    if request.method=='POST':
        age = int(request.form['age'])
        sex =int(request.form['sex'])
        cp =int(request.form['cp'])
        trtbps = int(request.form['trtbps'])
        chal = int(request.form['chal'])
        fbs = int(request.form['fabs'])
        restecg = int(request.form['restecg'])
        thalachh = int(request.form['thalachh'])
        exng = int(request.form['exng'])
        oldpeak = float(request.form['oldpeak'])
        slp = int(request.form['slp'])
        cao = int(request.form['cao'])
        thall = int(request.form['thall'])

        list = [age,sex,cp,trtbps,chal,fbs,restecg,thalachh,exng,oldpeak,slp,cao,thall]
        res = main(list)

    return redirect(url_for('output',result = res))





app.run(debug=True)