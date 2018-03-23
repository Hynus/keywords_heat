def group(n, sep = ','):
    s = str(n)[::-1]
    groups = []
    i = 0
    while i < len(s):
        groups.append(s[i:i+3])
        i+=3
    retval = sep.join(groups)[::-1]
    if n < 0:
        return '-%s' % retval
    else:
        return retval

def comma_str_to_int(num_str):
    return int(num_str.replace(',', ''))