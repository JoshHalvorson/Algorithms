#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # recursive method, couldnt quite figure out how to implement caching with this so this method 
  # dosnt work with the largers tests
  """if amount == 0 or amount == 1:
    return 1
  if amount < 0 or len(denominations) == 0:
    return 0
  # call making_change, decrementing the coin, add it to result of other recursive 
  # call with all but last coin in denominations
  return making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[:-1])"""
  
  # this method is whats laid out in the readme hints, not recursive but imo looks better and the
  # caching works 

  # initialize cache from 0 to the amount + 1 (index out of range otherwise) and intilize the 0 value
  cache = [0 for i in range(amount + 1)]
  cache[0] = 1
  # loop through the coins in denominations, and for each coin loop through the range from the coin to
  # amount + 1. Then add the difference of the higher amount and the coin to the cached value
  for c in denominations:
    #print(c)
    for higher_amount in range(c, amount + 1):
      #print(higher_amount)
      cache[higher_amount] += cache[higher_amount - c]
  return cache[amount]

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")