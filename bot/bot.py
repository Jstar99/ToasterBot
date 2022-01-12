from pathlib import path

import discord 
from discord.ext import commands

class MusicBot(commands.Bot):
  def __init__(self):
    self.cogs =[p.stem for p in Path(".").glob("./bot/cogs/*py")]
    super().__init__(commands_prefix, case_sensitive=True)

    def setup(self):
      print("Running setup...")

      for cog in self._cogs:
        self.load_extention(f"bot.cogs.{cog}")

    