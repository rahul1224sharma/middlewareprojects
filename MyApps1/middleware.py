class ExecutionFlowMiddleware(object):
    def __init__(self,get_response):
        print("init() is executed only once..!!")
        self.get_response=get_response
    def __call__(self,request):
        print("pre processing")
        response=self.get_response(request)
        print("post processing")
        return response


from django.http import HttpResponse
class appmiddleware(object):
    def __init__(self,get_response):
        print("__init__ is called")
        self.get_response=get_response

    def __call__(self, request):
        return HttpResponse("<h1>Currently Application undermaitenance....</h1>")