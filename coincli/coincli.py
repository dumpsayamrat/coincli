#!/usr/bin/env python3

# import sys
import argparse
from texttable import Texttable

from . import fetch_coins

parser = argparse.ArgumentParser(description='Crypto in terminal ')

def limit_validator(arg):
  try:
      n = int(arg)
      assert n > 0
      assert n <= 10
      return n
  except (ValueError, AssertionError):
      raise argparse.ArgumentTypeError('%s is not valid, it should be between 1 - 10' % arg)

parser.add_argument('-l', '--limit', type=limit_validator, default=5,
  metavar='N', help='number of coins to display, max is 10')

args = parser.parse_args()
print(args.limit)
data = fetch_coins(vars(args))


def generate_table(headers, data):
  t = Texttable(max_width=0)
  headersRow = []
  for h in headers:
    headersRow.append(h['title'])
  dataRow = []
  for index, item in enumerate(data):
    result = []
    for h in headers:
      if(h['title'] == '#'):
        result.append(index + 1)
      else:
        result.append(item[h['key']])
    dataRow.append(result)
  # print(dataRow)
  t.add_rows([headersRow] + dataRow)
  return t

headers = [
  {'title': '#'},
  {'title': 'Name', 'key': 'name'},
  {'title': 'Price', 'key': 'price'},
  {'title': '24h %', 'key': 'today_change'},
  {'title': '7d %', 'key': 'week_change'},
  {'title': 'Market Cap', 'key': 'market_cap'},
  {'title': 'Volume', 'key': 'volume'}
]
print(generate_table(headers, data).draw())
