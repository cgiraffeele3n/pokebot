import math


class Status:

    """
    個体値31
    のステータスを返す
    """

    def kotaichiZero(self, syuzokuchi):
        return str(math.floor(((syuzokuchi*2) * 50/100 + 5) * 1.0))

    """
    個体値31
    のステータスを返す
    """

    def mufuri(self, syuzokuchi):
        return str(math.floor(((syuzokuchi*2 + 31) * 50/100 + 5) * 1.0))

    """
    個体値31
    努力値252
    正確補正1.0
    のステータス実数値を返す
    """

    def muhosei(self, syuzokuchi):
        return str(math.floor(((syuzokuchi*2 + 31 + 252/4) * 50/100 + 5) * 1.0))

    """
    個体値31
    努力値252
    正確補正1.1
    のステータス実数値を返す
    """

    def hosei(self, syuzokuchi):
        return str(math.floor(((syuzokuchi*2 + 31 + 252/4) * 50/100 + 5) * 1.1))
