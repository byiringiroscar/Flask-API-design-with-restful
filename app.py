from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
from flasgger import Swagger, swag_from
from config.swagger import template, swagger_config


app = Flask(__name__)
SWAGGER={
                'title': "Bookmarks API",
                'uiversion': 3
            }



api = Api(app)
Swagger(app, config=swagger_config, template=template)


TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

class HelloWorld(Resource):
    def get(self):
        """
        This examples uses FlaskRESTful Resource
        It works also with swag_from, schemas and spec_dict
        ---
        responses:
          200:
            description: User all

          401:
             description: Fails to get items due to authentication error
          
        """
        return TODOS


class TodoSimple(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]
    
    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201
    
    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple, '/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)