# インストールした discord.py を読み込む
import discord
import random
import os
from lib import csvwrapper

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NjcyMDI3OTE4NzU0NTEyODk2.XjLEaQ.pk_FOYmDs0EicrFKbkOHVsit0oU'

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
    if message.content.startswith("$?", 0):
        for row in readcsv:
            if message.content.lstrip("$?") in row[0]:
                await message.channel.send(row[0] + ":" + row[1] + "-" + row[2] + "-" + row[3] + "-" + row[4] + "-" + row[5] + "-" + row[6])

    for row in readcsv:
        if message.content == "$" + row[0]:
            await message.channel.send(row[0] + ":" + row[1] + "-" + row[2] + "-" + row[3] + "-" + row[4] + "-" + row[5] + "-" + row[6])

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
