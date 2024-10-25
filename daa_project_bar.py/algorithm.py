from collections import Counter
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(text):
    frequency = Counter(text)
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    root = priority_queue[0]
    codes = {}
    _generate_codes(root, "", codes)
    return codes

def _generate_codes(node, current_code, codes):
    if node:
        if node.char is not None:
            codes[node.char] = current_code
        _generate_codes(node.left, current_code + "0", codes)
        _generate_codes(node.right, current_code + "1", codes)

def lzw_compress(text):
    dictionary = {chr(i): i for i in range(256)}
    current_string = ""
    compressed = []
    code = 256

    for symbol in text:
        combined_string = current_string + symbol
        if combined_string in dictionary:
            current_string = combined_string
        else:
            compressed.append(dictionary[current_string])
            dictionary[combined_string] = code
            code += 1
            current_string = symbol

    if current_string:
        compressed.append(dictionary[current_string])
    
    return compressed
