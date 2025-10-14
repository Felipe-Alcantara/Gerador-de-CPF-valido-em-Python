"""
Gerador de CPF Válido
Autor: Felipe Alcântara
Descrição: Gera um número de CPF válido com dígitos verificadores corretos
"""

import random


def gerar_nove_digitos():
    """
    Gera os primeiros 9 dígitos aleatórios do CPF.
    
    Returns:
        list: Lista com 9 números aleatórios entre 0 e 9
    """
    return [random.randint(0, 9) for _ in range(9)]


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


def exibir_mensagem_geracao(cpf_formatado, digitos, digito1, digito2):
    """
    Exibe uma mensagem descritiva e bonita sobre o CPF gerado.
    
    Args:
        cpf_formatado (str): CPF completo formatado
        digitos (list): Lista com os 9 primeiros dígitos
        digito1 (int): Primeiro dígito verificador
        digito2 (int): Segundo dígito verificador
    """
    print("\n" + "="*60)
    print("          🎲 GERADOR DE CPF VÁLIDO 🎲")
    print("="*60)
    print()
    print("📋 Processo de Geração:")
    print(f"   ├─ Dígitos aleatórios gerados: {' '.join(map(str, digitos))}")
    print(f"   ├─ Primeiro dígito verificador calculado: {digito1}")
    print(f"   └─ Segundo dígito verificador calculado: {digito2}")
    print()
    print("✅ CPF GERADO COM SUCESSO!")
    print()
    print(f"   📄 Seu CPF válido é: {cpf_formatado}")
    print()
    print("="*60)
    print("⚠️  Importante: Este CPF foi gerado apenas para fins educacionais.")
    print("="*60)
    print()


def gerar_cpf_valido():
    """
    Função principal que coordena a geração do CPF e exibe o resultado.
    """
    # Gera os 9 primeiros dígitos
    digitos = gerar_nove_digitos()
    
    # Calcula os dígitos verificadores
    primeiro_digito = calcular_primeiro_digito(digitos)
    segundo_digito = calcular_segundo_digito(digitos, primeiro_digito)
    
    # Formata o CPF
    cpf_formatado = formatar_cpf(digitos, primeiro_digito, segundo_digito)
    
    # Exibe a mensagem descritiva
    exibir_mensagem_geracao(cpf_formatado, digitos, primeiro_digito, segundo_digito)
    
    return cpf_formatado


if __name__ == "__main__":
    gerar_cpf_valido()