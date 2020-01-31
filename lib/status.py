import math


class status:


"""
無補正のステータス実数値を返す
"""


def muhosei(self, syuzokuti):
    return math.floor(((syuzokuchi*2 + 31 + 252/4) * 50/100 + 5) * 1.0)


"""
補正のステータス実数値を返す
"""


def hosei(self, syuzokuti):
    return math.floor(((syuzokuchi*2 + 31 + 252/4) * 50/100 + 5) * 1.1)


"""
無振りのステータスを返す
"""


def mufuri(self, syuzokuti):
    return math.floor(((syuzokuchi*2 + 31) * 50/100 + 5) * 1.0)
