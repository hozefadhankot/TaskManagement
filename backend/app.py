from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flasgger import Swagger
from config import Config
from resources import TaskListResource, TaskResource

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
api = Api(app)

swagger = Swagger(app)

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<task_id>')

if __name__ == '__main__':
    app.run(debug=True)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/",
    "definitions": {
        "Task": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "description": "The unique identifier of the task"
                },
                "title": {
                    "type": "string",
                    "description": "The title of the task"
                },
                "description": {
                    "type": "string",
                    "description": "The description of the task"
                },
                "status": {
                    "type": "string",
                    "description": "The status of the task"
                }
            }
        }
    }
}

swagger = Swagger(app, config=swagger_config)
