#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:00:30 2020

@author: carolyntaylor
"""
from operator import itemgetter

invoices = [(83, 'Electric sander', 7, 57.98), 
            (24, 'Power saw', 18, 99.99),
            (7, 'Sledge hammer', 11, 21.50),
            (77, 'Hammer', 76, 11.99),
            (39, 'Jig saw', 3, 79.50)]


for ID, desc, quant, price in sorted(invoices, key=itemgetter(1)):
    print(f'{ID:>2}  {desc:<16}{quant:>3}{price:7.2f}')
    
for ID, desc, quant, price in sorted(invoices, key=itemgetter(3)):
    print(f'{ID:>2}  {desc:<16}{quant:>3}{price:7.2f}')
    
quantity = [(desc, quant) for ID, desc, quant, price in invoices]

for desc, quant in sorted(quantity, key=itemgetter(1)):
    print(f'{desc:<16}{quant:>3}')
    
prices = [(desc, quant * price) for ID, desc, quant, price in invoices]

for desc, total in sorted(prices, key=itemgetter(1)):
    print(f'{desc:<16}{total:9.2f}')
    
prices = [(desc, quant * price) for ID, desc, quant, price in invoices\
          if 200 <= quant * price <= 500]

for desc, total in sorted(prices, key=itemgetter(1)):
    print(f'{desc:<16}{total:9.2f}')
    
total = sum([(quant * price) for ID, desc, quant, price in invoices])

print(f'Total for all invoices is: {total:.2f}')