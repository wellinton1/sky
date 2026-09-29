# sky

Repositório de experimenting do usuário **[@wellinton1](https://github.com/wellinton1)**.

## Propósito

Espaço pessoal de projetos, ferramentas e anotações técnicas. Foco em
documentação clara, testes automatizados e mudanças pequenas e revisáveis.

## Estrutura

```
sky/
├── .github/
│   ├── ISSUE_TEMPLATE/bug_report.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/ci.yml
├── docs/
│   └── notas.md
├── tests/
│   └── test_badges.py
├── tools/
│   └── badges.py
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── SECURITY.md
```

## Ferramentas

### `tools/badges.py`

Audita a saúde do perfil público e do repositório via API do GitHub.

```bash
python tools/badges.py
```

Variáveis opcionais: `GITHUB_USER`, `GITHUB_REPO`, `GITHUB_TOKEN`.
Com token, o rate limit da API sobe de 60 para 5000 requisições/hora.

### Testes

```bash
python -m unittest discover -s tests -v
```

A CI roda o mesmo comando em cada push e em cada Pull Request.

## Contribuindo

Leia [CONTRIBUTING.md](CONTRIBUTING.md). Resumo: issue antes do código, branch
descritivo, Conventional Commits, e pelo menos uma aprovação antes do merge.

Para reportar vulnerabilidades, use o canal privado descrito em
[SECURITY.md](SECURITY.md) — nunca issue pública.

## Licença

MIT — ver [LICENSE](LICENSE).
