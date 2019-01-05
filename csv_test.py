# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 08:45:58 2018

@author: elindgre
"""

import csv
rek = []

with open('mlearndata.csv', 'wb') as csvfile:
    fieldnames = ['Open', 'Lunch', 'Close', 'yclose', 'closetoopen', 'opentolunch', 'lunchtoclose', 'rek']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    
    for i in range(len(first_minute)-1):
        if i > 0:
            if last_minute[i] > kurs_lunch[i]:
                rek = "BUY"
            else:
                rek = "SELL"
            
            writer.writerow({'Open': first_minute[i], \
            'Lunch': kurs_lunch[i], 'Close': last_minute[i],\
            'yclose':last_minute[i-1],'closetoopen': first_minute[i] - last_minute[i-1],'opentolunch': kurs_lunch[i]-first_minute[i],\
            'lunchtoclose': last_minute[i] - kurs_lunch[i], 'rek': rek})
                         