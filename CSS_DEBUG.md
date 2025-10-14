# 🔧 Debug do CSS no GitHub Pages

## 🐛 Problema Identificado

O CSS não está carregando corretamente no GitHub Pages (elementos sem cor, sem borda, desalinhados), mas funciona localmente.

## ✅ Correções Aplicadas

### 1. Caminhos Relativos Explícitos
```html
<!-- Antes -->
<link rel="stylesheet" href="style.css">

<!-- Depois -->
<link rel="stylesheet" href="./style.css?v=2">
```

O `./` garante caminho relativo correto e `?v=2` força o navegador a recarregar (bypass de cache).

### 2. Meta Tags de Cache
Adicionado para forçar reload no GitHub Pages:
```html
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
```

## 🔍 Como Testar no GitHub Pages

### 1. Abra o DevTools (F12)
- Vá para a aba **Network** (Rede)
- Recarregue a página (F5)
- Procure por `style.css`

### 2. Verifique o Status do CSS
**Se status = 200:**
- ✅ CSS carregou corretamente
- Problema pode ser no conteúdo do CSS

**Se status = 404:**
- ❌ Arquivo não encontrado
- Problema de caminho ou deploy

**Se status = 304:**
- ⚠️ Cache do navegador
- Use Ctrl+F5 (hard refresh)

### 3. Verifique o Content-Type
Clique em `style.css` na aba Network:
- **Headers** → **Response Headers**
- `Content-Type` deve ser: `text/css`

Se aparecer `text/plain` ou outro, o servidor não reconheceu como CSS.

## 🚀 Soluções Alternativas

### Solução 1: CSS Inline (Temporário para Teste)
Se nada funcionar, teste com CSS inline para confirmar que é problema de carregamento:

```html
<head>
    <style>
        /* Cole todo o conteúdo do style.css aqui */
        * { margin: 0; padding: 0; }
        /* ... resto do CSS ... */
    </style>
</head>
```

### Solução 2: MIME Type Correto
Crie arquivo `.htaccess` na pasta `docs/`:
```apache
AddType text/css .css
<FilesMatch "\.css$">
    Header set Content-Type "text/css"
</FilesMatch>
```

### Solução 3: Renomear Arquivo
Às vezes o GitHub Pages tem problemas com arquivos específicos:
```
style.css → styles.css
```
E atualize no HTML:
```html
<link rel="stylesheet" href="./styles.css?v=2">
```

## 📊 Checklist de Debug

- [ ] Fazer commit e push das mudanças
- [ ] Aguardar 2-5 min para GitHub Pages atualizar
- [ ] Abrir em modo anônimo (sem cache)
- [ ] Abrir DevTools (F12)
- [ ] Ir na aba Network
- [ ] Recarregar página
- [ ] Verificar se `style.css` carregou (status 200)
- [ ] Verificar Content-Type = `text/css`
- [ ] Fazer Ctrl+Shift+F5 (hard refresh)

## 🎯 Comandos Git

```bash
# Adicionar mudanças
git add docs/

# Commitar
git commit -m "fix: Corrige caminhos CSS para GitHub Pages"

# Enviar
git push origin main

# Aguardar deploy (2-5 min)
```

## 🔍 URL para Testar

Depois do deploy, acesse:
```
https://felipe-alcantara.github.io/Gerador-de-CPF-valido-em-Python/
```

E abra o DevTools para verificar!

## ⚡ Quick Fix

Se estiver com pressa, adicione `?v=` com timestamp:

```html
<link rel="stylesheet" href="./style.css?v=<?php echo time(); ?>">
```

Ou simplesmente mude o número toda vez que fizer deploy:
```html
<link rel="stylesheet" href="./style.css?v=3">
<link rel="stylesheet" href="./style.css?v=4">
```

## 📝 Nota Importante

GitHub Pages usa CDN global, então pode levar até **10 minutos** para propagar mudanças em todos os servidores. Se funcionar em modo anônimo, é só aguardar.
