import math

class Calculadora:
    def __init__(self):
        self.resultado = None
        self.display = {'eq1': None,
                        'op': '',
                        'eq2': None,
                        'resultado': 0}
        self.metodo = ''
        self.comandos = {
            '+': lambda: self.soma(),
            ',': lambda: self.parse_float(),
            '-': lambda: self.subtracao(),
            '*': lambda: self.multiplicacao(),
            '%': lambda: self.resto(),
            '/': lambda: self.divisao(),
            'rad': lambda: self.radiciacao(),
            'pi': lambda: self.pi(),
            '^': lambda: self.exponenciacao(),
            '!': lambda: self.fatorial(),
            'sin': lambda: self.sin(),
            'cos': lambda: self.cos(),
            'tan': lambda: self.tan(),
            'log': lambda: self.logaritmo(),
        }
  

    def __str__(self):
        return f'Resultado: {0 if self.resultado is None else self.resultado}'

    def reset_display(self):
        self.display = {'eq1': None,
                        'op': '',
                        'eq2': None,
                                    }

    def parse_float(self):
        if self.display['eq1'] is None:
            self.display['eq1'] = float(0)
            return self.display['eq1']
        
        if self.display['eq2'] is None:  
            self.display['eq1'] = float(self.display['eq1']) # Mudança aqui
            return self.display['eq1']
        else:
            self.display['eq2'] = float(self.display['eq2'])


    def soma(self):
        x, y = self.display['eq1'], self.display['eq2']
        if self.display['eq2'] is None:
            y = 0
        x, y = float(x), float(y)

        self.resultado = x + y
        return self.resultado
    
    def pi(self):
        return round(math.pi, 2)

    def subtracao(self):
        x, y = self.display['eq1'], self.display['eq2']
        self.resultado = float(x) - float(y)
        return self.resultado

    def multiplicacao(self):
        x, y = self.display['eq1'], self.display['eq2']
        self.resultado = float(x) * float(y)
        return self.resultado
    
    def resto(self):
        x, y = self.display['eq1'], self.display['eq2']
        try:
            self.resultado = float(x) % float(y)
        except ZeroDivisionError:
            self.resultado = 'Não é possivel dividir por zero'
        return self.resultado
    
    def divisao(self):
        x, y = self.display['eq1'], self.display['eq2']
        try:
            self.resultado = float(x) / float(y)
        except ZeroDivisionError:
            self.resultado = 'Não é possivel dividir por zero'
        return self.resultado
    
    def radiciacao(self):
        self.resultado = math.sqrt(float(self.display['eq1']))
        return self.resultado

    def exponenciacao(self):
        base, expoente = self.display['eq1'], self.display['eq2']
        self.resultado = float(base) ** float(expoente)
        return self.resultado

    def fatorial(self):
        num = self.display['eq1']
        self.resultado = math.factorial(int(num))
        return self.resultado
    
    def sin(self):
        angulo = self.display['eq1']
        angulo_rad = math.radians(float(angulo))
        self.resultado = round(math.sin(angulo_rad), 2)
        return self.resultado

    def cos(self):
        angulo = self.display['eq1']
        angulo_rad = math.radians(float(angulo))
        self.resultado = round(math.cos(angulo_rad), 2)
        return self.resultado

    def tan(self):
        angulo = self.display['eq1']
        angulo_rad = math.radians(float(angulo))
        self.resultado = round(math.tan(angulo_rad), 2)
        return self.resultado


    def logaritmo(self):
        num, base = self.display['eq1'], self.display['eq2']
        self.resultado = math.log(float(num), float(base))
        return self.resultado

    def all_clear(self):
        self.resultado = None
        return "Resultado resetado."

    def mostra_instrucao(self):
        print('Digite "AC" para resetar o resultado ou "sair" para fechar a calculadora')

    def solicita_entrada(self):
        return input('Qual operação deseja realizar?\n').lower()

if __name__ == '__main__':
  calc = Calculadora()
  print(calc)
  calc.mostra_instrucao()
  operacao = calc.solicita_entrada()

  while operacao != 'sair':

      if operacao == "ac":
          print(calc.all_clear())
          calc.mostra_instrucao()
          print(calc)
          operacao = calc.solicita_entrada()
          continue

      match operacao:
          case '+':
              operacao = 'soma'
          case '-':
              operacao = 'subtracao'
          case '*':
              operacao = 'multiplicacao'
          case '/':
              operacao = 'divisao'
          case '^':
              operacao = 'exponenciacao'

      comando = calc.comandos.get(operacao)
      if comando is None:
        print('Não há essa operação no momento. Prometemos atualizar em breve')
        operacao = calc.solicita_entrada()
        continue

      possiveis_args = ("Digite os números separados por espaço (ou deixe em"\
      "branco para usar o resultado anterior): ") if operacao != 'trigonometria'\
      else ("Entre com o angulo em graus: ")

      args = input(possiveis_args).split()
      if not args:
          print(calc)
          args = salva_args,
          comando()
          continue
      else:
          args = list(map(float, args))
          salva_args = args[-1]

      comando()
      print(calc, end='\n\n') # mostra o resultado atual atraves do dunder __str__
      calc.mostra_instrucao()
      operacao = calc.solicita_entrada()