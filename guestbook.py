from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/bukutamu'
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
    comment_to_update = Comments.query.get_or_404(id)
    return render_template('update.html', comment=comment_to_update)

@app.route('/update_process/<int:id>', methods=['POST'])
def update_process(id):
    comment_to_update = Comments.query.get_or_404(id)
    
    comment_to_update.name = request.form['name']
    comment_to_update.comment = request.form['comment']
    
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
