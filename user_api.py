from bottle import Bottle, response, request

from bettertutors_sql_models.User import User

user_app = Bottle(catchall=False, autojson=True)

__version__ = '0.1.0'


@user_app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'


@user_app.route('/api/user/signup')  # Not register, so not POST /api/user
def signup():
    if ['email', 'institute', 'role'] != request.body().keys():
        response.status = 400
        return {'error': 'ValidationError', 'error_message': 'Invalid input'}
    return {'created': User.create(**request.body())}


if __name__ == '__main__':
    # run(app=oauth2_error_catcher, debug=True)
    user_app.run(host='0.0.0.0', port=5555, debug=True)
