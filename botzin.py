import os

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("DISCORD_GUILD_ID")

if not TOKEN or TOKEN == "cole_o_token_aqui":
    raise SystemExit("Faltou o token. Copie .env.example para .env e cole o DISCORD_TOKEN.")
def guild_object():
    if GUILD_ID and GUILD_ID.isdigit():
        return discord.Object(id=int(GUILD_ID))
    return None


intents = discord.Intents.default()


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self) -> None:
        # setup_hook roda uma vez na inicialização.
        # Sync em on_ready é ruim: o Discord pode limitar se reconectar.
        target = guild_object()
        if target:
            self.tree.copy_global_to(guild=target)
            synced = await self.tree.sync(guild=target)
            print(f"Comandos sincronizados no servidor de testes: {len(synced)}")
        else:
            synced = await self.tree.sync()
            print(f"Comandos sincronizados globalmente: {len(synced)}")
            print("Sem DISCORD_GUILD_ID, o /ping pode demorar até 1 hora para aparecer.")


bot = Bot()


@bot.event
async def on_ready():
    print(f"Online como {bot.user} (id: {bot.user.id})")
    print("No Discord, digite /ping")


@bot.tree.command(name="ping", description="Testa se o bot está online")
async def ping(interaction: discord.Interaction):
    latency_ms = round(bot.latency * 1000)
    await interaction.response.send_message(f"Pong! Latência: {latency_ms} ms")


@bot.tree.command(name="oi", description="O bot te cumprimenta")
@app_commands.describe(nome="Seu nome (opcional)")
async def oi(interaction: discord.Interaction, nome: str | None = None):
    quem = nome or interaction.user.display_name
    await interaction.response.send_message(f"Oi, {quem}! 👋")


@bot.tree.error
async def on_app_command_error(
    interaction: discord.Interaction, error: app_commands.AppCommandError
):
    if interaction.response.is_done():
        await interaction.followup.send("Deu erro nesse comando.", ephemeral=True)
    else:
        await interaction.response.send_message(
            "Deu erro nesse comando.", ephemeral=True
        )
    print(f"Erro no comando: {error}")


if __name__ == "__main__":
    bot.run(TOKEN)
