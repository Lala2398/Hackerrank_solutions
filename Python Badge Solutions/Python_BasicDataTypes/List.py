if __name__ == '__main__':
    # Read the number of commands
    N = int(input())

    # Initialize an empty list
    array = []

    # Loop through the number of commands
    i = 0
    while i < N:
        i += 1

        # Split the command input into a list
        numbers = input().split()

        # Check if the command is 'print'
        if numbers[0] == 'print':
            # Print the current list
            print(array)
        else:
            # Assume it's another command and extract arguments
            command, *args = numbers  # Unpack command and arguments

            # Use getattr to call the method on the list with arguments
            getattr(array, command)(*[int(i) for i in args])
            
            #arr.append(value)) #you`ll use instead of getattr 

        # Increment loop counter
