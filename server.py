from flask import Flask, request
from logify import Logify
import simplejson as json
from flask.ext import restful

app = Flask(__name__)

api = restful.Api(app)

parser = reqparse.RequestParser()
parser.add_argument('log', type=str)

class Log(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

class LogList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = 'todo%d' % (len(TODOS) + 1)
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

api.add_resource(LogList, '/logs')
api.add_resource(Log, '/log/<string:log_id>')

# @app.route('/log', methods=['POST'])
# def log():
#     projectname = request.form['projectname']
#     type = request.form['type']
#     message = request.form['message']
#     logify = Logify(projectname)
#     log = logify.log(type, message)
#     return json.dump({"status": "ok"})


if __name__ == '__main__':
    app.run()
