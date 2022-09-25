class Clients:
# Single Responsability
    class ClientsDiscount:
        def __init__(self, customer, price):
            self.customer = customer
            self.price = price

        def get_discount(self):
            return self.price * 0.2
        
        def get_price(self):
            return self.price
        
        def get_customer(self):
            return self.customer
            
# Open-Closed Principle
    class VIPClientsDiscount(ClientsDiscount):
        def get_discount(self):
            return super().get_discount() * 2

    class VVIPClientsDiscount(VIPClientsDiscount):
        def get_discount(self):
            return super().get_discount() * 2


# Dependecy Inversion Principle
class Connector:
    def connect(self, identifier):
        print(f"{identifier} -- Connection established ... 100%")

class Staff:
    class AuthenticationStaff(): # este abstracta, nu are implementare, se comporta ca o interfata
        def __init__(self, connector: Connector, identifier):
            self.connection = connector.connect(identifier)

        def authenticate(self, credentials):
            return credentials

        def is_authenticated(self):
            pass

        def last_login(self):
            pass

    class Manager(AuthenticationStaff):
        def __init__(self, connector: Connector):
            super().__init__(connector, 'Manager')
            

    class Guardian(AuthenticationStaff):
        def __init__(self, connector: Connector):
            super().__init__(connector, 'Guardian')

    class Seller(AuthenticationStaff):
        def __init__(self, connector: Connector):
            super().__init__(connector, 'Seller')

test = Clients().ClientsDiscount("Andrei", 200)
print(test.get_customer(), " ---> ", test.get_discount(), "MDL")

test2 = Clients().VIPClientsDiscount("Ion", 200)
print(test2.get_customer(), " ---> ", test2.get_discount(), "MDL")

test3 = Clients.VVIPClientsDiscount("Andreea", 200)
print(test3.get_customer(), " ---> ", test3.get_discount(), "MDL")

print("-------------------------------")

connector = Connector()

manager = Staff().Manager(connector)
guardian = Staff().Guardian(connector)
seller = Staff().Seller(connector)

print(manager.authenticate("managerPassword"))
print(guardian.authenticate("guardianPassword"))
print(seller.authenticate("sellerPassword"))