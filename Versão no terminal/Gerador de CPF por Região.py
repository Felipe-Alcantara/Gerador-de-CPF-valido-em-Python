"""
Gerador de CPF Válido por Região
Autor: Felipe Alcântara
Descrição: Gera um número de CPF válido permitindo escolher a região fiscal desejada
"""

import random


def obter_regioes_fiscais():
    """
    Retorna o dicionário com todas as regiões fiscais disponíveis.
    
    Returns:
        dict: Mapa de dígitos para regiões
    """
    return {
        0: "RS (Rio Grande do Sul)",
        1: "DF, GO, MT, MS, TO (Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul, Tocantins)",
        2: "AC, AM, AP, PA, RO, RR (Acre, Amazonas, Amapá, Pará, Rondônia, Roraima)",
        3: "CE, MA, PI (Ceará, Maranhão, Piauí)",
        4: "AL, PB, PE, RN (Alagoas, Paraíba, Pernambuco, Rio Grande do Norte)",
        5: "BA, SE (Bahia, Sergipe)",
        6: "MG (Minas Gerais)",
        7: "ES, RJ (Espírito Santo, Rio de Janeiro)",
        8: "SP (São Paulo)",
        9: "PR, SC (Paraná, Santa Catarina)"
    }


def exibir_menu_regioes():
    """
    Exibe o menu com todas as regiões fiscais disponíveis.
    """
    regioes = obter_regioes_fiscais()
    
    print("\n" + "="*70)
    print("          🗺️  SELECIONE A REGIÃO FISCAL DO CPF  🗺️")
    print("="*70)
    print()
    
    for digito, regiao in regioes.items():
        print(f"   [{digito}] - {regiao}")
    
    print()
    print("="*70)


def solicitar_regiao():
    """
    Solicita ao usuário que escolha uma região fiscal válida.
    
    Returns:
        int: Dígito da região escolhida (0-9)
    """
    while True:
        try:
            exibir_menu_regioes()
            escolha = input("Digite o número da região desejada (0-9): ").strip()
            
            digito = int(escolha)
            
            if 0 <= digito <= 9:
                return digito
            else:
                print("\n❌ Erro: Por favor, digite um número entre 0 e 9.")
                input("Pressione ENTER para tentar novamente...")
        except ValueError:
            print("\n❌ Erro: Por favor, digite apenas números.")
            input("Pressione ENTER para tentar novamente...")
        except KeyboardInterrupt:
            print("\n\n👋 Operação cancelada pelo usuário.")
            exit(0)


def gerar_oito_digitos_aleatorios():
    """
    Gera os primeiros 8 dígitos aleatórios do CPF.
    
    Returns:
        list: Lista com 8 números aleatórios entre 0 e 9
    """
    return [random.randint(0, 9) for _ in range(8)]


def gerar_nove_digitos_com_regiao(regiao_escolhida):
    """
    Gera os primeiros 9 dígitos do CPF com o 9º dígito definido pela região.
    
    Args:
        regiao_escolhida (int): Dígito da região fiscal (0-9)
        
    Returns:
        list: Lista com 9 dígitos (8 aleatórios + 1 da região)
    """
    digitos = gerar_oito_digitos_aleatorios()
    digitos.append(regiao_escolhida)  # 9º dígito = região fiscal
    return digitos


def calcular_primeiro_digito(digitos):
    """
    Calcula o primeiro dígito verificador do CPF.
    
    Args:
        digitos (list): Lista com os 9 primeiros dígitos do CPF
        
    Returns:
        int: Primeiro dígito verificador
    """
    soma = sum(digitos[i] * (10 - i) for i in range(9))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto


def calcular_segundo_digito(digitos, primeiro_digito):
    """
    Calcula o segundo dígito verificador do CPF.
    
    Args:
        digitos (list): Lista com os 9 primeiros dígitos do CPF
        primeiro_digito (int): Primeiro dígito verificador
        
    Returns:
        int: Segundo dígito verificador
    """
    digitos_completos = digitos + [primeiro_digito]
    soma = sum(digitos_completos[i] * (11 - i) for i in range(10))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto


def formatar_cpf(digitos, digito1, digito2):
    """
    Formata o CPF no padrão XXX.XXX.XXX-XX.
    
    Args:
        digitos (list): Lista com os 9 primeiros dígitos
        digito1 (int): Primeiro dígito verificador
        digito2 (int): Segundo dígito verificador
        
    Returns:
        str: CPF formatado
    """
    cpf_numeros = ''.join(map(str, digitos))
    return f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{digito1}{digito2}"


def exibir_resultado(cpf_formatado, digitos, digito1, digito2, regiao_escolhida):
    """
    Exibe o resultado da geração do CPF com informações detalhadas.
    
    Args:
        cpf_formatado (str): CPF completo formatado
        digitos (list): Lista com os 9 primeiros dígitos
        digito1 (int): Primeiro dígito verificador
        digito2 (int): Segundo dígito verificador
        regiao_escolhida (int): Dígito da região fiscal escolhida
    """
    regioes = obter_regioes_fiscais()
    regiao_nome = regioes[regiao_escolhida]
    
    print("\n" + "="*70)
    print("               🎲 CPF GERADO COM SUCESSO! 🎲")
    print("="*70)
    print()
    print("📋 Processo de Geração:")
    print(f"   ├─ Dígitos aleatórios (1 ao 8): {' '.join(map(str, digitos[:8]))}")
    print(f"   ├─ 9º dígito (região escolhida): {regiao_escolhida}")
    print(f"   ├─ Primeiro dígito verificador calculado: {digito1}")
    print(f"   └─ Segundo dígito verificador calculado: {digito2}")
    print()
    print("✅ RESULTADO FINAL:")
    print()
    print(f"   📄 Seu CPF válido é: {cpf_formatado}")
    print()
    print("🗺️  Região Fiscal Selecionada:")
    print(f"   └─ Dígito {regiao_escolhida}: {regiao_nome}")
    print()
    print("="*70)
    print("💡 Observação: O 9º dígito indica a Região Fiscal onde o CPF foi")
    print("   registrado originalmente, não necessariamente a residência atual.")
    print()
    print("⚠️  Importante: Este CPF foi gerado apenas para fins educacionais.")
    print("="*70)
    print()


def perguntar_gerar_novamente():
    """
    Pergunta ao usuário se deseja gerar outro CPF.
    
    Returns:
        bool: True se deseja gerar novamente, False caso contrário
    """
    while True:
        resposta = input("Deseja gerar outro CPF? (S/N): ").strip().upper()
        
        if resposta in ['S', 'SIM', 'Y', 'YES']:
            return True
        elif resposta in ['N', 'NAO', 'NÃO', 'NO']:
            return False
        else:
            print("❌ Por favor, responda com S (Sim) ou N (Não).")


def gerar_cpf_por_regiao():
    """
    Função principal que coordena a geração interativa do CPF por região.
    """
    print("\n" + "="*70)
    print("          🎯 GERADOR DE CPF VÁLIDO POR REGIÃO 🎯")
    print("="*70)
    print()
    print("Este gerador permite escolher a região fiscal do CPF a ser gerado!")
    print()
    input("Pressione ENTER para começar...")
    
    while True:
        # Solicita a região desejada
        regiao_escolhida = solicitar_regiao()
        
        # Gera os 9 primeiros dígitos (8 aleatórios + 1 da região)
        digitos = gerar_nove_digitos_com_regiao(regiao_escolhida)
        
        # Calcula os dígitos verificadores
        primeiro_digito = calcular_primeiro_digito(digitos)
        segundo_digito = calcular_segundo_digito(digitos, primeiro_digito)
        
        # Formata o CPF
        cpf_formatado = formatar_cpf(digitos, primeiro_digito, segundo_digito)
        
        # Exibe o resultado
        exibir_resultado(cpf_formatado, digitos, primeiro_digito, segundo_digito, regiao_escolhida)
        
        # Pergunta se deseja gerar outro
        if not perguntar_gerar_novamente():
            print("\n" + "="*70)
            print("          👋 Obrigado por usar o Gerador de CPF!")
            print("                    Até a próxima! 🚀")
            print("="*70)
            print()
            break


if __name__ == "__main__":
    try:
        gerar_cpf_por_regiao()
    except KeyboardInterrupt:
        print("\n\n👋 Programa encerrado pelo usuário. Até logo!")
