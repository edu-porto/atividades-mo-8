import re

# Funções que mostram para onde o rôbo vai 

def get_screwdriver():
    return "Estou a caminho da chave de fenda"

def get_screw():
    return "Estou a caminho do parafuso"

def get_measuring():
    return "Estou a caminho da trena"

def get_hose_nozzle():
    return "Estou a caminho do bico de mangueira"

def get_tape():
    return "Estou a caminho da fita"

def get_nut():
    return "Estou a caminho da porca"

def get_philips():
    return "Estou a caminho da chave Philips"

def main():
    intent_dict = {
        r"(chave\s*de\s*fenda)": get_screwdriver,
        r"(parafuso)": get_screw,
        r"(trena)": get_measuring,
        r"(bico\s*de\s*mangueira)": get_hose_nozzle,
        r"(fita)": get_tape,
        r"(porca)": get_nut,
        r"(chave\s*philips)": get_philips
    }

    # Esse loop while tem a função de manter o script rodando 
    while True:
        command = input("Digite o seu comando: (Caso deseje sair digite 'SAIR') ")
        if command == 'SAIR':
            break
        tool_found = False
        for pattern, action in intent_dict.items():
            match = re.search(pattern, command)
            if match:
                print(action()) 
                tool_found = True
                break
        else:
            print("Comando não reconhecido.")

if __name__ == '__main__':
    main()
