<div align="center">

# 🎲 Gerador de CPF Válido em Python

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Atualizado-brightgreen.svg)

*Um projeto educacional para entender o algoritmo de validação de CPF*

</div>

---

## 📖 Sobre o Projeto

Este projeto foi criado em **2024** quando eu estava aprendendo a programar. Era um dos meus primeiros códigos em Python! 🚀

Em **outubro de 2025**, decidi revisitar este projeto e dar uma atualizada completa, aplicando boas práticas de programação, refatorando o código e tornando-o mais profissional e organizado.

### 🎯 Propósito

O objetivo principal deste projeto é **educacional**:
- 📚 Entender como funciona o algoritmo de validação de CPF brasileiro
- 💡 Aprender sobre dígitos verificadores e sua importância
- 🔢 Praticar lógica de programação com cálculos matemáticos
- ✨ Demonstrar a evolução de código desde iniciante até práticas mais avançadas

> **⚠️ IMPORTANTE:** Este gerador cria CPFs válidos **apenas do ponto de vista algorítmico**. Os números gerados NÃO são CPFs reais e NÃO devem ser utilizados para fins oficiais, cadastros ou qualquer atividade fraudulenta.

---

## 🛠️ Como Funciona

O algoritmo de validação do CPF brasileiro segue estas etapas:

### 1️⃣ Geração dos Nove Primeiros Dígitos
- Gera 9 números aleatórios entre 0 e 9
- Exemplo: `1 2 3 4 5 6 7 8 9`

### 2️⃣ Cálculo do Primeiro Dígito Verificador
- Multiplica cada dígito por uma sequência decrescente (10 a 2)
- Soma todos os resultados
- Calcula o resto da divisão por 11
- Se resto < 2: dígito = 0, senão: dígito = 11 - resto

**Exemplo:**
```
(1×10) + (2×9) + (3×8) + (4×7) + (5×6) + (6×5) + (7×4) + (8×3) + (9×2) = 210
210 % 11 = 1 (resto menor que 2)
Primeiro dígito = 0
```

### 3️⃣ Cálculo do Segundo Dígito Verificador
- Multiplica os 9 dígitos + primeiro verificador por sequência (11 a 2)
- Repete o processo de cálculo
- Resultado: segundo dígito verificador

### 4️⃣ Formatação Final
- Formato: `XXX.XXX.XXX-XX`
- Exemplo: `123.456.789-09`

---

## 🚀 Como Usar

### 🌐 Versão Web (Recomendado!)

Acesse a versão web com interface gráfica moderna:

**[🔗 Abrir Gerador Web](docs/index.html)** (ou use GitHub Pages se publicado)

#### Executar localmente:
```bash
# Na pasta docs
python -m http.server 8000

# Acesse: http://localhost:8000
```

**Funcionalidades da versão web:**
- ✨ Interface moderna e responsiva
- 🎲 Gerador aleatório com um clique
- 🗺️ Seletor visual de regiões
- 📱 Funciona em mobile
- 🎨 Design bonito com gradientes

---

### 💻 Versão Terminal

#### 1️⃣ **Gerador de CPF.py** - Gerador Aleatório Simples
Gera um CPF completamente aleatório com região fiscal automática.

```bash
python "Gerador de CPF.py"
```

#### 2️⃣ **Gerador de CPF por Região.py** - Gerador Interativo
Permite escolher a região fiscal antes de gerar o CPF!

```bash
python "Gerador de CPF por Região.py"
```

**Como funciona:**
1. O programa exibe um menu com todas as regiões fiscais (0-9)
2. Você escolhe qual região deseja
3. O CPF é gerado com o 9º dígito correspondente à região escolhida
4. Pode gerar quantos CPFs quiser da mesma região ou trocar de região

---

### 📊 Exemplo de Saída - Gerador Simples

```
======================================================================
               🎲 GERADOR DE CPF VÁLIDO 🎲
======================================================================

📋 Processo de Geração:
   ├─ Dígitos aleatórios gerados: 7 4 7 5 0 6 7 8 2
   ├─ Primeiro dígito verificador calculado: 3
   └─ Segundo dígito verificador calculado: 6

✅ CPF GERADO COM SUCESSO!

   📄 Seu CPF válido é: 747.506.782-36

🗺️  Informação da Região Fiscal:
   └─ 9º dígito (2): AC, AM, AP, PA, RO, RR (Acre, Amazonas, Amapá, Pará, Rondônia, Roraima)

======================================================================
💡 Observação: O 9º dígito indica a Região Fiscal onde o CPF foi
   registrado originalmente, não necessariamente a residência atual.

⚠️  Importante: Este CPF foi gerado apenas para fins educacionais.
======================================================================
```

### 🗺️ Exemplo de Saída - Gerador por Região

```
======================================================================
          🗺️  SELECIONE A REGIÃO FISCAL DO CPF  🗺️
======================================================================

   [0] - RS (Rio Grande do Sul)
   [1] - DF, GO, MT, MS, TO (Distrito Federal, Goiás, Mato Grosso, ...)
   [2] - AC, AM, AP, PA, RO, RR (Acre, Amazonas, Amapá, Pará, ...)
   [3] - CE, MA, PI (Ceará, Maranhão, Piauí)
   [4] - AL, PB, PE, RN (Alagoas, Paraíba, Pernambuco, ...)
   [5] - BA, SE (Bahia, Sergipe)
   [6] - MG (Minas Gerais)
   [7] - ES, RJ (Espírito Santo, Rio de Janeiro)
   [8] - SP (São Paulo)
   [9] - PR, SC (Paraná, Santa Catarina)

======================================================================
Digite o número da região desejada (0-9): 8

======================================================================
               🎲 CPF GERADO COM SUCESSO! 🎲
======================================================================

📋 Processo de Geração:
   ├─ Dígitos aleatórios (1 ao 8): 3 8 8 7 5 7 8 2
   ├─ 9º dígito (região escolhida): 8
   ├─ Primeiro dígito verificador calculado: 7
   └─ Segundo dígito verificador calculado: 3

✅ RESULTADO FINAL:

   📄 Seu CPF válido é: 388.757.828-73

🗺️  Região Fiscal Selecionada:
   └─ Dígito 8: SP (São Paulo)

======================================================================
```

---

## 📂 Estrutura do Código

### Gerador de CPF.py (Simples)

```python
├── gerar_nove_digitos()              # Gera os 9 dígitos aleatórios
├── calcular_primeiro_digito()        # Calcula 1º dígito verificador
├── calcular_segundo_digito()         # Calcula 2º dígito verificador
├── formatar_cpf()                    # Formata no padrão XXX.XXX.XXX-XX
├── identificar_regiao_fiscal()       # Identifica a região pelo 9º dígito
├── exibir_mensagem_geracao()         # Exibe mensagem descritiva
└── gerar_cpf_valido()                # Função principal
```

### Gerador de CPF por Região.py (Interativo) 🆕

```python
├── obter_regioes_fiscais()           # Retorna mapa de regiões
├── exibir_menu_regioes()             # Mostra menu de seleção
├── solicitar_regiao()                # Solicita escolha do usuário
├── gerar_oito_digitos_aleatorios()   # Gera 8 dígitos aleatórios
├── gerar_nove_digitos_com_regiao()   # Adiciona 9º dígito da região
├── calcular_primeiro_digito()        # Calcula 1º dígito verificador
├── calcular_segundo_digito()         # Calcula 2º dígito verificador
├── formatar_cpf()                    # Formata no padrão XXX.XXX.XXX-XX
├── exibir_resultado()                # Exibe resultado detalhado
├── perguntar_gerar_novamente()       # Pergunta se quer gerar outro
└── gerar_cpf_por_regiao()            # Função principal interativa
```

Cada função possui:
- ✅ Docstrings explicativas
- ✅ Nomes descritivos e claros
- ✅ Uma única responsabilidade
- ✅ Código limpo e pythônico

---

## 🗺️ Tabela de Regiões Fiscais

| Dígito | Estados | Região |
|--------|---------|--------|
| **0** | RS | Rio Grande do Sul |
| **1** | DF, GO, MT, MS, TO | Centro-Oeste + Tocantins |
| **2** | AC, AM, AP, PA, RO, RR | Região Norte |
| **3** | CE, MA, PI | Nordeste (Parte 1) |
| **4** | AL, PB, PE, RN | Nordeste (Parte 2) |
| **5** | BA, SE | Nordeste (Parte 3) |
| **6** | MG | Minas Gerais |
| **7** | ES, RJ | Sudeste (ES/RJ) |
| **8** | SP | São Paulo |
| **9** | PR, SC | Região Sul (PR/SC) |

---

## 🎓 O Que Aprendi

### Na Versão Original (2024)
- ✏️ Variáveis e tipos de dados
- 🔢 Operações matemáticas
- 🎲 Geração de números aleatórios
- 📝 Concatenação de strings

### Na Refatoração (2025)
- 🔧 Refatoração de código
- 📦 Organização em funções
- 📚 Documentação (docstrings)
- 🎨 Clean Code e boas práticas
- 💡 List comprehensions
- 🎯 Programação interativa com input
- 🗺️ Manipulação de dados estruturados (dicionários)
- 🐍 Código mais pythônico

---

## ⚖️ Considerações Legais

🚨 **ATENÇÃO**: Este projeto é **exclusivamente educacional**.

- ❌ NÃO use os CPFs gerados para cadastros reais
- ❌ NÃO use para fins comerciais ou fraudulentos
- ❌ NÃO são CPFs registrados na Receita Federal
- ✅ Use apenas para aprendizado e testes

O uso indevido de CPFs pode configurar crime conforme o Código Penal Brasileiro.

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

**Felipe Alcântara**

- 📧 Entre em contato para dúvidas ou sugestões
- 🌟 Se este projeto te ajudou, considere dar uma estrela!

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- 🐛 Reportar bugs
- 💡 Sugerir melhorias
- 🔀 Enviar pull requests

---

<div align="center">

**Feito com 💙 e Python**

*De um iniciante em 2024 para um código mais maduro em 2025* 🚀

</div>