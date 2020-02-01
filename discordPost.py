import discord
import random
import os
from lib import csvwrapper
from lib import status

# トークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

getCsv = './csv/poke.csv'

# CsvWrapperインスタンス
csv = csvwrapper.CsvWrapper()

# statusインスタンス
status = status.Status()

# ステータスcsvファイルの読み込み
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
        await message.channel.send("$:ポケモンを完全一致で検索し該当する種族値を表示")
        await message.channel.send("$?:ポケモンを部分一致で検索し該当する種族値をすべて表示")
        await message.channel.send("$S:ポケモンの素早さを無振り、無補正、補正で表示")
        await message.channel.send("/pass:[0-9]の４ケタのランダムなパスワードの生成")

    # ランダムパスワード生成
    if message.content == "/pass":
        await message.channel.send(str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)))

    # $[ポケモン名]と一致する種族値を返す(部分一致)
    if message.content.startswith("$?", 0):
        for row in readcsv:
            if message.content.lstrip("$?") in row[0]:
                await message.channel.send(row[0] + ":" + row[1] + "-" + row[2] + "-" + row[3] + "-" + row[4] + "-" + row[5] + "-" + row[6])

    # $[ポケモン名]と一致する種族値を返す(完全一致)
    if message.content.startswith("$", 0):
        for row in readcsv:
            if message.content == "$" + row[0]:
                await message.channel.send(row[0] + ":" + row[1] + "-" + row[2] + "-" + row[3] + "-" + row[4] + "-" + row[5] + "-" + row[6])

    # $[ポケモン名]と一致する素早さステータスを返す
    if message.content.startswith("$S", 0):
        for row in readcsv:
            if message.content == "$S" + row[0]:
                intRow = int(row[6])
                await message.channel.send(row[0] + "の素早さは")
                await message.channel.send(status.kotaichiZero(intRow) + "（個体値0、下降補正）")
                await message.channel.send(status.mufuri(intRow))
                await message.channel.send(status.muhosei(intRow))
                await message.channel.send(status.hosei(intRow))

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
