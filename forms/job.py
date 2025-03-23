import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, FieldList
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired


class RegisterJob(FlaskForm):
    title = StringField('Название работы', validators=[DataRequired()])
    team_leader = StringField('Руководитель работы', validators=[DataRequired()])
    work_size = IntegerField('Размер работы', validators=[DataRequired()])
    collaborators = StringField('Помощники', validators=[DataRequired()])
    start_date = StringField('Дата создания', default=str(datetime.date.today()))
    end_date = StringField('Дата срока', validators=[DataRequired()])
    about_job = TextAreaField("О работе")
    is_finished = BooleanField('Завершена ли работа', default=False)
    submit = SubmitField('Add')