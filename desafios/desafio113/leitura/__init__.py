def leiaInt(prompt='', /):
    while True:
        try:
            print(prompt, end='')
            leu = int(input())
        except (ValueError, UnboundLocalError):
            print(f"\033[1;31mErro! Digite um número inteiro válido.\033[m")
        except KeyboardInterrupt:
            print('\033[1;31m\nPrograma encerrado pelo usuário.\033[m')
            try:
                return leu
            except UnboundLocalError:
                return 0
        else:
            return leu

def leiaFloat(prompt='', /):
    while True:
        try:
            print(prompt, end='')
            leu = str(input()).strip()
            if ',' in leu:
                leu = leu.replace(',', '.')
            leu = float(leu)
        except ValueError:
            print("\033[1;31mERRO! Digite um número real válido.\033[m")
        except KeyboardInterrupt:
            print('\033[1;31m\nPrograma encerrado pelo usuário.\033[m')
            try:
                return leu
            except UnboundLocalError:
                return 0
        else:
            return leu