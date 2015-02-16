from bottle import Bottle, response, request

from bettertutors_sql_models.User import User

user_app = Bottle(catchall=False, autojson=True)

__version__ = '0.2.3'


@user_app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'


@user_app.route('/api/user/signup', method=['POST'])  # Not register, so not POST /api/user
def signup():
    if not request.json:
        response.status = 400
        return {'error': 'ValidationError', 'error_message': 'Invalid input'}
    elif [u'email', u'institute', u'role'] != sorted(request.json.keys()):
        response.status = 400
        return {'error': 'ValidationError', 'error_message': 'Invalid input'}
    return {'created': User.create(**request.json)}


if __name__ == '__main__':
    # run(app=oauth2_error_catcher, debug=True)
    user_app.run(host='0.0.0.0', port=5555, debug=True)
