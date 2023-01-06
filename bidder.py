from replit import clear

print("Welcome to the secret auction program.")

repeat = True
bidders_dictionary = {}

# Winner selection function
def winner_selector(bidders_dictionary):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bidders_dictionary:
        if bidders_dictionary[bidder] > highest_bid:
            highest_bid = bidders_dictionary[bidder]
            highest_bidder = bidder

    
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

# Bidders dictionary creates here
while repeat:

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if answer == "yes":
        repeat = True
    else:
        repeat = False

    bidders_dictionary[name] = bid
    
    clear()

winner_selector(bidders_dictionary)