d={'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
def flatten_dict(d, prefix='',result=None):
    if result is None:
        result = {}
    for k,v in d.items():
        if isinstance(v,dict):
            flatten_dict(v, prefix=str(k),result=result)
        else:
            if prefix=='':
                result.setdefault(k,v)
            else:
                result.setdefault(prefix+'.'+k,v)
    return result
dd=flatten_dict(d, prefix='')           
print(dd)
def unflatten_dict(dd, prefix='',result=None,number=None):
    if result is None:
        result = {}
    if isinstance(dd,dict):
        for k,v in dd.items():
            if '.' in k:
                t=k.split('.')
                unflatten_dict(t[1], prefix=t[0],result=result,number=v)
            else:
                result.setdefault(k,v)
    else:
        global U
        try:
            U[str(dd)]=number
            result.setdefault(prefix,U)
        except:
            U=dict([(str(dd),number)])
            result.setdefault(prefix,U)
    return(result)
d=unflatten_dict(dd, prefix='')
print(d)