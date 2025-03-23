import datetime

from flask import Flask, render_template, redirect, abort, request
from flask_login import login_user, LoginManager, login_required, logout_user, current_user

from data import db_session
from data import jobs_api
from data.jobs import Jobs
from data.users import User
from forms.job import RegisterJob
from forms.user import LoginForm, RegisterForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def users():
    db_sess = db_session.create_session()
    lst = [i.id for i in db_sess.query(User).filter(User.position == 'captain')]
    return render_template('index.html', jobs=db_sess.query(Jobs), colonists=db_sess.query(User), captains=lst)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/job', methods=['GET', 'POST'])
def add_job():
    form = RegisterJob()
    if form.submit.data:
        db_sess = db_session.create_session()
        jobs = Jobs()
        jobs.job = form.title.data
        jobs.team_leader = form.team_leader.data
        jobs.work_size = form.work_size.data
        jobs.collaborators = form.collaborators.data
        jobs.creater = str(current_user)
        db_sess.add(jobs)
        db_sess.commit()
        return redirect('/')
    return render_template('job.html', title='Adding a job', form=form)


@app.route('/job/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = RegisterJob()
    if request.method == "GET":  # получить выбранную работу
        db_sess = db_session.create_session()
        lst = [i.id for i in db_sess.query(User).filter(User.position == 'captain')]
        job = [j for j in db_sess.query(Jobs) if
               j.id == id and (j.team_leader == current_user.id or current_user.id in lst)]
        if job:
            job = job[0]
            form.title.data = job.job
            form.team_leader.data = job.team_leader
            form.work_size.data = job.work_size
            form.collaborators.data = job.collaborators
        else:
            abort(404)

    if form.submit.data:  # при изменении
        db_sess = db_session.create_session()
        lst = [i.id for i in db_sess.query(User).filter(User.position == 'captain')]
        job = [j for j in db_sess.query(Jobs) if
               j.id == id and (j.team_leader == current_user.id or current_user.id in lst)]
        if job:
            job = job[0]
            job.job = form.title.data
            job.team_leader = form.team_leader.data
            job.work_size = form.work_size.data
            job.collaborators = form.collaborators.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('job.html', title='Редактирование работы', form=form)


@app.route('/job_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    lst = [i.id for i in db_sess.query(User).filter(User.position == 'captain')]
    job = [j for j in db_sess.query(Jobs) if
           j.id == id and (j.team_leader == current_user.id or current_user.id in lst)]
    if job:
        job = job[0]
        db_sess.delete(job)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


def main():
    db_session.global_init('db/mars_explorer.sqlite')
    app.register_blueprint(jobs_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()
