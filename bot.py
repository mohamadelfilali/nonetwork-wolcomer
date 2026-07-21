import os
import discord

# ── Bot setup ─────────────────────────────────────────────────────────────────

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

WELCOME_CHANNEL_ID = 1511119087051473137
LEAVE_CHANNEL_ID   = 1529202684723331102

WELCOME_IMAGE_URL = (
    "https://i.postimg.cc/tRwLbR4w/Gemini-Generated-Image-ckchgfckchgfckch.webp"
)


# ── Helper: ordinal string ─────────────────────────────────────────────────────

def ordinal(n: int) -> str:
    """Convert an integer to its English ordinal string (e.g. 1 -> '1st')."""
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


# ── Events ────────────────────────────────────────────────────────────────────

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")


# ── Welcome ───────────────────────────────────────────────────────────────────

@client.event
async def on_member_join(member: discord.Member):
    channel = client.get_channel(WELCOME_CHANNEL_ID)
    if channel is None:
        print(f"[welcome] Could not find channel {WELCOME_CHANNEL_ID}")
        return

    guild          = member.guild
    ordinal_count  = ordinal(guild.member_count)

    embed = discord.Embed(
        title="✨ Welcome to NONETWORK",
        description=(
            f"We are glad to have you on board! "
            f"You are officially the **{ordinal_count}** member of our network.\n\n"
            f"> **📜 Essential Guidelines**\n"
            f"> Please proceed to <#1511119087051473137> and review the rules "
            f"to ensure a safe and seamless experience for everyone."
        ),
        color=7340287,
    )

    embed.set_thumbnail(url=member.display_avatar.url)
    embed.set_image(url=WELCOME_IMAGE_URL)

    guild_icon_url = guild.icon.url if guild.icon else None
    embed.set_footer(
        text="Jakles MC • Network Operations",
        icon_url=guild_icon_url,
    )

    await channel.send(
        content=f"Welcome <@{member.id}> ! 🌌",
        embed=embed,
    )


# ── Farewell ──────────────────────────────────────────────────────────────────

@client.event
async def on_member_remove(member: discord.Member):
    channel = client.get_channel(LEAVE_CHANNEL_ID)
    if channel is None:
        print(f"[farewell] Could not find channel {LEAVE_CHANNEL_ID}")
        return

    guild = member.guild

    embed = discord.Embed(
        title="🌒 Farewell from NONETWORK",
        description=(
            f"**{member.name}** has left the server.\n"
            f"We now have **{guild.member_count}** members remaining in our network."
        ),
        color=3552822,
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    guild_icon_url = guild.icon.url if guild.icon else None
    embed.set_footer(
        text="Jakles MC • Network Operations",
        icon_url=guild_icon_url,
    )

    await channel.send(
        content=f"Goodbye **{member.name}**... 👋",
        embed=embed,
    )


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError(
            "DISCORD_TOKEN environment variable is not set. "
            "Set it before running the bot."
        )
    client.run(token)
