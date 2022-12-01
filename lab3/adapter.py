class IranSocket: # client
    _type = '2'


class Adapter: # adapter
    _socket = None
    _pinType = '3to2'

    def __init__(self, socket):
        self._socket = socket


class Fridge: # adaptee
    _adapter = None
    _pinType = '3'

    def __init__(self, adapter):
        self._adapter = adapter

    def fnFreeze(self):
        if self._adapter._pinType == self._pinType + 'to' + self._adapter._socket._type:
            print('Done...')
        else:
            print('Sorry, it is not possible...')


IS = IranSocket()
Adp = Adapter(IS)
fdg = Fridge(Adp)
fdg.fnFreeze()