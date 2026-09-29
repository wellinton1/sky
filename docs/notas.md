# Notas

Registro de uso do repositório.

## Como rodar a auditoria

```bash
python tools/badges.py
```

O script consulta apenas a API publica do GitHub. Com `GITHUB_TOKEN` definido
o rate limit da API sobe de 60 para 5000 requisicoes por hora.
