from piston.handler import BaseHandler

class testHandler( BaseHandler ):
    def read(self, request, expression ):
        return 'Result: '+str(eval( expression ))