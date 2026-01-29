def leiaInt(prompt='', /, padrao=0):
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
                return padrao
        else:
            return leu

def leiaFloat(prompt='', /, padrao=0):
    while True:
        try:
            print(prompt, end='')
            leu = str(input()).strip()
            if ',' in leu:
                leu = leu.replace(',', '.')
            leu = float(leu)
        except ValueError:
            print("\033[mERRO! Digite um número real válido.\033[m")
        except KeyboardInterrupt:
            print('\033[1;31m\nPrograma encerrado pelo usuário.\033[m')
            try:
                return leu
            except UnboundLocalError:
                return padrao
        else:
            return leu