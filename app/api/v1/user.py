from app.libs.redprint import RedPrint

api = RedPrint('user')

@api.route('/get')
def user():
    print('this is user')
    return 'this is user'
