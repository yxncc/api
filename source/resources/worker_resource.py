from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from ..extensions import db
from ..models import Worker
from ..schemas import WorkerSchema


class WorkerListResource(Resource):
    def get(self):
        worker_list = Worker.query.order_by(Worker.id)
        response = WorkerSchema().dump(worker_list, many=True)
        return response, 200

    def post(self):
        try:
            new_worker = WorkerSchema().load(request.json)
        except ValidationError as e:
            return {'errors': e.normalized_messages()}, 400

        db.session.add(new_worker)
        db.session.commit()

        new_worker = Worker.query.get(new_worker.id)
        response = WorkerSchema().dump(new_worker)
        return response, 200


class WorkerDetailResource(Resource):
    def get(self, worker_id):
        worker = Worker.query.get(worker_id)
        response = WorkerSchema().dump(worker)
        return response, 200

    def put(self, worker_id):
        try:
            data = WorkerSchema().load(request.json)
        except ValidationError as e:
            return {'errors': e.normalized_messages()}, 400

        worker = Worker.query.get(worker_id)
        if worker is None:
            return {'message': "Worker with given id not found"}, 404

        worker.update(data)
        db.session.commit()

        response = WorkerSchema().dump(Worker.query.get(worker_id))
        return response, 200

    def delete(self, worker_id):
        worker = Worker.query.get(worker_id)
        db.session.delete(worker)
        db.session.commit()

        return {'message': 'Worker deleted successfully'}, 200
