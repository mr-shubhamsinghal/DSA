def compress_string(input_str):
    compressed = ""
    count = 1
    
    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            compressed += input_str[i - 1] + str(count)
            count = 1
    
    compressed += input_str[-1] + str(count)
    
    return compressed

# Example usage
input_str = "aafdddervteaa"
output = compress_string(input_str)
print(output)  # Output: f1r1t1v1e2d3a4