from tastypie.resources import ModelResource, Resource
from tastypie.api import Api
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization, ReadOnlyAuthorization
from tastypie import fields
from django.contrib.auth.models import User
from ATTparser.models import ATT_user, Phone_Call
from analysis.summaries import get_lines, get_top_calls

v1_api = Api(api_name='v1')

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        authentication = BasicAuthentication()
        authorization = Authorization()
        fields = ['username', 'email']
        allowed_methods = ['get', 'post']
    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(username=request.user)
v1_api.register(UserResource())

class ATTUserResource(ModelResource):
    class Meta:
        queryset = ATT_user.objects.all()
        authorization = Authorization()
        authentication = BasicAuthentication()
        allowed_methods=['post']

    def obj_create(self, bundle, request=None, **kwargs):
        return super(ATTUserResource, self).obj_create(bundle, request, user=request.user)
v1_api.register(ATTUserResource())

class LinesObject(object):
    line=''

class PlanLinesResource(Resource):
    line = fields.CharField(attribute='line')
    #test = fields.CharField(attribute='atest')
    class Meta:
        object_class = LinesObject
        authorization = ReadOnlyAuthorization()
        authentication = BasicAuthentication()
        limit = 0
        include_resource_uri=False
        allowed_methods=['get']
        
    def detail_uri_kwargs(self, bundle_or_obj):
        return {}
    def get_object_list(self, request):
        all_lines = get_lines(user=request.user)
        results = []
        for line in all_lines:
            new_line = LinesObject()
            new_line.line = line
            results.append(new_line)
        return results

    def obj_get_list(self, request=None, **kwargs):
        return self.get_object_list(request)
    def obj_get(self, request=None, **kwargs):
        return self.get_object_list(request)
v1_api.register(PlanLinesResource())
    
class CallObject(object):
    number=''
    calls=0
    
class TopCallsResource(Resource):
    number=fields.CharField(attribute='number')
    calls=fields.IntegerField(attribute='calls')
    
    class Meta:
        object_class=CallObject
        authorization = ReadOnlyAuthorization()
        authentication = BasicAuthentication()
        limit=5
        allowed_methods=['get']
    def detail_uri_kwargs(self, bundle_or_obj):
        #TODO make this URL enabled, connect it to the detailed view
        return {}

    def get_object_list(self, request):
        calls=get_top_calls(user=request.user, billed_number=request.GET.get('line'))
        results=[]
        for caller in calls:
            caller_obj = CallObject()
            caller_obj.calls=caller['c']
            caller_obj.number=caller['other_number']
            results.append(caller_obj)
        return results
    def obj_get_list(self, request=None, **kwargs):
        return self.get_object_list(request)
    def obj_get(self, request=None, **kwargs):
        return self.get_object_list(request)
v1_api.register(TopCallsResource())




