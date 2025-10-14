"""
Gerador de CPF Válido - Versão Web com Brython
Autor: Felipe Alcântara

NOTA: Este arquivo usa Brython e só funciona no navegador.
O módulo 'browser' é fornecido automaticamente pelo Brython.
"""

from browser import document, html  # type: ignore
import random

# ==================== FUNÇÕES DO GERADOR ====================

def obter_regioes_fiscais():
    """Retorna o mapa de regiões fiscais"""
    return {
        0: "RS (Rio Grande do Sul)",
        1: "DF, GO, MT, MS, TO",
        2: "AC, AM, AP, PA, RO, RR",
        3: "CE, MA, PI",
        4: "AL, PB, PE, RN",
        5: "BA, SE",
        6: "MG (Minas Gerais)",
        7: "ES, RJ",
        8: "SP (São Paulo)",
        9: "PR, SC"
    }

def gerar_nove_digitos():
    """Gera 9 dígitos aleatórios"""
    return [random.randint(0, 9) for _ in range(9)]

def gerar_nove_digitos_com_regiao(regiao):
    """Gera 8 dígitos aleatórios + 1 da região"""
    digitos = [random.randint(0, 9) for _ in range(8)]
    digitos.append(regiao)
    return digitos

def calcular_primeiro_digito(digitos):
    """Calcula o primeiro dígito verificador"""
    soma = sum(digitos[i] * (10 - i) for i in range(9))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def calcular_segundo_digito(digitos, primeiro_digito):
    """Calcula o segundo dígito verificador"""
    digitos_completos = digitos + [primeiro_digito]
    soma = sum(digitos_completos[i] * (11 - i) for i in range(10))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def formatar_cpf(digitos, digito1, digito2):
    """Formata o CPF no padrão XXX.XXX.XXX-XX"""
    cpf_numeros = ''.join(map(str, digitos))
    return f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{digito1}{digito2}"

# ==================== FUNÇÕES DE INTERFACE ====================

def exibir_resultado_aleatorio(cpf_formatado, digitos, digito1, digito2):
    """Exibe o resultado do gerador aleatório"""
    regioes = obter_regioes_fiscais()
    nono_digito = digitos[8]
    regiao = regioes[nono_digito]
    
    cpf_display = document["cpf-aleatorio"]
    cpf_display.text = cpf_formatado
    
    detalhes = document["detalhes-aleatorio"]
    detalhes.clear()
    
    detalhes <= html.DIV(
        html.DIV([html.SPAN("📋 Dígitos gerados: ", Class="label"), 
                  html.SPAN(' '.join(map(str, digitos)), Class="valor")], Class="detalhes-linha") +
        html.DIV([html.SPAN("🔢 1º verificador: ", Class="label"), 
                  html.SPAN(str(digito1), Class="valor")], Class="detalhes-linha") +
        html.DIV([html.SPAN("🔢 2º verificador: ", Class="label"), 
                  html.SPAN(str(digito2), Class="valor")], Class="detalhes-linha") +
        html.DIV([html.SPAN("🗺️ Região Fiscal: ", Class="label"), 
                  html.SPAN(f"Dígito {nono_digito} - {regiao}", Class="valor")], Class="detalhes-linha")
    )
    
    document["resultado-aleatorio"].classList.remove("hidden")

def exibir_resultado_regiao(cpf_formatado, digitos, digito1, digito2, regiao_escolhida):
    """Exibe o resultado do gerador por região"""
    regioes = obter_regioes_fiscais()
    regiao = regioes[regiao_escolhida]
    
    cpf_display = document["cpf-regiao"]
    cpf_display.text = cpf_formatado
    
    detalhes = document["detalhes-regiao"]
    detalhes.clear()
    
    detalhes <= html.DIV(
        html.DIV([html.SPAN("📋 Dígitos (1-8): ", Class="label"), 
                  html.SPAN(' '.join(map(str, digitos[:8])), Class="valor")], Class="detalhes-linha") +
        html.DIV([html.SPAN("🗺️ 9º dígito (região): ", Class="label"), 
                  html.SPAN(str(regiao_escolhida), Class="valor")], Class="detalhes-linha") +
        html.DIV([html.SPAN("🔢 1º verificador: ", Class="label"), 
                  html.SPAN(str(digito1), Class="valor")], Class="detalhes-linha") +
        html.DIV([html.SPAN("🔢 2º verificador: ", Class="label"), 
                  html.SPAN(str(digito2), Class="valor")], Class="detalhes-linha") +
        html.DIV([html.SPAN("🗺️ Região Fiscal: ", Class="label"), 
                  html.SPAN(regiao, Class="valor")], Class="detalhes-linha")
    )
    
    document["resultado-regiao"].classList.remove("hidden")

# ==================== GERADORES ====================

def gerar_cpf_aleatorio(event):
    """Gera um CPF aleatório"""
    digitos = gerar_nove_digitos()
    primeiro_digito = calcular_primeiro_digito(digitos)
    segundo_digito = calcular_segundo_digito(digitos, primeiro_digito)
    cpf_formatado = formatar_cpf(digitos, primeiro_digito, segundo_digito)
    
    exibir_resultado_aleatorio(cpf_formatado, digitos, primeiro_digito, segundo_digito)

regiao_selecionada = None

def selecionar_regiao(event):
    """Seleciona uma região e gera o CPF"""
    global regiao_selecionada
    
    # Garante que pegamos o card correto, mesmo se clicar no filho
    target = event.target
    while target and not target.classList.contains("regiao-card"):
        target = target.parent
    
    if not target:
        return
    
    # Remove seleção anterior
    for card in document.select(".regiao-card"):
        card.classList.remove("selected")
    
    # Adiciona seleção atual
    target.classList.add("selected")
    regiao_selecionada = int(target.dataset.regiao)
    
    # Gera o CPF
    gerar_cpf_por_regiao()

def gerar_cpf_por_regiao():
    """Gera CPF da região selecionada"""
    if regiao_selecionada is None:
        return
    
    digitos = gerar_nove_digitos_com_regiao(regiao_selecionada)
    primeiro_digito = calcular_primeiro_digito(digitos)
    segundo_digito = calcular_segundo_digito(digitos, primeiro_digito)
    cpf_formatado = formatar_cpf(digitos, primeiro_digito, segundo_digito)
    
    exibir_resultado_regiao(cpf_formatado, digitos, primeiro_digito, segundo_digito, regiao_selecionada)

def gerar_outro_cpf(event):
    """Gera outro CPF da mesma região"""
    gerar_cpf_por_regiao()

# ==================== INICIALIZAÇÃO ====================

def criar_grid_regioes():
    """Cria o grid de regiões"""
    regioes = obter_regioes_fiscais()
    grid = document["regioes-grid"]
    grid.clear()
    
    for digito, nome in regioes.items():
        card = html.DIV(Class="regiao-card")
        card.dataset.regiao = str(digito)
        card <= html.DIV(str(digito), Class="regiao-numero")
        card <= html.DIV(nome, Class="regiao-nome")
        card.bind("click", selecionar_regiao)
        grid <= card

# Vincula eventos
document["btn-gerar-aleatorio"].bind("click", gerar_cpf_aleatorio)
document["btn-gerar-outro"].bind("click", gerar_outro_cpf)

# Inicializa
criar_grid_regioes()

