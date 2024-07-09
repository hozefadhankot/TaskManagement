from marshmallow import Schema, fields

class TaskSchema(Schema):
    id = fields.String(description='The unique identifier of the task')
    title = fields.String(description='The title of the task', required=True)
    description = fields.String(description='The description of the task')
    status = fields.String(description='The status of the task')
