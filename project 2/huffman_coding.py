import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_tree(data):
    # Step 1: Frequency calculation
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1
    
    # Step 2: Priority Queue (Min Heap)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    # Step 3: Build Huffman Tree
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    
    return heap[0]

def huffman_codes(root):
    # Step 4: Assign Codes
    huff_codes = {}

    def generate_codes(node, code=""):
        if node is not None:
            if node.char is not None:
                huff_codes[node.char] = code
            generate_codes(node.left, code + "0")
            generate_codes(node.right, code + "1")
    
    generate_codes(root)
    return huff_codes

def huffman_encode(data, codes):
    return ''.join(codes[char] for char in data)

def huffman_decode(encoded_data, root):
    decoded_data = []
    current = root
    for bit in encoded_data:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        if current.char:
            decoded_data.append(current.char)
            current = root
    return ''.join(decoded_data)

# Example Usage
data = "this is an example for huffman encoding"
root = huffman_tree(data)
codes = huffman_codes(root)
encoded_data = huffman_encode(data, codes)
decoded_data = huffman_decode(encoded_data, root)

print(f"Original: {data}")
print(f"Encoded: {encoded_data}")
print(f"Decoded: {decoded_data}")
