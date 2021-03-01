import discord
import urllib.request
import json
import re

client = discord.Client()

citycode = '140010'
resp = urllib.request.urlopen('https://weather.tsukumijima.net/api/forecast/city/%s'%citycode).read()
resp = json.loads(resp.decode('utf-8'))

@client.event
async def on_ready():
  print(client.user.name + "はログインしました")

@client.event
async def on_message(message):
  if message.author != client.user:
    if message.content == "!weather":
      msg = resp['location']['city']
      msg += "の天気は、\n"
      for f in resp['forecasts']:
          if f['telop'] == None:
            break

          msg += "{0[dateLabel]}は{0[telop]}\n".format(f)
      msg += "です。\n"
      for m in resp['forecasts']:
          msg2 = "※現在の日付" + m['date'] + "\n\n"
          break
      msg3 = resp['description']['text']
      await message.channel.send(msg + msg2 + msg3)

client.run("ODEzMDMxNDgxMDc3MTM3NDE4.YDJYkg.1ENc0WcfMTCfZWK58j7JIJoR91o")