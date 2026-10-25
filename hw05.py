"""
Name: Gloria Domefa
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """ Uses if statements to check whether the letter input is A, B, or C
        """
    # remove the default return and add your code
    while (True): 
        let = input("Give a single uppercase letter: ")
        if let == "A" or let == "B" or let == "C":
            return let # if the correct input is given, the function ends
        # if the input isn't one letters
        
        if (len(let) > 1):
            print("Error: it needs to be a single character.")
            continue
        # if the input isn't a letter at all
        else:
            print("Error: You provided the wrong character.")
            continue

def get_digit():
    """ Checks whether input is a single digit number within the range of 1-3
        Comment: when I added 'continue' to the if statements, the loop wouldn't end """
    # remove the default return and add your code
   # n = 0
    n = input("Give a single number character: ")
    while (n not in ["1","2","3"]):
      #  n = input("Give a single number character: ")
        # if input isn't a single digit
        if n.isdigit() == False:
            print("Error: your input should be only digits.")
    
            
        # if the input is outside of the range
        else:
            print("Error: a single digit needs to be in [1,3].")
            
        n = input("Give a single number character: ")
            
    return n


def check_pattern(letter, digit, lst):
    """ Nested conditional for loop that checks each element in st_list for
        a match with both the letter and number input"""
    # remove the default pass and add your code
    # loop over each word
    # loop over each number
    match = []
    # goes through each element of the list
    for elem in lst:
        # for every index in the element its looking at, checks if that index matches the letter
        for idx1 in range(len(elem)):
            if (letter == elem[idx1]):
                # if theres a match, for every index in the element, look for a matching number after the letter
                for idx2 in range(idx1 +1, len(elem)):
                    if (digit == elem[idx2]):
                        # add matching elements into the match list
                        match.append(elem)
    if (match != []):
        print(f"Strings with the pattern: ", *match)
    else:
        print("Strings with the pattern: ")
        print()
#         if letter in lst[elem]:
#             if digit in lst[idx]:
#                 return lst[idx]
#             else:
#                 continue


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------

    # Your code Here
    while (True):
        abc = get_letter()
        num = get_digit()
        result = check_pattern(abc, num, st_list)
        choice = input("Try again (y/n): ")
        if choice == "y":
            continue
        else:
            break
        

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()