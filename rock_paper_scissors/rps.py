#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  plays = ['rock', 'paper', 'scissors']
  result = []
  buildArr(plays, result, [], n)
  return result

def buildArr(plays, result, arr, n):
  # base case
  # if no more plays to be added to arr, append the arr to result
  if n == 0:
    result.append(arr)
    return
  # loop through the plays, recursivley call builArr to build up the arr with n plays
  for play in plays:
    buildArr(plays, result, arr + [play], n - 1)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')