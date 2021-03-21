# pcost.py
#
# Exercise 1.27


# total_cost = 0

# with open('/mnt/e/get_better/programme/practical-python/Work/Data/portfolio.csv') as f:
#     headers = next(f)
#     for line in f:
#         row = line.split(',')
#         shares = int(row[1])
#         price = float(row[2])
#         total_cost += shares * price
# print('Total cost', total_cost)

# # Exercise 1.30


# def portfolio_cost(filename):
#     '''
#     # Your code here
#     '''
#     cost = 0
#     with open(filename) as f:
#         headers = next(f)
#         for line in f:
#             row = line.split(',')
#             shares = int(row[1])
#             price = float(row[2])
#             cost += shares * price
#     return cost

# cost = portfolio_cost('/mnt/e/get_better/programme/practical-python/Work/Data/portfolio.csv')
# print('Total cost:', cost)


import csv
def portfolio_cost(filename):

    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                shares = int(row[1])
                price = float(row[2])
                total_cost += shares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print('Bad row:', row)

    return total_cost

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)
