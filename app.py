from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pastebin.db'
db = SQLAlchemy(app)

class Paste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    pastes = Paste.query.all()
    return render_template('index.html', pastes=pastes)

@app.route('/paste', methods=['POST'])
def paste():
    content = request.form['content']
    new_paste = Paste(content=content)
    db.session.add(new_paste)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
