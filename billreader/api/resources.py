from tastypie.resources import ModelResource
from tastypie.api import Api
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from django.contrib.auth.models import User
from ATTparser.models import ATT_user

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        authentication = BasicAuthentication()
        authorization = Authorization()
        fields = ['username', 'email']
        allowed_methods = ['get', 'post']
    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(username=request.user)
        
class ATTUserResource(ModelResource):
    class Meta:
        queryset = ATT_user.objects.all()
        authorization = Authorization()
        authentication = BasicAuthentication()

    def obj_create(self, bundle, request=None, **kwargs):
        return super(ATTUserResource, self).obj_create(bundle, request, user=request.user)

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(ATTUserResource())