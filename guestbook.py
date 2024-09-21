from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.vevjsqcqtpmczexwneck:databasesaya123#@aws-0-us-east-1.pooler.supabase.com:6543/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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

@app.route('/delete/<int:id>')
def delete(id):
    comment_to_delete = Comments.query.get_or_404(id)
    db.session.delete(comment_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>')
def update(id):
    Komentar = Comments.query.get_or_404(id)
    return render_template('update.html', comment=Komentar)

@app.route('/update_process/<int:id>', methods=['POST'])
def update_process(id):
    Komentar = Comments.query.get_or_404(id)
    Komentar.name = request.form['name']
    Komentar.comment = request.form['comment']
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
