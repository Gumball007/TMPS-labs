# Singleton pattern

class ChocolateBoiler:
    instance = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        if not ChocolateBoiler.instance:
            ChocolateBoiler.instance = ChocolateBoiler.__ChocolateBoiler()
        return ChocolateBoiler.instance

    class __ChocolateBoiler:

        def __init__(self):
            self.empty = True
            self.boiled = False

        def fill(self):
            if self.empty:
                self.empty = False
                self.boiled = False

        def drain(self):
            if not self.empty and self.boiled:
                self.empty = True

        def boil(self):
            if not self.empty and not self.boiled:
                self.boiled = True

