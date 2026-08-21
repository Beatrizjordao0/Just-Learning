# Verbo Janga — protótipo de escala

Protótipo Flask/MySQL para cadastro de participantes e registro de dias indisponíveis, migrado do antigo repositório `Verbo-Janga`.

A migração removeu a senha de banco que estava gravada no código, passou a usar variáveis de ambiente e armazenar senhas de usuários com hash.

## Executar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
mysql -u root -p < schema.sql
python app.py
```

No Windows, ative o ambiente com `.venv\Scripts\activate`. Ajuste o arquivo `.env` com os dados do seu MySQL; ele não deve ser enviado ao Git.
