from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('myForm.html')
@app.route('/submit',methods=['POST'])
def submit():
    uname=request.form['uname']
    return render_template('greetings.html',name=uname)
app.run(debug=True)