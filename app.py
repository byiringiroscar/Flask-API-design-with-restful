from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


todos = {
    'todo1': 'task1',
    'todo2': 'task2',
    'todo3': 'task3',
}

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}
    
    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple, '/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)