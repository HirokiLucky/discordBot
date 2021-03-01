import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODEzMDM0MDYwMDQ1MDkwODQ2.YDJa-Q.wKFZ2_wyGoWHg-Mym6h1wQS7DHg'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 返信する非同期関数を定義
async def reply(message):
    reply0 = f'{message.author.mention} 呼んだ？'
    # 返信メッセージの作成
    await message.channel.send(reply0)
    # 返信メッセージを送信

# 発言時に実行されるイベントハンドラを定義
@client.event
async def on_mention(message):
    if client.user in message.mentions:
        # 話しかけられたかの判定
        await reply(message)
        # 返信する非同期関数を実行

client.run(TOKEN)