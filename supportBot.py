import os
from asyncio import events
from os import name
import nextcord
from nextcord import activity
from nextcord import embeds

from nextcord.embeds import Embed
from nextcord.ext.commands.core import check
from nextcord.shard import EventType
from nextcord.utils import get
from random import *
from datetime import *
from nextcord import channel
from time import *
from nextcord.ext import commands,tasks
from nextcord.http import Route
from nextcord import *

INTENTS = Intents.all()
client = commands.Bot(command_prefix = "None",intents=INTENTS)

def random_color():
    return randint(0x000000,0xffffff)

@client.event
async def on_ready():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nstart")
    
@client.event
async def send(message = None , embed = None):
    await client.get_channel(934793904631459870).send(message , embed=embed)

@client.slash_command(description="개발자만 사용가능")
async def 답변(inter : Interaction , id , message):
    member = utils.get(client.get_all_members(),id = int(str(id).replace(" ","")))
    await member.send(embed = Embed(title = f"**{member.name}**님, 개발자에게서 답변이 왔어요" , description=f"```\n{message}\n```" , color = random_color() ))
    await inter.response.send_message(f"답변완료\n```\n{message}\n```")

@client.event
async def on_message(message):
    try:
        if str(message.channel.type) == "private":
            if message.author.bot == False:
                embed = Embed(title = f"문의를 하실 건가요?",description = f"내용 : {message.content}",timestamp=message.created_at , color = random_color())
                try: 
                    img = str(message.attachments[0])
                    embed.set_image(url = img)
                    embed.url = img
                except: 
                    pass
                await message.channel.send(embed = embed , view = yes())
    except:
        pass

class yes(ui.View):
    @ui.button(label="네" , style=ButtonStyle.green , emoji="<:vv:905014667632594994>")
    async def yes(self , button : Button , inter : Integration):
        embed = Embed(title = "문의가 왔습니다." , description=f"{inter.message.embeds[0].description.replace('내용 : ' , '')} \n\nid : {inter.user.id}\nname:{inter.user}" , color = random_color())
        try:
            if "http" in str(inter.message.embeds[0].url):
                embed.set_image(url = str(inter.message.embeds[0].url))
        except:
            pass
        print(inter.message.embeds[0].description.replace("내용 : " , ""))
        await send(embed=embed )
        await inter.response.send_message(embed = Embed(title = "문의가 완료됐습니다" , color = random_color()))
    @ui.button(label="아니요" , style=ButtonStyle.red , emoji="<:xx:905014703577772063>")
    async def no(self , button : Button , inter : Integration):
        await inter.message.delete()

token = os.environ['BOT_TOKEN']
client.run(token)
