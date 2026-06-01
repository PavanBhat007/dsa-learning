"""
2144. Minimum Cost of Buying Candies With Discount [Easy]

A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.
The customer can choose any candy to take away for free as long as the cost of the chosen candy is less than or equal to the minimum cost of the two candies bought.

For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3, 
they can take the candy with cost 1 for free, but not the candy with cost 4.

Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the minimum cost of buying all the candies.
"""

# -------------------------------------------------------------------------------------------------

def minCostOfCandiesWithDiscount(cost):
    num_candies = len(cost)
    final_cost = 0

    if num_candies == 1:
        return cost[0]
    elif num_candies == 2:
        return cost[0] + cost[1]
    else:

        # sort in decreasing order to buy costly candies pair
        # to be always able to avail next candy for free
        cost.sort(reverse=True)
        for i in range(num_candies):
            # buy 2 next 1 free, first one always buy
            if (i+1)%3 != 0 or i == 0:
                final_cost += cost[i]
        
        return final_cost
    
if __name__ == "__main__":
    n = int(input("NUMBER OF CANDIES: "))
    candies = [int(candy) for candy in input("CANDIES COST: ").split(" ")]

    min_cost = minCostOfCandiesWithDiscount(candies)
    print(f"Minimum cost of buying all candies with discount = {min_cost}")