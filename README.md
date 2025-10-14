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

### Pré-requisitos
- Python 3.x instalado

### Executando o Gerador

```bash
python "Gerador de CPF.py"
```

### Saída Esperada

```
============================================================
          🎲 GERADOR DE CPF VÁLIDO 🎲
============================================================

📋 Processo de Geração:
   ├─ Dígitos aleatórios gerados: 1 2 3 4 5 6 7 8 9
   ├─ Primeiro dígito verificador calculado: 0
   └─ Segundo dígito verificador calculado: 9

✅ CPF GERADO COM SUCESSO!

   📄 Seu CPF válido é: 123.456.789-09

============================================================
⚠️  Importante: Este CPF foi gerado apenas para fins educacionais.
============================================================
```

---

## 📂 Estrutura do Código

O código foi completamente refatorado e organizado em funções:

```python
├── gerar_nove_digitos()           # Gera os 9 dígitos aleatórios
├── calcular_primeiro_digito()     # Calcula 1º dígito verificador
├── calcular_segundo_digito()      # Calcula 2º dígito verificador
├── formatar_cpf()                 # Formata no padrão XXX.XXX.XXX-XX
├── exibir_mensagem_geracao()      # Exibe mensagem descritiva
└── gerar_cpf_valido()             # Função principal
```

Cada função possui:
- ✅ Docstrings explicativas
- ✅ Nomes descritivos e claros
- ✅ Uma única responsabilidade
- ✅ Código limpo e pythônico

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