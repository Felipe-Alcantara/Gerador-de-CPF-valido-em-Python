# 🔧 Correção de Problemas de Encoding no GitHub Pages

## 🐛 Problema Identificado

Caracteres acentuados (á, é, í, ó, ú, ã, õ, ç) aparecem corrompidos no GitHub Pages, mas funcionam localmente.

**Exemplo:**
- Local: "Dígito" ✅
- GitHub Pages: "DÃ­gito" ❌

## ✅ Soluções Aplicadas

### 1. Declaração UTF-8 no Python
Adicionado no início de `gerador.py`:
```python
# -*- coding: utf-8 -*-
```

### 2. Meta Tag HTTP Explícita no HTML
Adicionado em `index.html`:
```html
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
```

### 3. Charset no Script Python
Modificado em `index.html`:
```html
<script type="text/python" src="gerador.py" charset="utf-8"></script>
```

### 4. Arquivo .htaccess
Criado `docs/.htaccess` para forçar UTF-8 no servidor.

### 5. Configuração GitHub Pages
Criado `docs/_config.yml` para Jekyll.

## 🚀 Como Testar

### Teste 1: Verificar Encoding dos Arquivos
```bash
# Windows (PowerShell)
Get-Content gerador.py -Encoding UTF8

# Verificar se não há BOM
$bytes = [System.IO.File]::ReadAllBytes("gerador.py")
$bytes[0..2]  # Deve mostrar o conteúdo, não EF BB BF
```

### Teste 2: Commit e Push
```bash
git add docs/
git commit -m "fix: Corrige encoding UTF-8 para GitHub Pages"
git push origin main
```

### Teste 3: Aguardar Deploy
- Aguarde 2-5 minutos
- Acesse o GitHub Pages
- Force refresh: `Ctrl+F5` ou `Cmd+Shift+R`

## 🔍 Diagnóstico Adicional

Se o problema persistir, verifique:

### 1. VS Code está salvando em UTF-8?
Verifique no canto inferior direito do VS Code:
- Deve mostrar "UTF-8"
- Se mostrar "UTF-8 with BOM", mude para "UTF-8"

**Como mudar:**
1. Clique em "UTF-8" no canto inferior direito
2. Selecione "Save with Encoding"
3. Escolha "UTF-8" (sem BOM)

### 2. Git está preservando o encoding?
Adicione ao `.gitattributes` na raiz:
```
*.py text eol=lf encoding=utf-8
*.html text eol=lf encoding=utf-8
*.css text eol=lf encoding=utf-8
*.js text eol=lf encoding=utf-8
```

### 3. Cache do Navegador
Limpe o cache:
- Chrome: `Ctrl+Shift+Delete`
- Firefox: `Ctrl+Shift+Delete`
- Ou use modo anônimo

## 📝 Checklist de Correção

- [x] Adicionar `# -*- coding: utf-8 -*-` no Python
- [x] Adicionar meta tag HTTP no HTML
- [x] Adicionar charset no script tag
- [x] Criar .htaccess
- [x] Criar _config.yml
- [ ] Salvar todos os arquivos como UTF-8 (sem BOM)
- [ ] Commit e push
- [ ] Aguardar deploy (2-5 min)
- [ ] Testar com Ctrl+F5

## 🎯 Solução Alternativa (Se tudo falhar)

Se nada funcionar, converta caracteres especiais para HTML entities:

```python
# Antes:
"Dígito"

# Depois:
"D&iacute;gito"
```

**Tabela de Conversão:**
- á → `&aacute;`
- é → `&eacute;`
- í → `&iacute;`
- ó → `&oacute;`
- ú → `&uacute;`
- ã → `&atilde;`
- õ → `&otilde;`
- ç → `&ccedil;`
- º → `&ordm;`

## 📞 Suporte Adicional

Se o problema persistir após todas essas correções:

1. Verifique os logs do GitHub Pages
2. Teste com outro navegador
3. Verifique se o GitHub Actions está funcionando
4. Considere usar GitHub Actions para build customizado

## ✅ Resultado Esperado

Após aplicar as correções:
- ✅ "Dígito" deve aparecer corretamente
- ✅ "Região" deve aparecer corretamente
- ✅ "1º verificador" deve aparecer corretamente
- ✅ "2º verificador" deve aparecer corretamente
- ✅ Todos os acentos devem funcionar

---

**Nota:** GitHub Pages pode levar até 10 minutos para atualizar após um push.
