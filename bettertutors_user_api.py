from bottle import Bottle, response, request

from peewee import DatabaseError

from bettertutors_sql_models.models.Signup import Signup
from bettertutors_sql_models.utils import create_tables

create_tables([Signup])
user_app = Bottle(catchall=False, autojson=True)


@user_app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'


@user_app.route('/api/user/signup', method=['POST'])  # Not register, so not POST /api/user
def signup():
    valid_keys = [u'email', u'institute', u'role']
    if not request.json:
        response.status = 400
        return {'error': 'ValidationError',
                'error_message': 'Invalid input'}
    elif valid_keys != sorted(request.json.keys()):
        response.status = 400
        return {'error': 'ValidationError',
                'error_message': 'Invalid input, wanted: {}'.format(
                    ', '.join(tuple(e for e in valid_keys if e not in request.json.keys()))
                )}
    try:
        return {'created': Signup.create(**request.json)}
    except AssertionError as e:  # TODO: errno.h equivalent
        response.status = 400
        return {'error': 'ValidationError',
                'error_message': e.message}
    except DatabaseError as e:  # TODO: Handle each DatabaseError in-turn, globally to api (on a single route)
        return {'error': (
            lambda err: err[err.find('.') + 1:])((lambda s: s[s.find("'"):s.rfind("'")])(
            (lambda error: str(error))(e.__class__))),
                'error_message': e.message}


if __name__ == '__main__':
    user_app.run(host='0.0.0.0', port=5555, debug=True)
