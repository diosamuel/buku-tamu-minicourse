from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# instanciating the app using the module name
app = Flask(__name__)

# configuring the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql7320377:DBbYrSp2Y5@sql7.freemysqlhosting.net:3306/sql7320377'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# each class in python will be mapped to a table in the db


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))


@app.route('/')
def index():
    result = Comments.query.all()
    return render_template('index.html', result=result)


@app.route('/sign')
def sign():
    return render_template('sign.html')


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']

    signature = Comments(name=name, comment=comment)
    db.session.add(signature)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
