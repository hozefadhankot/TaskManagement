from flask import request
from flask_restful import Resource
from models import Task
from schemas import TaskSchema
from bson.objectid import ObjectId

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

class TaskListResource(Resource):
    def get(self):
        """
        Get all tasks
        ---
        responses:
          200:
            description: A list of tasks
            schema:
              type: array
              items:
                $ref: '#/definitions/Task'
        """
        tasks = Task.get_all()
        for task in tasks:
            task['id'] = str(task['_id'])
            del task['_id']
        return tasks_schema.dump(tasks)

    def post(self):
        """
        Create a new task
        ---
        parameters:
          - in: body
            name: task
            schema:
              $ref: '#/definitions/Task'
        responses:
          201:
            description: The created task
            schema:
              $ref: '#/definitions/Task'
          400:
            description: Invalid input
        """
        data = request.get_json()
        errors = task_schema.validate(data)
        if errors:
            return errors, 400
        new_task = Task.create(data)
        data['id'] = str(new_task.inserted_id)
        return task_schema.dump(data), 201

class TaskResource(Resource):
    def get(self, task_id):
        """
        Get a task by ID
        ---
        parameters:
          - in: path
            name: task_id
            type: string
            required: true
        responses:
          200:
            description: The task
            schema:
              $ref: '#/definitions/Task'
          404:
            description: Task not found
        """
        task = Task.get(ObjectId(task_id))
        if not task:
            return {'message': 'Task not found'}, 404
        task['id'] = str(task['_id'])
        del task['_id']
        return task_schema.dump(task)

    def patch(self, task_id):
        """
        Update a task by ID
        ---
        parameters:
          - in: path
            name: task_id
            type: string
            required: true
          - in: body
            name: task
            schema:
              $ref: '#/definitions/Task'
        responses:
          200:
            description: The updated task
            schema:
              $ref: '#/definitions/Task'
          400:
            description: Invalid input
          404:
            description: Task not found
        """
        data = request.get_json()
        errors = task_schema.validate(data, partial=True)
        if errors:
            return errors, 400
        result = Task.update(ObjectId(task_id), data)
        if result.matched_count == 0:
            return {'message': 'Task not found'}, 404
        task = Task.get(ObjectId(task_id))
        task['id'] = str(task['_id'])
        del task['_id']
        return task_schema.dump(task)

    def delete(self, task_id):
        """
        Delete a task by ID
        ---
        parameters:
          - in: path
            name: task_id
            type: string
            required: true
        responses:
          204:
            description: Task deleted
          404:
            description: Task not found
        """
        result = Task.delete(ObjectId(task_id))
        if result.deleted_count == 0:
            return {'message': 'Task not found'}, 404
        return '', 204
