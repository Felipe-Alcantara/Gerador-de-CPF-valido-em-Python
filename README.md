# Gerador de CPF Válido em Python

Este projeto contém um script Python que gera números de CPF (Cadastro de Pessoas Físicas) válidos de acordo com as regras estabelecidas pela Receita Federal do Brasil. O CPF é um número de identificação de indivíduos no Brasil.

O script realiza as seguintes operações:

1. **Geração dos Nove Primeiros Dígitos**: O script gera os nove primeiros dígitos do CPF de forma aleatória usando a função `random.randint(0, 9)`.

2. **Cálculo do Primeiro Dígito Verificador**: O script calcula o primeiro dígito verificador multiplicando cada um dos nove primeiros dígitos por uma sequência decrescente de números de 10 a 2 e somando os resultados. O resto da divisão dessa soma por 11 é calculado. Se o resto for menor que 2, o primeiro dígito verificador é 0, senão, o script subtrai o resto de 11 para obter o primeiro dígito verificador.

3. **Cálculo do Segundo Dígito Verificador**: O script calcula o segundo dígito verificador multiplicando cada um dos nove primeiros dígitos, bem como o primeiro dígito verificador, por uma sequência decrescente de números de 11 a 2 e somando os resultados. O resto da divisão dessa soma por 11 é calculado. Se o resto for menor que 2, o segundo dígito verificador é 0, senão, o script subtrai o resto de 11 para obter o segundo dígito verificador.

4. **Impressão do CPF Gerado**: Finalmente, o script imprime o número de CPF gerado, que inclui os nove primeiros dígitos, seguidos pelos dois dígitos verificadores.

Por favor, note que este código é apenas para fins de estudo e aprendizado de programação. Embora ele gere números de CPF que são válidos em termos de seguir o formato correto e ter dígitos verificadores corretos, ele não verifica se o número de CPF gerado já foi atribuído a um indivíduo pela Receita Federal do Brasil. Além disso, é ilegal usar um número de CPF gerado artificialmente para fins fraudulentos.