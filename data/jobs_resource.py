from flask import jsonify
from flask_login import current_user
from flask_restful import Resource, abort

from . import db_session
from .job_regparser import parser
from .jobs import Jobs


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'job': job.to_dict(
            only=('team_leader', 'creater', 'job', 'work_size', 'collaborators', 'start_date', 'end_date',
                  'is_finished'))})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'job': [item.to_dict(
            only=('id', 'team_leader', 'creater', 'job', 'work_size', 'collaborators', 'start_date', 'end_date',
                  'is_finished')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        job = Jobs(
            team_leader=args['team_leader'],
            creater=args['creater'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=args['start_date'],
            end_date=args['end_date'],
            is_finished=args['is_finished']
        )
        db_sess.add(job)
        db_sess.commit()
        return jsonify({'id': job.id})
