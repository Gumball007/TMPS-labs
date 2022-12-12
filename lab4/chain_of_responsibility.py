from abc import ABC, abstractmethod


# interface for handlers
class Handler(ABC):
    @abstractmethod
    def set_next_handler(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


# abstract class for concrete handlers
class AbstractHandler(Handler, ABC):
    _next_handler = None
    _can_take_to_club = False

    def set_next_handler(self, handler: Handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class Friend(AbstractHandler):
    def handle(self, request):
        if self._can_take_to_club:
            return 'Friend took you to the club!'
        else:
            print('Friend can\'t take you to the club. But he can speak to club member with connections')
            return super().handle(request)


class ClubMember(AbstractHandler):
    def handle(self, request):
        if self._can_take_to_club:
            return 'Club member with connections took you to the club!'
        else:
            print("Club member with connections can't take you to the club. He can speak to vice president of the club")
            return super().handle(request)


class VicePresident(AbstractHandler):
    _can_take_to_club = True

    def handle(self, request):
        if self._can_take_to_club:
            return 'Vice president took you to the club!'
        else:
            return super().handle(request)


class President(AbstractHandler):
    _can_take_to_club = True

    def handle(self, request):
        if self._can_take_to_club:
            return 'President took you to the club!'
        else:
            return super().handle(request)


# client code to start with the first handler in chain
def client_code_friend(handler):
    request = 'Take me to the club'
    result = handler.handle(request)
    return result


# client code to start with the last handler in chain
def client_code_president(handler):
    request = 'Take me to the club'
    result = handler.handle(request)
    return result


def main():
    # create handlers
    friend = Friend()
    club_member = ClubMember()
    vice_president = VicePresident()
    president = President()

    # building chain of responsibilities
    friend.set_next_handler(club_member).set_next_handler(vice_president).set_next_handler(president)

    print('Ask first handler in chain')
    chain = client_code_friend(friend)
    print(chain)
    print('')

    print('Ask last handler in chain')
    last_handler = client_code_president(president)
    print(last_handler)


if __name__ == '__main__':
    main()