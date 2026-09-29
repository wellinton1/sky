"""Audita a saúde do perfil público do GitHub e do repo local.

Requer apenas dados públicos (sem token) para o usuário, mas aceita
GITHUB_TOKEN para elevar o rate limit da API.

Uso:
    python tools/badges.py
    GITHUB_TOKEN=seu_token python tools/badges.py
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request

API = "https://api.github.com"
USER = os.environ.get("GITHUB_USER", "wellinton1")
REPO = os.environ.get("GITHUB_REPO", "sky")
TIMEOUT = 15


def _headers() -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "sky-badge-audit",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def get(path: str) -> dict:
    req = urllib.request.Request(f"{API}{path}", headers=_headers())
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        print(f"erro HTTP {exc.code} em {path}", file=sys.stderr)
    except urllib.error.URLError as exc:
        print(f"erro de rede em {path}: {exc.reason}", file=sys.stderr)
    return {}


def report(label: str, ok: bool, detail: str = "") -> None:
    mark = "OK  " if ok else "FALTA"
    suffix = f"  ({detail})" if detail else ""
    print(f"[{mark}] {label}{suffix}")


def main() -> int:
    print(f"auditando {USER}/{REPO}\n")

    profile = get(f"/users/{USER}")
    if not profile:
        print("nao foi possivel ler o perfil. verifique usuario/conexao.")
        return 1

    report("perfil encontrado", bool(profile.get("login")), profile.get("name", ""))

    repo = get(f"/repos/{USER}/{REPO}")
    if not repo:
        print(f"\nrepo {USER}/{REPO} ainda nao existe no GitHub.")
        print("crie em https://github.com/new e depois rode este script de novo.")
        return 0

    report("descricao", bool(repo.get("description")), repo.get("description", ""))
    report("topics", len(repo.get("topics") or []) > 0, ", ".join(repo.get("topics") or []))
    report("licenca detectada", repo.get("license") is not None,
           (repo.get("license") or {}).get("spdx_id", ""))
    report("nao e fork", not repo.get("fork"))
    report("publico", not repo.get("private"))

    readme = get(f"/repos/{USER}/{REPO}/readme")
    report("README", bool(readme), readme.get("name", ""))

    releases = get(f"/repos/{USER}/{REPO}/releases?per_page=1")
    report("tem release publicada", isinstance(releases, list) and len(releases) > 0)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
