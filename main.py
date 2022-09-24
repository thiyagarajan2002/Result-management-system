from flask import Flask, render_template,url_for,request,redirect
import getresult as gr
import datetime
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def Home():
  return render_template('home.html',status='Activate')

@app.route("/result", methods=['POST','GET'])
def result():
  if request.method == 'POST':
    register_number = (request.form['regno1'])
    date_of_birth = (request.form['dob1'])
    year = str((request.form['Year']))
    get_result=gr.getresult(register_number,date_of_birth,year)
    get_column=gr.getcolumn(year)
    if get_result!=[]:
      lenght1=len(get_result)
      return render_template('result.html',ls1=get_column,ls2=get_result,lenght1=lenght1)
    else:
      return render_template('home.html',status='Invalid Data')

  
if __name__ == '__main__':
    app.run(debug=True)
