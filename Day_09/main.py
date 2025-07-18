#Ask the user for the inputs
#Save the data to the dictionary
# Whether the new bids need to be added

# Compare the bids in the dictionary
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name? : ")
    bid_price = int(input("What is your bid? : $"))
    bids[name] = bid_price
    should_continue = input("Are there any other bidders? Type 'Yes' ore 'No' \n" ).lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 25 )