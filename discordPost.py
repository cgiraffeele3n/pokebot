import discord
import random

from lib import csvwrapper

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NjY4Nzg5NjUxODM3OTQzODM3.XiWZaQ.0saCyb48zhEBl5y9GKs8xU-9AXs'

# 接続に必要なオブジェクトを生成
client = discord.Client()

getCsv = './csv/poke.csv'

csv = csvwrapper.CsvWrapper()

readcsv = csv.readCsv(getCsv)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    print('stop to ctrl + z')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

     # マニュアルの表示
    if message.content == "/help":
        await message.channel.send("$ポケモン名で種族値を返します")
        await message.channel.send("/passでランダムなパスワードの生成")

    # ランダムパスワード生成
    if message.content == "/pass":
        await message.channel.send(str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)))

    # $[ポケモン名]と一致する種族値を返す
    for row in readcsv:
        if message.content == "$" + row[0]:
            await message.channel.send(row[1] + "-" + row[2] + "-" + row[3] + "-" + row[4] + "-" + row[5] + "-" + row[6] + ":" + row[7])
            return

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
