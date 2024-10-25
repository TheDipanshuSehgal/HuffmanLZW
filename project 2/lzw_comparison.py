def lzw_compress(data):
    # Step 1: Initialize the dictionary with single characters
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    w = ""
    compressed = []
    
    for c in data:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            compressed.append(dictionary[w])
            dictionary[wc] = next_code
            next_code += 1
            w = c

    if w:
        compressed.append(dictionary[w])
    
    return compressed

def lzw_decompress(compressed):
    # Step 1: Initialize the dictionary with single characters
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    w = chr(compressed.pop(0))
    decompressed = [w]

    for code in compressed:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = w + w[0]
        else:
            raise ValueError("Invalid compressed code")
        
        decompressed.append(entry)
        
        # Add w+entry[0] to the dictionary
        dictionary[next_code] = w + entry[0]
        next_code += 1
        w = entry
    
    return ''.join(decompressed)

# Example Usage
data = "this is an example for huffman encoding"
compressed = lzw_compress(data)
decompressed = lzw_decompress(compressed)

print(f"Original: {data}")
print(f"Compressed: {compressed}")
print(f"Decompressed: {decompressed}")
