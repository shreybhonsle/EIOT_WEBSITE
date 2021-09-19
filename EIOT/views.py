from django.shortcuts import render
from django.http import HttpResponse
from calculations.models import calc
from datetime import datetime

def index(request):
    all_calc = calc.objects.all()
    average =[]
    field1 = 0.0
    field2 = 0.0
    field3 = 0.0
    field4 = 0.0
    field5 = 0.0
    field6 = 0.0
    field7 = 0.0
    field8 = 0.0
    x=0
    for a in all_calc:
        x+=1
        if x == 10:
            break
        field1 += a.field1
        field2 += a.field2
        field3 += a.field3
        field4 += a.field4
        field5 += a.field5
        field6 += a.field6
        field7 += a.field7
        field8 += a.field8
    field1 = field1 / 10
    field2 = field2 / 10
    field3 = field3 / 10
    field4 = field4 / 10
    field5 = field5 / 10
    field6 = field6 / 10
    field7 = field7 / 10
    field8 = field8 / 10
    params =   {'Temp': str(field1),'Humidity': str(field2),'PM2':str(field3),'PM10':str(field4),'pressure':str(field5),'CO':str(field6),'NH3':str(field7),'03':str(field8) }


    return render(request,'index.html',params)


def insert(request):
    f1 = request.GET.get('field1','0')
    f2 = request.GET.get('field2','0')
    f3 = request.GET.get('field3','0')
    f4 = request.GET.get('field4','0')
    f5 = request.GET.get('field5','0')
    f6 = request.GET.get('field6','0')
    f7 = request.GET.get('field7','0')
    f8 = request.GET.get('field8','0')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y | %H:%M:%S")
    a= calc(Time=dt_string,field1 = float(f1),field2 = float(f2),field3 = float(f3),field4 = float(f4),field5 = float(f5),field6 = float(f6),field7 = float(f7),field8 = float(f8) )
    a.save()
    return HttpResponse()





