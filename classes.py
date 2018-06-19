class Greeter(object):

    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable

    # Instance method
    def greet(self, loud=True):
        if loud:
            print('HELLO, %s!' % self.name.upper())
        else:
            print('Hello, %s' % self.name)

    def shake_hand(self, soft=False):

        if soft:
            print('Shake hands, %s!' % self.name)
        else:
            print('Ow, %s!' % self.name)
    def bow(self, hard=True):
        if hard:
            print('greetings your majesty, %s!' % self.name)
        else:
            print('morning, %s!' % self.name)




g = Greeter('Fred')  # Construct an instance of the Greeter class
g.shake_hand()

g = Greeter('Ivy')
g.greet()
g.shake_hand()
g.bow()

g = Greeter('Daddy')
g.greet()
g.shake_hand()
g.bow()
g = Greeter('Mummy')
g.greet()
g.shake_hand()
g.bow()
g = Greeter('Emmett')
g.shake_hand()            # Call an instance method; prints "Hello, Fred"
g.shake_hand(soft=True)   # Call an instance method; prints "HELLO, FRED!"