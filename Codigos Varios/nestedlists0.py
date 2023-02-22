a={'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
def flatten_list(a, result=None):
    n=0
    if result is None:
        result = {}
    for x in a.items():
        if isinstance(x[1], dict):
            flatten_list(x[1], result)
        else:
            result.setdefault(x[0],x[1])
            n=n+1
    return result
print(flatten_list(a))