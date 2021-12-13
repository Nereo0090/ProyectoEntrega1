from django.http import HttpResponse
from datetime import datetime, date        #importo datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Django - Coder")


def segundaVista(request):

    return HttpResponse("<br><br>--------YA SOMOS PROGRAMADORES-----------")


def dia(request):

    variable = datetime.now()
    

    return HttpResponse(f"hoy es un gran dia<br>{variable}")


def apellido(request, ape):

    fecha = datetime.now()
    
    return HttpResponse(f"El alumno de coder {ape}, es muy bueno..<br><br>.. Por lo menos hoy : {fecha}")


def probandoTemplate(request):

    #cargar en memoria
    miHTML = open("C:/Users/Christian/Desktop/python curso/EntregaProyecto/Proyecto1/Proyecto1/plantillas/template1.html")

    #importar libreria template
    plantilla = Template(miHTML.read()) 

    miHTML.close() #cierro el archivo

    miContexto = Context() #datos que envio a pagina web

    documento = plantilla.render(miContexto) #renderizamos la plantilla en documento

    return HttpResponse(documento)

