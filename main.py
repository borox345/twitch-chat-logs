# Main package
from twitchio.ext import commands

# Libraries
import asyncio
# Config
import config
# Other
import random
# Modules
from modules.logs import log

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=config.TOKEN, prefix=config.BOT_PREFIX, initial_channels=config.INITIAL_CHANNELS)
        self.saving = False
        self.file = ""
        self.lp = 0

    async def event_ready(self):
        log('client', f'Client {self.nick} is ready.')
        # Ich bin froh, wenn du es nicht entfernen wirst :)
        log('client', f'Created by borox | https://github.com/borox345')

    async def event_message(self, message):
        if message.echo:
            return
        
        await self.handle_commands(message)

        if self.saving == True:
            self.lp += 1
            with open(f"{self.file}.txt", 'a') as f:
                f.write(f'{self.lp}. {message.content} - {message.author.name}\n')
                f.close()

 
    @commands.command(name='read')
    async def read(self, ctx: commands.Context, minutes: int = 1):
        gn = random.randint(0,100)
        self.file = f"readmessages{gn}"
        await ctx.send(f'Starting reading messages.')
        f = open(f"{self.file}.txt", "w")
        self.saving = True
        await asyncio.sleep(minutes * 60)
        self.lp = 0
        self.saving = False


        
if __name__ == "__main__":
    bot = Bot()
    bot.run()
