from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Grocery(db.Model):
    """Класс описывает таблицу в БД"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        """Когда происходит запрос, БД возвращает имя объекта из таблицы"""
        return self.name


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  # если форму заполнили и нажали "отправить"
        name = request.form['name']  # из поля name формы записываем данные в переменную name
        new_item = Grocery(name=name)  # создаем новый элемент в БД

        try:  # попробовать 🐋💨🌊
            db.session.add(new_item)  # добавить новую запись в БД 🐋💨🌊
            db.session.commit()  # применить изменения 🐋💨🌊
            return redirect('/')  # в случае успеха вернуть пользователя на главную страницу 🐋💨🌊
        except:  # в случае возникновения ошибки 🐋💨🌊
            return 'There was a problem adding new item!'
    else:
        groceries = Grocery.query.order_by(Grocery.added).all()
        return render_template('index.html', groceries=groceries)


if __name__ == '__main__':
    app.run(debug=True)
