

def is_boring_string(odd_str, even_str):
    
    if ord(odd_str[-1]) + 1 == ord(even_str[0]) or ord(odd_str[-1]) - 1 == ord(even_str[0]):
        return 0
    return 1

def boring_substring(string):
    
    n = len(string)
    if n == 2:
        return 0
    
    even_str = ''
    odd_str = ''
    for s in string:
        if ord(s) % 2 == 0:
            odd_str += s
        else:
            even_str += s
    
    if not even_str or not odd_str:
        return 1
    
    even_str = sorted(even_str)
    odd_str = sorted(odd_str)
    
    # odd_str + even_str
    if is_boring_string(odd_str, even_str):
        return 1
    
    if is_boring_string(even_str, odd_str):
        return 1
    
    return 0


if __name__ == "__main__":
    # string = "abcd"
    string = "gihhfjjejgh"
    ans = boring_substring(string)
    print(ans)
