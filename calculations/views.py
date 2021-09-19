from django.shortcuts import render
from .models import calc
from json import dumps

def index(request):
    all_calc = calc.objects.all()
    data = []
    x = 0
    for cal in reversed(all_calc):
        x += 1
        if x == 11:
            break
        lis = [str(cal.Time),str(cal.field1),str(cal.field2),str(cal.field3),str(cal.field4),str(cal.field5),str(cal.field6),str(cal.field7),str(cal.field8)]
        data.append(lis)
    params = {'d1t1' : str(data[0][0]),'d1f1' : str(data[0][1]),'d1f2' : str(data[0][2]),'d1f3' : str(data[0][3]),'d1f4' : str(data[0][4]),'d1f5' : str(data[0][5]),'d1f6' : str(data[0][6]),'d1f7' : str(data[0][7]),'d1f8' : str(data[0][8]),
              'd2t1' : str(data[1][0]),'d2f1' : str(data[1][1]),'d2f2' : str(data[1][2]),'d2f3' : str(data[1][3]),'d2f4' : str(data[1][4]),'d2f5' : str(data[1][5]),'d2f6' : str(data[1][6]),'d2f7' : str(data[1][7]),'d2f8' : str(data[1][8]),
              'd3t1' : str(data[2][0]),'d3f1' : str(data[2][1]),'d3f2' : str(data[2][2]),'d3f3' : str(data[2][3]),'d3f4' : str(data[2][4]),'d3f5' : str(data[2][5]),'d3f6' : str(data[2][6]),'d3f7' : str(data[2][7]),'d3f8' : str(data[2][8]),
              'd4t1' : str(data[3][0]),'d4f1' : str(data[3][1]),'d4f2' : str(data[3][2]),'d4f3' : str(data[3][3]),'d4f4' : str(data[3][4]),'d4f5' : str(data[3][5]),'d4f6' : str(data[3][6]),'d4f7' : str(data[3][7]),'d4f8' : str(data[3][8]),
              'd5t1' : str(data[4][0]),'d5f1' : str(data[4][1]),'d5f2' : str(data[4][2]),'d5f3' : str(data[4][3]),'d5f4' : str(data[4][4]),'d5f5' : str(data[4][5]),'d5f6' : str(data[4][6]),'d5f7' : str(data[4][7]),'d5f8' : str(data[4][8]),
              'd6t1' : str(data[5][0]),'d6f1' : str(data[5][1]),'d6f2' : str(data[5][2]),'d6f3' : str(data[5][3]),'d6f4' : str(data[5][4]),'d6f5' : str(data[5][5]),'d6f6' : str(data[5][6]),'d6f7' : str(data[5][7]),'d6f8' : str(data[5][8]),
              'd7t1' : str(data[6][0]),'d7f1' : str(data[6][1]),'d7f2' : str(data[6][2]),'d7f3' : str(data[6][3]),'d7f4' : str(data[6][4]),'d7f5' : str(data[6][5]),'d7f6' : str(data[6][6]),'d7f7' : str(data[6][7]),'d7f8' : str(data[6][8]),
              'd8t1' : str(data[7][0]),'d8f1' : str(data[7][1]),'d8f2' : str(data[7][2]),'d8f3' : str(data[7][3]),'d8f4' : str(data[7][4]),'d8f5' : str(data[7][5]),'d8f6' : str(data[7][6]),'d8f7' : str(data[7][7]),'d8f8' : str(data[7][8]),
              'd9t1' : str(data[8][0]),'d9f1' : str(data[8][1]),'d9f2' : str(data[8][2]),'d9f3' : str(data[8][3]),'d9f4' : str(data[8][4]),'d9f5' : str(data[8][5]),'d9f6' : str(data[8][6]),'d9f7' : str(data[8][7]),'d9f8' : str(data[8][8]),
              'd10t1' : str(data[9][0]),'d10f1' : str(data[9][1]),'d10f2' : str(data[9][2]),'d10f3' : str(data[9][3]),'d10f4' : str(data[9][4]),'d10f5' : str(data[9][5]),'d10f6' : str(data[9][6]),'d10f7' : str(data[9][7]),'d10f8' : str(data[9][8])
         }

    return render(request,'Tables.html',params)


def graph(request):
    all_calc = calc.objects.all()
    data = []
    x = 0
    for cal in reversed(all_calc):
        x += 1
        if x == 11:
            break
        dat = str(cal.Time).split('|')[0]
        tim = str(cal.Time).split('|')[1]
        lis = [tim,dat,str(cal.field1),str(cal.field2),str(cal.field3),str(cal.field4),str(cal.field5),str(cal.field6),str(cal.field7),str(cal.field8)]
        data.append(lis)

    params = {'d1t1' : str(data[0][0]),'d1d1' : str(data[0][1]),'d1f1' : str(data[0][2]),'d1f2' : str(data[0][3]),'d1f3' : str(data[0][4]),'d1f4' : str(data[0][5]),'d1f5' : str(data[0][6]),'d1f6' : str(data[0][7]),'d1f7' : str(data[0][8]),'d1f8' : str(data[0][9]),
              'd2t1' : str(data[1][0]),'d2d1' : str(data[1][1]),'d2f1' : str(data[1][2]),'d2f2' : str(data[1][3]),'d2f3' : str(data[1][4]),'d2f4' : str(data[1][5]),'d2f5' : str(data[1][6]),'d2f6' : str(data[1][7]),'d2f7' : str(data[1][8]),'d2f8' : str(data[1][9]),
              'd3t1' : str(data[2][0]),'d3d1' : str(data[2][1]),'d3f1' : str(data[2][2]),'d3f2' : str(data[2][3]),'d3f3' : str(data[2][4]),'d3f4' : str(data[2][5]),'d3f5' : str(data[2][6]),'d3f6' : str(data[2][7]),'d3f7' : str(data[2][8]),'d3f8' : str(data[2][9]),
              'd4t1' : str(data[3][0]),'d4d1' : str(data[3][1]),'d4f1' : str(data[3][2]),'d4f2' : str(data[3][3]),'d4f3' : str(data[3][4]),'d4f4' : str(data[3][5]),'d4f5' : str(data[3][6]),'d4f6' : str(data[3][7]),'d4f7' : str(data[3][8]),'d4f8' : str(data[3][9]),
              'd5t1' : str(data[4][0]),'d5d1' : str(data[4][1]),'d5f1' : str(data[4][2]),'d5f2' : str(data[4][3]),'d5f3' : str(data[4][4]),'d5f4' : str(data[4][5]),'d5f5' : str(data[4][6]),'d5f6' : str(data[4][7]),'d5f7' : str(data[4][8]),'d5f8' : str(data[4][9]),
              'd6t1' : str(data[5][0]),'d6d1' : str(data[5][1]),'d6f1' : str(data[5][2]),'d6f2' : str(data[5][3]),'d6f3' : str(data[5][4]),'d6f4' : str(data[5][5]),'d6f5' : str(data[5][6]),'d6f6' : str(data[5][7]),'d6f7' : str(data[5][8]),'d6f8' : str(data[5][9]),
              'd7t1' : str(data[6][0]),'d7d1' : str(data[6][1]),'d7f1' : str(data[6][2]),'d7f2' : str(data[6][3]),'d7f3' : str(data[6][4]),'d7f4' : str(data[6][5]),'d7f5' : str(data[6][6]),'d7f6' : str(data[6][7]),'d7f7' : str(data[6][8]),'d7f8' : str(data[6][9]),
              'd8t1' : str(data[7][0]),'d8d1' : str(data[7][1]),'d8f1' : str(data[7][2]),'d8f2' : str(data[7][3]),'d8f3' : str(data[7][4]),'d8f4' : str(data[7][5]),'d8f5' : str(data[7][6]),'d8f6' : str(data[7][7]),'d8f7' : str(data[7][8]),'d8f8' : str(data[7][9]),
              'd9t1' : str(data[8][0]),'d9d1' : str(data[8][1]),'d9f1' : str(data[8][2]),'d9f2' : str(data[8][3]),'d9f3' : str(data[8][4]),'d9f4' : str(data[8][5]),'d9f5' : str(data[8][6]),'d9f6' : str(data[8][7]),'d9f7' : str(data[8][8]),'d9f8' : str(data[8][9]),
              'd10t1' : str(data[9][0]),'d10d1' : str(data[9][1]),'d10f1' : str(data[9][2]),'d10f2' : str(data[9][3]),'d10f3' : str(data[9][4]),'d10f4' : str(data[9][5]),'d10f5' : str(data[9][6]),'d10f6' : str(data[9][7]),'d10f7' : str(data[9][8]),'d10f8' : str(data[9][9])
         }
    dataJSON = dumps(params)
    return render(request,'graph.html',{'data':dataJSON})
