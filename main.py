from art import logo
import os

print(logo)

bidder1_name = input("You are the first bidder. What is your name? ")
bidder1_amount = int(input("How much do you bid $"))

auction = {}

auction[bidder1_name] = bidder1_amount

more_bidders = ''
while more_bidders != 'no' and more_bidders != 'n' and more_bidders != 'yes' and more_bidders != 'y':
    more_bidders = input("Are there any other bidders? type 'yes' or 'no'\n").casefold()

more_bidders = True if more_bidders == 'y' or more_bidders == 'yes' else False

while more_bidders:
    os.system('clear')
    name = input("Hello next bidder. What is your name?: ")
    amount = int(input("What is your bid?: $"))
    auction[name] = amount
    while more_bidders != 'no' and more_bidders != 'n' and more_bidders != 'yes' and more_bidders != 'y':
        more_bidders = input("Are there any other bidders? type 'yes' or 'no'\n").casefold()

    more_bidders = True if more_bidders == 'y' or more_bidders == 'yes' else False


# Find highest bid
highest_bid = 0

for k in auction:
    if auction[k] > highest_bid:
        highest_bid = auction[k]
        highest_bidder = k

if highest_bid == 0:
    highest_bidder = 'nobody'
    msg = 'as there were no '
    highest_bid = 'valid bids'
else:
    msg = 'with a bid of $'

print(f"The winner is {highest_bidder} {msg}{highest_bid}.")