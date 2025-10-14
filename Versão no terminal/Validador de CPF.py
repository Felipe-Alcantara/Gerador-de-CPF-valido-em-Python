"""
Validador de CPF
Autor: Felipe Alcântara
Descrição: Valida se um CPF é válido ou não usando o algoritmo de dígitos verificadores
"""

import re


def limpar_cpf(cpf):
    """
    Remove todos os caracteres não numéricos do CPF.
    
    Args:
        cpf (str): CPF em qualquer formato
        
    Returns:
        str: CPF apenas com números
    """
    return re.sub(r'\D', '', cpf)


def validar_formato(cpf_limpo):
    """
    Verifica se o CPF tem 11 dígitos e não é uma sequência repetida.
    
    Args:
        cpf_limpo (str): CPF apenas com números
        
    Returns:
        tuple: (bool: é_valido, str: mensagem_erro)
    """
    # Verifica se tem 11 dígitos
    if len(cpf_limpo) != 11:
        return False, f"CPF deve ter 11 dígitos. Você digitou {len(cpf_limpo)} dígitos."
    
    # Verifica se não é uma sequência repetida (111.111.111-11, 222.222.222-22, etc)
    if cpf_limpo == cpf_limpo[0] * 11:
        return False, "CPF não pode ser uma sequência de números iguais."
    
    return True, ""


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


def identificar_regiao_fiscal(digitos):
    """
    Identifica a região fiscal baseada no 9º dígito do CPF.
    
    Args:
        digitos (list): Lista com os 11 dígitos do CPF
        
    Returns:
        tuple: (dígito, região/estados correspondentes)
    """
    mapa_regioes = {
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
    
    nono_digito = digitos[8]
    return nono_digito, mapa_regioes[nono_digito]


def validar_cpf(cpf):
    """
    Valida um CPF completo.
    
    Args:
        cpf (str): CPF em qualquer formato
        
    Returns:
        tuple: (bool: é_valido, dict: informações)
    """
    # Remove formatação
    cpf_limpo = limpar_cpf(cpf)
    
    # Valida formato básico
    formato_valido, mensagem_erro = validar_formato(cpf_limpo)
    if not formato_valido:
        return False, {"erro": mensagem_erro}
    
    # Converte para lista de inteiros
    digitos = [int(d) for d in cpf_limpo]
    
    # Pega os 9 primeiros dígitos
    nove_digitos = digitos[:9]
    
    # Calcula os dígitos verificadores
    primeiro_calculado = calcular_primeiro_digito(nove_digitos)
    segundo_calculado = calcular_segundo_digito(nove_digitos, primeiro_calculado)
    
    # Pega os dígitos verificadores informados
    primeiro_informado = digitos[9]
    segundo_informado = digitos[10]
    
    # Verifica se os dígitos conferem
    if primeiro_calculado != primeiro_informado or segundo_calculado != segundo_informado:
        return False, {
            "erro": "Dígitos verificadores inválidos",
            "verificadores_informados": f"{primeiro_informado}{segundo_informado}",
            "verificadores_corretos": f"{primeiro_calculado}{segundo_calculado}"
        }
    
    # CPF válido! Retorna informações adicionais
    nono_digito, regiao = identificar_regiao_fiscal(digitos)
    
    return True, {
        "cpf_formatado": f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:11]}",
        "nove_primeiros": ' '.join(map(str, nove_digitos)),
        "primeiro_verificador": primeiro_calculado,
        "segundo_verificador": segundo_calculado,
        "nono_digito": nono_digito,
        "regiao_fiscal": regiao
    }


def exibir_resultado(cpf_original, valido, informacoes):
    """
    Exibe o resultado da validação de forma bonita.
    
    Args:
        cpf_original (str): CPF original digitado
        valido (bool): Se o CPF é válido
        informacoes (dict): Informações sobre o CPF
    """
    print("\n" + "="*70)
    
    if valido:
        print("               ✅ CPF VÁLIDO!")
        print("="*70)
        print()
        print(f"📄 CPF Formatado: {informacoes['cpf_formatado']}")
        print()
        print("📋 Detalhes da Validação:")
        print(f"   ├─ Primeiros 9 dígitos: {informacoes['nove_primeiros']}")
        print(f"   ├─ 1º dígito verificador: {informacoes['primeiro_verificador']}")
        print(f"   └─ 2º dígito verificador: {informacoes['segundo_verificador']}")
        print()
        print("🗺️  Informação da Região Fiscal:")
        print(f"   └─ 9º dígito ({informacoes['nono_digito']}): {informacoes['regiao_fiscal']}")
        print()
        print("="*70)
        print("💡 Este CPF possui dígitos verificadores corretos.")
    else:
        print("               ❌ CPF INVÁLIDO!")
        print("="*70)
        print()
        print(f"📄 CPF Digitado: {cpf_original}")
        print()
        print("❌ Motivo da Invalidação:")
        
        if "erro" in informacoes:
            print(f"   └─ {informacoes['erro']}")
            
            if "verificadores_informados" in informacoes:
                print()
                print("🔍 Comparação dos Dígitos Verificadores:")
                print(f"   ├─ Dígitos informados: {informacoes['verificadores_informados']}")
                print(f"   └─ Dígitos corretos:   {informacoes['verificadores_corretos']}")
        
        print()
        print("="*70)
        print("💡 Os dígitos verificadores não conferem com o algoritmo.")
    
    print()


def solicitar_cpf():
    """
    Solicita ao usuário que digite um CPF para validar.
    
    Returns:
        str: CPF digitado pelo usuário
    """
    print("\n" + "="*70)
    print("          🔍 VALIDADOR DE CPF")
    print("="*70)
    print()
    print("Digite um CPF para validar.")
    print("Pode usar qualquer formato:")
    print("  • 123.456.789-09")
    print("  • 12345678909")
    print("  • 123 456 789 09")
    print()
    print("="*70)
    print()
    
    cpf = input("Digite o CPF: ").strip()
    return cpf


def perguntar_validar_novamente():
    """
    Pergunta ao usuário se deseja validar outro CPF.
    
    Returns:
        bool: True se deseja validar novamente, False caso contrário
    """
    while True:
        resposta = input("Deseja validar outro CPF? (S/N): ").strip().upper()
        
        if resposta in ['S', 'SIM', 'Y', 'YES']:
            return True
        elif resposta in ['N', 'NAO', 'NÃO', 'NO']:
            return False
        else:
            print("❌ Por favor, responda com S (Sim) ou N (Não).")


def main():
    """
    Função principal do validador de CPF.
    """
    print("\n" + "="*70)
    print("          🔍 VALIDADOR DE CPF - BEM-VINDO!")
    print("="*70)
    print()
    print("Este programa valida se um CPF é válido usando o algoritmo")
    print("de dígitos verificadores da Receita Federal.")
    print()
    input("Pressione ENTER para começar...")
    
    while True:
        # Solicita CPF
        cpf = solicitar_cpf()
        
        # Valida o CPF
        valido, informacoes = validar_cpf(cpf)
        
        # Exibe resultado
        exibir_resultado(cpf, valido, informacoes)
        
        # Pergunta se deseja validar outro
        if not perguntar_validar_novamente():
            print("\n" + "="*70)
            print("          👋 Obrigado por usar o Validador de CPF!")
            print("                    Até a próxima! 🚀")
            print("="*70)
            print()
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programa encerrado pelo usuário. Até logo!")
