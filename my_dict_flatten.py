def dict_flatten(target, separator):

    def is_dict(target):
        return isinstance(target, dict)

    def is_flattern(target):
        return not any(filter(is_dict, target.values()))

    if not is_dict(target):
        raise ValueError

    if is_flattern(target):
        return target

    ret = {}    
    for key, value in target.items():
        if is_dict(value):
            for k, v in dict_flatten(value, separator).items():
                ret[key + separator + k] = v
        else:
            ret[key] = value
    return ret


if __name__ == '__main__':
    print(dict_flatten({"foo": {"bar": "baz"}, "hoge": "fuga"}, "_"))
