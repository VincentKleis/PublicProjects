def flett(x: str, y: str) -> str:
    result = ''
    res_list = [x, y]
    for i in range(len(min(res_list))):
        result += x[i] + y[i]
    result += max(res_list)[len(min(res_list)):]
    return result
test1 = flett('abcdef', '1234')
print(test1)