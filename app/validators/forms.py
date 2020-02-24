
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError
from app.libs.enums import ClientTypeEnum
from app.models.user import User


class ClientForm(Form):
     account = StringField(validators=[DataRequired(),length(min=5, max=32)])
     secret = StringField()
     type = IntegerField(validators=[DataRequired()])

     def validate_type(self, value):
         try:
             client = ClientTypeEnum(value.data)
         except ValueError as e:
             raise e
         self.type.data = client

class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='invalidate email')])
    secret = StringField(validators=[DataRequired(), Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$', message='密码格式不对')])
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])

    # 查询nickname是否重复
    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()



