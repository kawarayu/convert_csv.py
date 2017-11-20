from collections import UserDict

#class StrKeyDict(dict):
class StrKeyDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
#        return key in self.keys() or str(key) in self.keys()
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

"""
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
"""

if __name__ == '__main__':
    d = StrKeyDict([('2', 'two'), ('4', 'four')])
    print('str: d["2"]: ' , d['2'])
    print('int: d[4]]: ', d[4])
    print('d.get(1, "N/A"): ', d.get(1, 'N/A'))
    print('2 in d: ', 2 in d)
    print('1 in d: ', 1 in d)
