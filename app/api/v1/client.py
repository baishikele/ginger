from app.libs.redprint import RedPrint
from flask import request

from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm
from app.libs.enums import ClientTypeEnum

api = RedPrint('client')

@api.route('/register', methods=['POST'])
def create_client():
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        # 模拟switch条件判断
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email
        }
        promise[form.type.data]()
    return 'success'

def __register_user_by_email():
    data = request.json
    form = UserEmailForm(data=data)
    if form.validate():
        User.register_by_email(nickname=form.nickname.data,
                               account=form.account.data,
                               secret=form.secret.data)
    else:
        print('no ok')
