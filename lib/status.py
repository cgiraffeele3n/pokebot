import math


class Status:


    def muhosei(self, syuzokuchi):
        return math.floor(((syuzokuchi*2 + 31 + 252/4) * 50/100 + 5) * 1.0)

    def hosei(self, syuzokuchi):
        return math.floor(((syuzokuchi*2 + 31 + 252/4) * 50/100 + 5) * 1.1)

    def mufuri(self, syuzokuchi):
        return math.floor(((syuzokuchi*2 + 31) * 50/100 + 5) * 1.0)
