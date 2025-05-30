# Padrões do projeto
autore: Michel, Everton

versão: 1.0.0

data: 2025-05-30


# Exemplo inspirado em ifbemnumeros.ifb.edu.br


# ícones
Ícones Bootstrap: A maneira mais fácil e recomendada é usar os ícones do Bootstrap. Você pode encontrá-los no site oficial do Bootstrap Icons: https://icons.getbootstrap.com/. Basta usar o nome do ícone sem o prefixo bi-. Por exemplo, para o ícone de casa, use "house" (e não "bi-house").

# projeto
## Estrutura do projeto
A estrutura do projeto deve seguir o seguinte padrão:

```python
seu_projeto/
├── app.py         (page principal)
└── pages/
    └── inicio.py  (page "Início")
    └── ensino.py  (pege "Ensino", e assim por diante)
    └── ...
    └── padrao.py  (página de padrões do projeto)
```