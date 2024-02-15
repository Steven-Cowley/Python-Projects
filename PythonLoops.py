def forLoopExample():
    # define an empty string
    result = ""
    # define the for loop for i is in the range of 1 through 6 (1 through 5)
    for i in range(1, 6):
        # result then becomes a string that has current number is and then what i is which is 1 through 5
        result += f"current number is {i}\n"
    # return the current number to the user
    return result

def whileLoopExample():
    result = ""
    # define a varaible that acts as our input
    count = 1
    # define while count is below to equal 5
    while count <= 5:
        # result then equals what the count is
        result += f"current while loop number is {count}\n"
        # count + 1 until count is 5 then the loop stopes
        count += 1
    # return the current number to the user
    return result

def loopInput(lowerLimit, upperLimti):
    result = ""
    for i in range(lowerLimit, upperLimti):
        result += f"current Input number is {i}\n"
    return result


# calls the functions
print(forLoopExample())
print(whileLoopExample())

lower = int(input("what is the lower limit "))
upper = int(input("what is the upper limit "))
print(loopInput(lower, upper))