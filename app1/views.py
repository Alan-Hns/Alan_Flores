from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

calculos = [
    {
        'monto': '1000000',
        'tasa': '15',
        'plazo': '1',
        'couta': '9025,831234515721',
        'total': '108309,97481418865'
    },
     {
        'monto': '800000',
        'tasa': '7',
        'plazo': '7',
        'couta': '12074,14398575148',
        'total': '1014228,0948031243'
    },
]

def index(request):
    if request.method == 'POST':
        monto = int(request.POST.get('monto'))
        tasa = int(request.POST.get('tasa'))
        plazo = int(request.POST.get('plazo'))

        r = tasa / 100 / 12

        n = plazo * 12

        c = (monto * r) / (1 - (1 + r) ** -n)
        
        t = n * c

        couta = c
        total = t 
  
        calculos.append({
            'monto': monto,
            'tasa': tasa,
            'plazo': plazo,
            'couta': couta,
            'total': total
        })

        ctx = {
            'calculos': calculos
        }

        return render(request, 'calculadora/index.html', ctx)
    else:

        ctx = {
            'calculos': calculos
        }

        return render(request, 'calculadora/index.html', ctx)
        