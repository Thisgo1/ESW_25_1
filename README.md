# Requisitos do Projeto Feiras

## Funcionais
- O sistema deve permitir criar, listar, atualizar e excluir feiras.
- Cada feira pode ter múltiplos expositores.
- Cada expositor pode ter múltiplos produtos.
- Usuários devem criar uma conta e autenticar para fazer operações de escrita.
- Cada ingresso está associado a uma feira e data.

## Não funcionais
- Segurança na autenticação.
- Performance adequada para até 1000 usuários simultâneos.
- Interface responsiva (se houver front-end).

# Sistema de Feiras - Documentação Técnica

## 🚀 Como Utilizar o Sistema

### ▶️ Executar a Aplicação
```bash
# Opção 1: Via Makefile
make run

# Opção 2: Direto pelo Python
python app.py

# A aplicação estará disponível em:
http://localhost:5000
```

### 📄 Gerar Documentação
```bash
# Comando completo
make doc

# Arquivos gerados:
./docs/app.html          # Documentação principal
./docs/modules.html      # Índice de módulos
```

### 👀 Visualizar Documentação
```bash
# Servidor local (recomendado)
python3 -m http.server 8000 --directory docs/

# Acessar no navegador:
http://localhost:8000/app.html

# Alternativas diretas:
xdg-open docs/app.html   # Linux
open docs/app.html       # Mac
start docs/app.html      # Windows
```

## 🛠️ Comandos Adicionais

### 🔄 Atualizar Documentação
```bash
make clean-doc  # Remove documentação antiga
make doc        # Gera nova documentação
```

### 🧹 Limpar Ambiente
```bash
make clean      # Remove arquivos temporários
```

## 📊 Estrutura da Documentação

O arquivo `app.html` contém:
```
1. Funções Principais
   - create_app()
   - list_routes()

2. Classes e Modelos
   - Feira
   - Expositor

3. Rotas Disponíveis
   - /feiras [GET, POST]
   - /routes [GET]
```

## ❗ Solução de Problemas Comuns

| Problema               | Solução                          |
|------------------------|----------------------------------|
| Documentação desatualizada | `make clean-doc && make doc` |
| Erros na geração       | Verifique requirements.txt       |
| Rotas não aparecendo   | Confira app.register_blueprint() |

## 🔗 Links Úteis
- [Documentação Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy Docs](https://www.sqlalchemy.org/)
- [Guia Markdown](https://www.markdownguide.org/)
