if __name__ == '__main__':
    #Get the number
    n = int(input())
    # Read integers (using map for convenient way to apply a function like int and it creates an iterator too)
    integer = map(int, input().split())
    # Create a tuple
    tuple=tuple(integer)
    # hash of tuple (hash: Returns the hash value of a specified object)
    print(hash(tuple))
