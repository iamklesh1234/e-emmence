from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)



@app.route('/',methods=['GET','POST'])
def home():
 return render_template('home.html')



@app.route('/home',methods=['GET','POST'])
def about():
    if request.method=='POST':
        # Handle PO
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)