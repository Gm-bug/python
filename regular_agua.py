from colorama import Fore, Style, init

# Inicializa o colorama (autoreset restaura a cor padrão após cada print)
init(autoreset=True)

# Lista com os níveis do reservatório, situação e cor correspondente
niveis_reservatorio = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": Fore.BLUE},
]


def definir_cor_mensagem(nivel):
    """
    Função responsável por definir a cor e a mensagem
    conforme o nível de água informado.
    """
    for item in niveis_reservatorio:
        if item["nivel"] == nivel:
            return item["cor"], item["situacao"]
    return Style.RESET_ALL, "Nível inválido"


def exibir_situacao(nivel):
    """
    Exibe no terminal a situação atual do reservatório
    com a cor correspondente ao nível.
    """
    cor, situacao = definir_cor_mensagem(nivel)
    print(f"{cor}Nível {nivel}: {situacao}")


def main():
    print("=== Sistema de Monitoramento de Reservatório de Água ===\n")

    # Simulação com todos os níveis definidos no código
    for nivel in range(1, 6):
        exibir_situacao(nivel)

    # Restaura o estilo padrão do terminal
    print(Style.RESET_ALL)
    print("\nMonitoramento finalizado.")


if __name__ == "__main__":
    main()
