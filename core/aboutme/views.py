from django.http import HttpResponse
from django.template import loader

def aboutme(request):
    template = loader.get_template("aboutme.html")
    return HttpResponse(template.render())