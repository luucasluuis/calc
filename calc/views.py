from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from calc.data import Calculadora

# por favor
calc = Calculadora()

def calculando(request):

    if request.method == 'POST':
        requisicao = request.POST.get('valor')
        
        try:
            if requisicao == 'pi':
                requisicao = calc.pi()

            float(requisicao)
            if not calc.display['op']:
                if calc.display['eq1'] is None:
                    calc.display['eq1'] = requisicao
                else:
                    if requisicao != 'pi':
                        calc.display['eq1'] = f'{calc.display['eq1']}' + f'{requisicao}'
                    else:
                        calc.display['eq1'] = calc.pi()
            else:
                if calc.display['eq2'] is None:
                    calc.display['eq2'] = requisicao
                else:
                    calc.display['eq2'] += requisicao

        except ValueError:
            if requisicao == "AC":
                calc.reset_display()
                calc.resultado = 0
            elif requisicao == '=':
                comando = calc.display.get('op')
                if comando:
                    calc.comandos[comando]()
                
                salva_eq1 = calc.resultado
                calc.reset_display()
                if salva_eq1 is not None:
                    calc.display['eq1'] = salva_eq1

            else:
                if calc.display['eq1'] is None:
                    calc.display['eq1'] = '0'

                if requisicao == ',':
                    calc.comandos[',']()
                calc.display['op'] = requisicao

        # Exibe informações de depuração
        print(calc.display.get('op'))
        print(type(calc.display.get('eq1')))
        print(calc.display.get('eq2'))
        print(calc)
        
        return render(request, 'calc/calculadora.html', calc.display)
    
    # Se a requisição não for do tipo POST, renderiza o template sem atualizar nada
    return render(request, 'calc/calculadora.html')



def exemplo(request):
    context = {
        'text': 'olá exemplo',
    }
    return render(request, 'calc/exemplo.html', context)
