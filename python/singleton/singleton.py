class Singleton:

    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls._instance = super(Singleton, cls).__new__(cls)
            # Initialize the instance here
        return cls.__instance


if __name__ == '__main__':
    # Create the first instance
    s1 = Singleton()

    # Create the second instance
    s2 = Singleton()

    # Check if the two instances are the same
    print(s1 is s2)     # True

    # Print the memory address of the two instances
    print(hex(id(s1)))  # Something like 0x7f9b0c0c0a90
    print(hex(id(s2)))  # Should be the same as above
