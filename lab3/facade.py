class Raw:
    def raw(self):
        print('buy raw food ...')

class Transfer:
    def teransfer(self):
        print('transfer food to restutant')

class Cook:
    def cook(self):
        print('cook food by cheif')

class ItalianResturant:
    def get(self):
        r = Raw()
        r.raw()

        t = Transfer()
        t.teransfer()

        c = Cook()
        c.cook()

def order():
    i = ItalianResturant()
    i.get()

order()