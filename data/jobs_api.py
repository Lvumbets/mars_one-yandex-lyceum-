import flask
from flask import jsonify, make_response, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_news():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [job.to_dict(only=(
                    "id", 'team_leader', 'creater', 'job', 'work_size', 'collaborators', 'start_date', 'end_date',
                    'is_finished'))
                    for job in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return make_response(jsonify({'error': 'Not found'}), 404)
    elif not all(key in request.json for key in
                 ["id", 'team_leader', 'creater', 'job', 'work_size', 'collaborators', 'start_date', 'end_date',
                  'is_finished']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    return jsonify(
        {
            'job': job.to_dict(only=(
                "id", 'team_leader', 'creater', 'job', 'work_size', 'collaborators', 'start_date', 'end_date',
                'is_finished'))
        }
    )
