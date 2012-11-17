from tastypie.resources import ModelResource, Resource
from tastypie.api import Api
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization, ReadOnlyAuthorization
from tastypie import fields
from django.contrib.auth.models import User
from ATTparser.models import ATT_user, Phone_Call
from analysis.summaries import get_lines

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

        return results
    def obj_get_list(self, request=None, **kwargs):
        return self.get_object_list(request)
    def obj_get(self, request=None, **kwargs):
        return self.get_object_list(request)
v1_api.register(PlanLinesResource())
    


class LinesResource(ModelResource):
    #user = fields.ForeignKey(UserResource, 'billed_user')
    astring='a string!'
    nums=set()
    
    class Meta:
        queryset = Phone_Call.objects.all()
        authorization = Authorization()
        authentication = BasicAuthentication()
        fields=['billed_number']#['billed_number','other_number']
        include_resource_uri=False
        limit=0
    
    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(billed_user=request.user)#.values('billed_number').distinct()
    #def get_object_list(self, request):
    #    return super(PlanLinesResource, self).get_object_list(request).#filter(billed_number__exact='7039993230')
    
    def dehydrate_billed_number(self, bundle):
        self.nums.add(bundle.data['billed_number'])
        #return bundle.data['billed_number']
    

    def dehydrate(self, bundle):
        bundle.data={'mynums':tuple(self.nums)};
        self.numbers=self.nums
        return bundle
v1_api.register(LinesResource())
        






