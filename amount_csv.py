# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 11:29:43 2017

@author: kawarayu
"""
from datetime import datetime

INPUT_FILE = 'amount_input.csv'
day = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
OUTPUT_FILE = day + '_amount.csv'
#ENCODING = 'cp932'
ENCODING = 'UTF-8'
items = []


with open(INPUT_FILE, encoding=ENCODING) as f:
    for i, row in enumerate(f):
        if i == 0: # ヘッダ行をスキップ
            accounts = row.rstrip().split(',')
            accounts.pop(0)
            continue
        
        line = row.rstrip().split(',')
        org = line.pop(0) # 組織コードを取り除く
        for j, amount in enumerate(line):
            items.append({
                    'org': org,
                    'acc': accounts[j],
                    'amo': amount,
                     })

with open(OUTPUT_FILE, 'w', encoding=ENCODING) as f:
    for item in items:
        string = f"{item['org']},{item['acc']},{item['amo']}\n"
        f.write(string)

