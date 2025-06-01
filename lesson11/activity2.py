class computer:
    def __init__(self):
        self.__price=1000
    def sell(self):
        print("selling price: {}".format(self.__price))
    def maxprice(self,maxprice):
        self.__price=maxprice
c=computer()
c.sell()
c.__price=2000
c.sell()
c.maxprice(2000)
c.sell()