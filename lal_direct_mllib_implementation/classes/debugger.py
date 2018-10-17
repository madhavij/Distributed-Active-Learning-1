

class Debugger:
    def __init__(self):
        self.debugCount = 1
        self.items = []


    def DEBUG(self, arg):
        print('-----------------------  DEBUG no. # ',self.debugCount ,' --------------------------------------------------------------------------------\n')
        print(arg)
        print('\n\n\\n---------------------------------------------------------------------------------------------------------------------------------------')
        print('########################################################################################################################')
        print('########################################################################################################################')
        print('########################################################################################################################')
        print('########################################################################################################################\n\n')
        self.debugCount +=1

    def add(self, items):
        self.items = items
        for x in self.items:
            self.DEBUG(x)
