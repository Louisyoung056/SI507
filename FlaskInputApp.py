from v1 import getPrepath, Courseoffered, Coursename, Coursedescription, Courseprerequisite, Coursesuccessor

#FlaskInputApp.py
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('FlaskInputs2.html') # just the static HTML
    
@app.route('/handle_form', methods=['POST'])
def handle_the_form():
    eecs_number = request.form["number"]
    eecs_term = request.form["term"]
    return render_template('response.html', 
        term = eecs_term,
        number=eecs_number,
        offered = Courseoffered(int(eecs_number)),
        path = getPrepath(int(eecs_number)),
        Name = Coursename(int(eecs_number)),
        Description = Coursedescription(int(eecs_number)),
        Prerequisite = Courseprerequisite(int(eecs_number)),
        suc = Coursesuccessor(int(eecs_number))
        )
    
if __name__ == "__main__":
    app.run(debug=True) 

