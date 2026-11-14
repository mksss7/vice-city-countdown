
import discord
import asyncio
from datetime import datetime, timezone

TOKEN = "TU_TOKEN_AQUI"
CHANNEL_ID = 0  # ID de tu canal de cuenta atrás

# Lanzamiento GTA VI: 19 noviembre 2026
TARGET = datetime(2026, 11, 19, 0, 0, tzinfo=timezone.utc)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Conectado como {client.user}")
    channel = client.get_channel(CHANNEL_ID)

    if channel is None:
        print("No encuentro el canal. Comprueba CHANNEL_ID.")
        return

    message = await channel.send("🌴 Preparando Vice City...")

    while datetime.now(timezone.utc) < TARGET:
        remaining = TARGET - datetime.now(timezone.utc)

        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes = remainder // 60

        embed = discord.Embed(
            title="🌴 GRAND THEFT AUTO VI",
            description="**WELCOME TO VICE CITY**\n\n"
                        f"💗 **{days} DÍAS**\n"
                        f"💙 **{hours} HORAS**\n"
                        f"💜 **{minutes} MINUTOS**",
            color=0xFF55B8
        )
        embed.set_footer(text="VICE CITY HUB • 19 NOVIEMBRE 2026")

        await message.edit(content=None, embed=embed)
        await asyncio.sleep(60)

    await message.edit(content="🌴 **GTA VI YA ESTÁ AQUÍ. WELCOME TO VICE CITY!**")

client.run(TOKEN)
