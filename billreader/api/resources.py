from tastypie.resources import ModelResource
from tastypie.api import Api
from tastypie.authorization import Authorization
from django.contrib.auth.models import User
from ATTparser.models import ATT_user

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        authorization = Authorization()
        fields = ['username', 'password', 'email']
        allowed_methods = ['get', 'post']
        
class ATTUserResource(ModelResource):
    class Meta:
        queryset = ATT_user.objects.all()
        authorization = Authorization()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(ATTUserResource())