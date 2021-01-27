from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Grocery(db.Model):
    """Класс описывает таблицу в БД"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        """Когда происходит запрос, БД возвращает имя объекта из таблицы"""
        return f'<Grocery {self.name}>'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
