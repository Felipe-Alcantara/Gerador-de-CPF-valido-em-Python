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

# ==================== VALIDADOR DE CPF ====================

def limpar_cpf(cpf):
    """Remove todos os caracteres não numéricos"""
    import re
    return re.sub(r'\D', '', cpf)

def validar_cpf(cpf):
    """Valida um CPF completo"""
    # Remove formatação
    cpf_limpo = limpar_cpf(cpf)
    
    # Verifica se tem 11 dígitos
    if len(cpf_limpo) != 11:
        return False, {"erro": f"CPF deve ter 11 dígitos. Você digitou {len(cpf_limpo)} dígitos."}
    
    # Verifica se não é sequência repetida
    if cpf_limpo == cpf_limpo[0] * 11:
        return False, {"erro": "CPF não pode ser uma sequência de números iguais."}
    
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
            "cpf_formatado": f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:11]}",
            "verificadores_informados": f"{primeiro_informado}{segundo_informado}",
            "verificadores_corretos": f"{primeiro_calculado}{segundo_calculado}"
        }
    
    # CPF válido!
    regioes = obter_regioes_fiscais()
    nono_digito = digitos[8]
    regiao = regioes[nono_digito]
    
    return True, {
        "cpf_formatado": f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:11]}",
        "nove_primeiros": ' '.join(map(str, nove_digitos)),
        "primeiro_verificador": primeiro_calculado,
        "segundo_verificador": segundo_calculado,
        "nono_digito": nono_digito,
        "regiao_fiscal": regiao
    }

def validar_cpf_interface(event):
    """Valida o CPF digitado pelo usuário"""
    cpf_input = document["input-cpf"].value.strip()
    
    if not cpf_input:
        return
    
    valido, info = validar_cpf(cpf_input)
    
    status_div = document["status-validacao"]
    detalhes_div = document["detalhes-validacao"]
    
    status_div.clear()
    detalhes_div.clear()
    
    if valido:
        # CPF Válido
        status_div.attrs["class"] = "status-valido"
        status_div <= html.DIV("✅ CPF VÁLIDO!")
        
        detalhes_div <= html.DIV(
            html.DIV(Class="cpf-display", text=info['cpf_formatado']) +
            html.DIV(
                html.DIV([html.SPAN("📋 Primeiros 9 dígitos: ", Class="label"), 
                          html.SPAN(info['nove_primeiros'], Class="valor")], Class="detalhes-linha") +
                html.DIV([html.SPAN("🔢 1º verificador: ", Class="label"), 
                          html.SPAN(str(info['primeiro_verificador']), Class="valor")], Class="detalhes-linha") +
                html.DIV([html.SPAN("🔢 2º verificador: ", Class="label"), 
                          html.SPAN(str(info['segundo_verificador']), Class="valor")], Class="detalhes-linha") +
                html.DIV([html.SPAN("🗺️ Região Fiscal: ", Class="label"), 
                          html.SPAN(f"Dígito {info['nono_digito']} - {info['regiao_fiscal']}", Class="valor")], 
                         Class="detalhes-linha"),
                Class="detalhes"
            )
        )
    else:
        # CPF Inválido
        status_div.attrs["class"] = "status-invalido"
        status_div <= html.DIV("❌ CPF INVÁLIDO!")
        
        detalhes_content = html.DIV(Class="detalhes")
        
        if "cpf_formatado" in info:
            detalhes_content <= html.DIV(Class="cpf-display", text=info['cpf_formatado'])
        
        detalhes_content <= html.DIV([html.SPAN("❌ Motivo: ", Class="label"), 
                                       html.SPAN(info['erro'], Class="valor")], Class="detalhes-linha")
        
        if "verificadores_informados" in info:
            detalhes_content += html.DIV([html.SPAN("🔍 Dígitos informados: ", Class="label"), 
                                          html.SPAN(info['verificadores_informados'], Class="valor")], 
                                         Class="detalhes-linha")
            detalhes_content += html.DIV([html.SPAN("✅ Dígitos corretos: ", Class="label"), 
                                          html.SPAN(info['verificadores_corretos'], Class="valor")], 
                                         Class="detalhes-linha")
        
        detalhes_div <= detalhes_content
    
    document["resultado-validador"].classList.remove("hidden")

def formatar_cpf_input(event):
    """Formata o CPF enquanto o usuário digita"""
    input_elem = event.target
    valor = limpar_cpf(input_elem.value)
    
    if len(valor) > 11:
        valor = valor[:11]
    
    # Formata: XXX.XXX.XXX-XX
    formatado = ""
    for i, char in enumerate(valor):
        if i == 3 or i == 6:
            formatado += "."
        elif i == 9:
            formatado += "-"
        formatado += char
    
    input_elem.value = formatado

# ==================== FUNÇÃO COPIAR ====================

def copiar_cpf(event):
    """Copia o CPF para a área de transferência"""
    from browser import window
    
    # Identifica qual botão foi clicado
    botao = event.target
    botao_id = botao.id
    
    # Pega o CPF correspondente
    if botao_id == "btn-copiar-aleatorio":
        cpf_texto = document["cpf-aleatorio"].text
    elif botao_id == "btn-copiar-regiao":
        cpf_texto = document["cpf-regiao"].text
    else:
        return
    
    # Copia para área de transferência
    window.navigator.clipboard.writeText(cpf_texto)
    
    # Feedback visual
    texto_original = botao.text
    botao.text = "✓ Copiado!"
    botao.classList.add("copiado")
    
    # Volta ao normal após 2 segundos
    def restaurar_botao():
        botao.text = texto_original
        botao.classList.remove("copiado")
    
    window.setTimeout(restaurar_botao, 2000)

# Vincula eventos
document["btn-gerar-aleatorio"].bind("click", gerar_cpf_aleatorio)
document["btn-gerar-outro"].bind("click", gerar_outro_cpf)
document["btn-validar"].bind("click", validar_cpf_interface)
document["input-cpf"].bind("input", formatar_cpf_input)
document["input-cpf"].bind("keypress", lambda e: validar_cpf_interface(e) if e.key == "Enter" else None)

# Vincula botões de copiar
document["btn-copiar-aleatorio"].bind("click", copiar_cpf)
document["btn-copiar-regiao"].bind("click", copiar_cpf)

# Inicializa
criar_grid_regioes()

