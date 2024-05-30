from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthdata.db'

db = SQLAlchemy(app)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    medical_record = db.Column(db.Text, nullable=True)

@app.route('/')
def index():
    patients = Patient.query.all()
    return render_template('index.html', patients=patients)

@app.route('/add_patient', methods=['POST'])
def add_patient():
    name = request.form.get('name')
    medical_record = request.form.get('medical_record')
    
    new_patient = Patient(name=name, medical_record=medical_record)
    db.session.add(new_patient)
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
