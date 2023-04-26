import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///ToDoWeb.db'
app.config['SQLALCHEMY_TRACK_MODIFICAIONS'] = False
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Quest_name = db.Column(db.String(200), nullable=False)
    Desc_of_Quest = db.Column(db.String(600), nullable=False)
    Date_created = db.Column(db.DateTime, default=datetime)
    # Main_Quest = db.Column(db.String(200), nullable=False)
    
    def __repr__(self) -> str:
        return f'{self.sno} - {self.Quest_name} - {self.Desc_of_Quest}'

@app.route('/')
def index():
    todo = Todo(title='First todo', desc='compleate backend')
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')

@app.route('/show')
def product():
    alltodo = todo.quary.all()
    print(alltodo)
    return 'this page'

if __name__== "__main__":
    app.run(debug=True) 