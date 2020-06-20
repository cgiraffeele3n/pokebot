# pokebot
このツールはDiscord用Bot「pokebot」です
ポケモンの種族値の検索と
ウッウロボのレシピ検索が行えます。
***
## ・コマンド
### $ポケモン名
完全一致したポケモンの種族値を表示します
例）$ロトム
>ロトム:50-50-77-95-77-91

### $?ポケモン名
部分一致したポケモン名を表示します
例）$?ロトム
>ロトム:50-50-77-95-77-91
>ロトム（ヒート）:50-65-107-105-107-86
>ロトム（ウォッシュ）:50-65-107-105-107-86
>ロトム（フロスト）:50-65-107-105-107-86
>ロトム（スピン）:50-65-107-105-107-86
>ロトム（カット）:50-65-107-105-107-86

### $Sポケモン名
完全一致したポケモンの素早さを、無振り、無補正、補正で表示します
例）$Sロトム
>ロトムの素早さは
>86（個体値0、下降補正）
>111（個体値31、無補正）
>143（個体値31、努力値252、無補正）
>157（個体値31、努力値252、上方補正）

### ¥uuアイテム名
完全一致したアイテムを合成するのに必要な素材を表示します
例） ¥uuきんのおうかん
>[ぎんのおうかん:ぎんのおうかん:ぎんのおうかん:ぎんのおうかん]->きんのおうかん