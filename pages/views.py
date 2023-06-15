from django.http import HttpResponse
def homePageView(request):
    return HttpResponse('welcome to django')
