from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import mainapp.models


#class ContactsView(TemplateView):
#    template_name = 'mainapp/contacts.html'

class IndexView(TemplateView):
    template_name = 'mainapp/index.html'

#class FirstContr(View):
#    def get(self, request, *args, **kwargs):
#        return HttpResponse("request")

def FirstContr(request):
    a = mainapp.models.my_parser('https://news.ycombinator.com/item?id=13713480')
    return HttpResponse(a.GetContent())

def PNF(request, exception):
    path = request.path
    qs = request.META['QUERY_STRING']
    a = mainapp.models.my_parser('https://news.ycombinator.com' + path+'?'+qs)

    return HttpResponse(a.GetContent())
