class History:
    def all_history(self):
        print('print all articles')


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def check_staff_password(self):
        if self.username == 'admin' and self.password == 'password':
            return True

def outer(Func):
    def inner():
        username = input('Please enter your username: ')
        password = input('Please enter your password: ')
        log = Login(username,password)
        res = log.check_staff_password()
        if res:
            Func()
        else:
            print('Sorry, you don\'t have access')
    return inner

@outer
def show_all_history():
    articles = History()
    articles.all_history()

show_all_history()