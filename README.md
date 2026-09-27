<div align=center>
  <img src="https://skillicons.dev/icons?i=python" height="150" width="150">
</div>

<h2>Bot do Discord em Python</h2>
Projeto inicial com `discord.py` e slash commands `/ping` e `/oi`.
<h2>O que você precisa</h2>
- Python 3.10 ou mais novo
- Conta no [Discord Developer Portal](https://discord.com/developers/applications)
- Um servidor de testes onde você possa adicionar o bot

<h2>Criar o bot e pegar o token</h2>
1. Abra https://discord.com/developers/applications
2. **New Application** → escolha um nome → **Create**
3. Menu **Bot** → **Reset Token** → copie o token na hora
4. Em **Privileged Gateway Intents**, neste projeto inicial **não precisa** ligar Message Content Intent
5. Menu **OAuth2 → URL Generator**
   - Scopes: `bot` e `applications.commands`
   - Permissões: `Send Messages` e `Use Slash Commands` (ou Use Application Commands)
6. Abra o link gerado e convide o bot para o seu servidor

O token é senha. Nunca envie no chat e nunca suba o arquivo `.env` para o GitHub.

<h2>Instalar e configurar</h2>
No terminal, dentro desta pasta:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

No Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Edite o `.env`:

```
DISCORD_TOKEN=cole_o_token_aqui
DISCORD_GUILD_ID=id_do_seu_servidor
```

Como copiar o ID do servidor:

1. Discord → Configurações do usuário → Avançado → ative **Modo desenvolvedor**
2. Clique com o botão direito no ícone do servidor → **Copiar ID do servidor**

Com o `DISCORD_GUILD_ID`, o `/ping` aparece em segundos. Sem ele, o comando global pode demorar até 1 hora.

<h2> Rodar</h2>
```bash
python bot.py
```
Quando aparecer `Online como ...`, vá no Discord e digite `/ping`.

Se o comando não aparecer:

- Confirme que o bot está no servidor (ele deve estar offline/online na lista de membros)
- Confirme os scopes `bot` + `applications.commands` no convite
- Confirme o `DISCORD_GUILD_ID`
- Feche e abra o Discord, ou recarregue com Ctrl+R

<h2>Comandos inclusos</h2>
<h3>| Comando | O que faz |</h3>
|---|---|
| `/ping` | Responde pong e mostra a latência |
| `/oi` | Cumprimenta você; aceita um nome opcional |

<h2> Próximos passos</h2>
- Adicionar mais comandos no `bot.py` com `@bot.tree.command`
- Separar comandos em cogs quando o projeto crescer
- Hospedar 24h (VPS ou host de bot) para o bot não cair quando fechar o PC

<h2> Segurança</h2>
- `.env` já está no `.gitignore`
- Se o token vazar, reset no Developer Portal na hora
- Não peça permissão de Administrador sem necessidade
