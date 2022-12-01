class DB:
    def work(self):
        print('You are admin so you can work with DB')


class proxy:
    _password = 'Secret'

    def check_user_password(self, password):
        if self._password == password:
            db = DB()
            db.work()
        else:
            print('Sorry you dont have permison to access db')

p = proxy()
p.check_user_password('Secret')
p.check_user_password('Wrong_password')