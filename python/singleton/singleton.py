class BaseSingleton:

    def __init__(self):
        print("BaseSingleton.__init__")


class Singleton(BaseSingleton):

    __instance = None

    def __init__(self):
        print("Singleton.__init__, do nothing")     # This method might be called multiple times

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls)
            super(Singleton, cls.__instance).__init__()
            # Initialize the instance here
            cls.__instance.__message = "Hello, world!"
        return cls.__instance

    def get_message(self):
        return self.__message


if __name__ == '__main__':
    # Create the first instance
    s1 = Singleton()

    # Create the second instance
    s2 = Singleton()

    print(s1.get_message())
    print(s2.get_message())

    # Check if the two instances are the same
    print(s1 is s2)     # True

    # Print the memory address of the two instances
    print(hex(id(s1)))  # Something like 0x7f9b0c0c0a90
    print(hex(id(s2)))  # Should be the same as above
