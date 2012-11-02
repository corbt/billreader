from handlers import testHandler
from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import testHandler

class CsrfExemptResource( Resource ):
    def __init__( self, handler, authentication = None ):
        super( CsrfExemptResource, self ).__init__( handler, authentication )
        self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )
        
eval_resource = Resource( testHandler )

urlpatterns = patterns( '',
    url( r'^(?P<expression>.*)$', eval_resource )
)