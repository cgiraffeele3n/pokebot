import math


class status:


    def muhosei(self, syuzokuti):
        return math.floor(((syuzokuchi*2 + 31 + 252/4) * 50/100 + 5) * 1.0)

    def hosei(self, syuzokuti):
        return math.floor(((syuzokuchi*2 + 31 + 252/4) * 50/100 + 5) * 1.1)

    def mufuri(self, syuzokuti):
        return math.floor(((syuzokuchi*2 + 31) * 50/100 + 5) * 1.0)
