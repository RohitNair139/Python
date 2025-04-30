def get_bids(starting_price):
    """
    Prompts bidders to enter their name and bid.
    Stops when an empty name is entered.
    Ensures each bid > current highest (or starting price).
    Returns a dict of {bidder_name: bid_amount}.
    """
    bids = {}
    highest = starting_price

    while True:
        name = input("Bidder name (Enter to finish): ").strip()
        if not name:
            break

        try:
            bid = float(input(f"  {name}, enter your bid (current highest: {highest}): "))
        except ValueError:
            print("  → Invalid number, try again.")
            continue

        if bid <= highest:
            print(f"  → Bid must be greater than {highest}.")
            continue

        bids[name] = bid
        highest = bid

    return bids

def determine_winner(bids):
    """
    From bids dict, return (winner_name, winning_bid).
    If no bids, returns (None, None).
    """
    if not bids:
        return None, None
    winner = max(bids, key=bids.get)
    return winner, bids[winner]

def main():
    print("=== Auction Simulator ===")
    item = input("Item up for auction: ").strip()
    while not item:
        item = input("  Please enter an item name: ").strip()

    # Starting price
    while True:
        try:
            start = float(input("Starting price: "))
            break
        except ValueError:
            print("  → Please enter a valid number.")

    print(f"\nAuctioning: '{item}' starting at {start}\n"
          "Enter bids below. Leave name blank to end.\n")

    bids = get_bids(start)

    winner, price = determine_winner(bids)
    print("\n=== Auction Result ===")
    if winner:
        print(f"Winner: {winner}\nWinning Bid: {price}")
    else:
        print("No bids were placed. Auction closed without a sale.")

if __name__ == "__main__":
    main()
