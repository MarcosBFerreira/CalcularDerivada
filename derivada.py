import sympy as sy
from sympy.interactive import init_printing
import numpy as np
import matplotlib.pyplot as plt

init_printing(pretty_print=True)

x = sy.symbols('x')

nova_func = []

funcao = str(input('Digite a função: '))

for i in range(len(funcao)):
    nova_func.append(funcao[i])
    if nova_func[i] == 'x':
        if nova_func[i - 1].isnumeric():
            nova_func.insert(i, '*')

for i in range(len(nova_func)):
    if nova_func[i] == 'x':
        if nova_func[i - 1].isnumeric():
            nova_func.insert(i, '*')

funcao = ''

for j in range(len(nova_func)):
    funcao += f'{nova_func[j]}'

d_x = sy.diff(funcao, x)
print(f'A derivada de {funcao} é: {d_x}')

expressao = sy.lambdify('x', funcao, 'numpy')
derivada = sy.lambdify('x', d_x, 'numpy')

x = np.linspace(-20, 20, 200)

y_expressao = expressao(x)
y_derivada = derivada(x)

plt.subplot(1, 2, 1)
plt.plot(x, y_expressao)
plt.title('Função Polinomial')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.subplot(1, 2, 2)
plt.plot(x, y_derivada)
plt.title('Derivada')
plt.xlabel('x')
plt.ylabel("f'(x)")

plt.tight_layout()
plt.show()
