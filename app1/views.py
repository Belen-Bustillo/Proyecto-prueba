from django.shortcuts import render

# Create your views here.
def index(requests):
    context = {"mensaje": "Prueba de app en Django"}
    return render(requests,"app1/index.html", context)