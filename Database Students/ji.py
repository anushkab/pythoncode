#made by Anushka Bhandari :')
#used SQLAlchemy Flask Django Python

from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.ULOO'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(60))
   email = db.Column(db.String(50))
   section = db.Column(db.String(2))
   Group = db.Column(db.String(2))

   def __init__(self, name, email, section,Group):
      self.name = name
      self.email = email
      self.section = section
      self.Group = Group


@app.route('/')
def show_all():
   return render_template('show_all.html', students = students.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['email'] or not request.form['section']:
         flash('Please enter all the fields', 'error')
      else:
         student = students(request.form['name'], request.form['email'],
            request.form['section'], request.form['Group'])

         db.session.add(student)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug=True,port=5004,host="0.0.0.0")
   # create a new server
   #external server provided in free by IIITD yayayayayayaya! :D
