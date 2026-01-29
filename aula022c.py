try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi: {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print("Volte sempre! Muito obrigado!")

"""
a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a / b
print(f'O resultado é {r}')

Traceback (most recent call last):
  File "c:\Github\desafios-aula-23\aula022c.py", line 3, in <module>
    r = a / b
        ~~^~~
ZeroDivisionError: division by zero
"""