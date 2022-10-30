from flask_restful import Resource


class FileResource(Resource):

    def get(self):
        print('qwe')
        return 'qwezxc', 200
