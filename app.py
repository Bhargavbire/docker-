#from flask import Flask, render_template
#app = Flask(__name__)
 
#@app.route('/evalution/<int:score>')
#def evalution(score):
    #return render_template('evalution.html', marks = score)
 
#if __name__  =='__main__':  
    #app.run(debug = True)




from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('index.html')
 
if __name__  =='__main__':  
    app.run(debug = True)    