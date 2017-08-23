import json

def main():
    while True:
        try:
            f = open("meses.txt", encoding="utf8")
            linhas = f.readlines()
            
            for linha in linhas:
                print(linha.strip())

            break

        except:
            print('Error: File not found')

        finally:
            print('Oppa Gangnam Style')

if __name__ == '__main__':
    main()
