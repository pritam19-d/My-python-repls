from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

bidders_details = []
new_bidder = "y"

def add_bidders(name, bid):
    bidders_details.append({"bidder_name": name, "bid_amount": bid})
    global new_bidder
    new_bidder = input("Is there any other bidders? (type 'y' or 'n') :").lower()
    clear()

while new_bidder == "y":
    name = input("What is your name? :")
    bid = int(input("Enter your bidding amount: ₹"))
    add_bidders(name, bid)
clear()

highest_bid = {"winner_bidder": "", "winners_bid": 0}
for i in range(0, len(bidders_details)):
    if bidders_details[i]["bid_amount"] > highest_bid["winners_bid"]:
        highest_bid["winners_bid"] = bidders_details[i]["bid_amount"]
        highest_bid["winner_bidder"] = bidders_details[i]["bidder_name"]

print(f"The bid winner is {highest_bid['winner_bidder']} with the bid amount of ₹{highest_bid['winners_bid']}")
