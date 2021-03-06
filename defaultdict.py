"""Build an index mapping word -> list of occurerences"""

import sys
import re
import collections

WORD_RE = re.compile(r'\w+')

#index = {}
index = collections.defaultdict(list)

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            #index.setdefault(word, []).append(location)
            index[word].append(location)


# print in frequency order
for word in sorted(index, key=lambda x: len(index[x]), reverse=True):
    print(word, index[word])
