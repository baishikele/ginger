from app.libs.redprint import RedPrint
from flask import request
from app.validators.forms import ClientForm
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


def __register_user_by_email():
    pass