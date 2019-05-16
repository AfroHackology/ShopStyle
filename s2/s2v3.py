# calculating sums and totals
import numpy
from introDataScience.s2.s2v1 import load_data
my_csv = load_data('data.csv')

def calculate_sum(data_sameple):
    total = 0
    for row in data_sameple[1:]:
        price = float(row[2])
        total += price
    return total

def calculate_sum_succinct(data_sameple):
    prices = [float(row[2]) for row in data_sameple[1:]]
    return sum(prices)

def calculate_sum_concise(data_sample):
    prices = list(map(lambda x: float(x[2]), data_sample[1:]))
    return sum(prices)

#rint(calculate_sum_concise(data_from_csv))
#print(calculate_sum_succinct(data_from_csv))

def calc_numpy_sum(price):
    prices_in_float = [float(line) for line in price]
    total = numpy.sum(prices_in_float)
    return total

price = my_csv['pricelabel']
my_sum = calc_numpy_sum(price)
#print("The sum (numpy);", my_sum)