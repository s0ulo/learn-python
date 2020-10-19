# Миграции баз данных

## Прежде чем мы начнем

Перед тем, как перейти к теме миграций, давайте упростим себе запуск Flask. Сейчас для запуска нам приходится использовать длинную команду:

```sh
Linux и Mac: export FLASK_APP=webapp && export FLASK_ENV=development && flask run
```

```sh
Windows: set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
```

## Скрипты для запуска

Самый простой способ решения проблемы - сделать скрипт для запуска. В Windows это будет `.bat`-файл в Linux и MacOs - `.sh`-файл

### Скрипт для Windows

В корне проекта создайте файл `run.bat` (название перед точкой может быть любое). В файл добавьте одну строку:

```sh
set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
```

Это все. Теперь для запуска проекта нужно просто написать в консоли `run.bat`

### Скрипт для Linux и MacOs

В корне проекта создайте файл `run.sh`:

```sh
#!/bin/sh
export FLASK_APP=webapp && export FLASK_ENV=development && flask run
```

Сохраните файл и в корне проекта выполните в консоли команду `chmod +x run.sh` - это сделает файл исполняемым. Теперь для запуска проекта нужно писать `./run.sh`. Косая черточка и точка означает для операционной системы "файл из текущей папки". Если не написать `./` перед именем файла, вы получите ошибку `run.sh: command not found`

## Что такое миграции?

Когда мы вносим изменения в наши модели (например, добавляем в модель `User` поле `email`) - эти изменения не появятся в базе данных сами собой. Если мы добавим колонку и попробуем обратиться к модели `User`, мы получим ошибку: `sqlalchemy.exc.OperationalError: no such column: user.email`

Миграции - это python-скрипты, которые вносят изменения в нашу базу данных автоматически.

## Flask-Migrate

[Пакет Flask-Migrate](https://github.com/miguelgrinberg/flask-migrate) позволяет отслеживать изменения в моделях и генерировать скрипты миграций автоматически. Пакет построен на базе [Alembic](https://alembic.sqlalchemy.org/en/latest/) - системы миграций для SQLAlchemy. Если вы работаете с БД через SQLAlchemy, но ваш проект не на Flask - используйте для миграций Alembic.

```sh
pip install flask-migrate
```

Не забудьте добавить новую зависимость в requirements.txt

## Включим поддержку миграций

Добавим соответствующий код в `__init__.py`:

```py
from flask_migrate import Migrate
...
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
   migrate = Migrate(app, db)

```

## Поправим конфигурацию

Сейчас при старте проекта SQLAlchemy выдает в консоль сообщение `FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead`. Добавим в `config.py` строку `SQLALCHEMY_TRACK_MODIFICATIONS = False`. Это отключит функционал отправки сигнала приложению при изменениях в БД - мы не будем пользоваться им, т.к. он создает большую дополнительную нагрузку на приложение.

## Инициализируем механизм миграций

Для работы Flask-Migrate нужно создать несколько файлов и папок. К счастью, этот процесс автоматизирован, нам нужно выполнить команду:

```sh
Linux и Mac: export FLASK_APP=webapp && flask db init
```

```sh
Windows: set FLASK_APP=webapp && flask db init
```

В корне проекта должна появиться папка `migrations`

## Создадим первую миграцию

У нас уже создана база данных, поэтому чтобы посмотреть как работают миграции, давайте сначала переименуем нашу базу данных `webapp.db`:

- Linux и Mac:

  ```sh
  mv webapp.db webapp.db.old
  ```

- Windows:
  ```py
  move webapp.db webapp.db.old
  ```

## Создадим первую миграцию

- Linux и Mac:

  ```sh
  export FLASK_APP=webapp && flask db migrate -m "users and news tables"
  ```

- Windows:

  ```sh
  set FLASK_APP=webapp && flask db migrate -m "users and news tables"
  ```

Теперь в `migrations/versions/` у нас появился первый файл вида `84cccf62ee91_users_and_news_tables.py`, внутри в секции `upgrade()` написан код для создания таблиц.
В секции `downgrade()` прописано удаление таблиц. Это означает, что миграции можно как применять, так и отменять.

## Применим миграцию

Миграция применяется командой `flask db upgrade`, и если мы выполним ее, то у нас появится новый файл `webapp.db`. Там будет правильная структура, но не будет данных. Теперь нам не нужен файл `create_db.py` - давайте удалим его.

## Миграции и существующие таблицы

Как вы помните, у нас уже есть база со структурой и данными (давайте вернем ее при помощи mv/move). Если мы попробуем выполнить миграцию на ней, то получим ошибку "Table already exists". Чтобы работать с миграциями на существующей базе, нам нужно пометить нашу миграцию как выполненную командой `flask db stamp 84cccf62ee91` (у вас номер миграции будет другой).
Если мы теперь заглянем в базу, то увидим что там появилась новая таблица `alembic_version`, в которой сохраняются данные о выполненных миграциях.

## Добавим новое поле в модель User

Для того, чтобы добавить на сайт регистрацию, нам понадобится поле `email` в модели `User`:

```py
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    email = db.Column(db.String(50))

```

## Создадим миграцию и выполним ее

```sh
flask db migrate -m "added email to user"

flask db upgrade
```

Зайдем в базу данных и проверим, что в таблице `user` появилось новое поле.

## Создадим форму для регистрации

Форма регистрации будет немного похожа на форму логина, но мы добавим пару дополнительных полей:

```py
class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    email = StringField('Email', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})
```

## Добавим пару стандартных валидаторов

Мы уже использовали валидатор `DataRequired`, который проверял, что поле не пустое. Добавим валидаторы `Email` и `EqualTo` - они проверяют, что в поле введен email и что значение одного поля идентично значению другого:

```py
from wtforms.validators import DataRequired, Email, EqualTo

...

email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})

```

## Добавим шаблон

Скопируем файл `templates/user/login.html` как `templates/user/registration.html` и поменяем форму под наши поля.

## Страница регистрации

Мы сделали форму и шаблон, но чтобы все заработало, нужно добавить соответствующие `route`-ы и функции-обработчики. Первая функция будет просто показывать форму регистрации:

```py
from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm
```

## Страница регистрации

```py
@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    form = RegistrationForm()
    title = "Регистрация"
    return render_template('user/registration.html', page_title=title, form=form)
```

## Обработчик регистрации

```py
@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('user.register'))
```

## Дополнительные проверки

Если пользователь при регистрации укажет имя, которое уже есть в системе, то мы получим ошибку базы данных. Добавим собственные валидаторы для полей формы. Валидатор - это просто метод класса формы, имя которого строится как `validate_ПОЛЕ`, например `validate_email`. В случае ошибки валидатор должен выкидывать исключение `wtforms.validators.ValidationError`

```py
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from webapp.user.models import User
```

## Дополнительные проверки

```py
class RegistrationForm(FlaskForm):
...
    def validate_username(self, username):
        users_count = User.query.filter_by(username=username.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с таким именем уже зарегистрирован')

    def validate_email(self, email):
        users_count = User.query.filter_by(email=email.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с такой электронной почтой уже зарегистрирован')
```

## Вывод ошибок в шаблоне

Будем передавать ошибки в форме при помощи `flash`

```py
def process_reg():
    ...
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('user.register'))

```

## Удобный просмотр ошибок

Поднимем блок вывод ошибок над `<div class="row"\>` и будем выводить каждую ошибку отдельной строкой:

```{.html}
{% with messages = get_flashed_messages() %}
    {% if messages %}
        {% for message in messages %}
        <div class="alert alert-danger" role="alert">
            {{ message }}
        </div>
        {% endfor %}
    {% endif %}
{% endwith %}
```

## Работа с пользователем в шаблоне

Flask-Login дает нам возможность обращаться к `current_user` в шаблоне:

```{.html}
{% if current_user.is_authenticated %}
    <a class="nav-link" href="{{ url_for('user.logout') }}">Выйти</a>
{% else %}
    <a class="nav-link" href="{{ url_for('user.login') }}">Войти</a>
{% endif %}

```

## Перенесем блок логина вправо

Для этого просто создадим новый блок `navbar-nav` после формы поиска:

```{.html}
<ul class="navbar-nav">
{% if current_user.is_authenticated %}
    <a class="nav-link" href="{{ url_for('user.logout') }}">Выйти</a>
{% else %}
    <a class="nav-link" href="{{ url_for('user.login') }}">Войти</a>
{% endif %}
</ul>

```

## Добавим дополнительные возможности

```{.html}
<ul class="navbar-nav">
{% if current_user.is_authenticated %}
    <li class="nav-item">
        <span class="nav-link">Привет, {{ current_user.username }}!</span>
    </li>
    {% if current_user.is_admin %}
    <li class="nav-item">
        <a href="{{ url_for('admin.admin_index') }}" class="nav-link">Админка</a>
    </li>
    {% endif %}
    <li class="nav-item">
        <a class="nav-link" href="{{ url_for('user.logout') }}">Выйти</a>
    </li>
{% else %}
    <li class="nav-item">
        <a class="nav-link" href="{{ url_for('user.login') }}">Войти</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="{{ url_for('user.register') }}">Регистрация</a>
    </li>
{% endif %}
</ul>

```

## Включим поддержку миграций

Добавим соответствующий код в `__init__.py`:

```py
from flask_migrate import Migrate
...
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
   migrate = Migrate(app, db)

```
