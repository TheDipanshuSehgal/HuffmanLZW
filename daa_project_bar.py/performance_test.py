import time
import random
import string
import matplotlib.pyplot as plt
from algorithm import huffman_coding, lzw_compress

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def calculate_compressed_size_huffman(text, codes):
    return sum(len(codes[char]) for char in text)  

def calculate_compressed_size_lzw(compressed):
    return len(compressed) * 12 

def performance_test():
    input_sizes = [5000, 10000, 50000, 100000, 200000]

    huffman_times = []
    lzw_times = []
    huffman_ratios = []
    lzw_ratios = []

    for size in input_sizes:
        text = generate_random_string(size)  
        original_size = len(text) * 8  

        start_time = time.perf_counter()  
        codes = huffman_coding(text)
        huffman_compressed_size = calculate_compressed_size_huffman(text, codes)
        huffman_time = time.perf_counter() - start_time  
        huffman_ratio = huffman_compressed_size / original_size

        start_time = time.perf_counter() 
        compressed = lzw_compress(text)
        lzw_compressed_size = calculate_compressed_size_lzw(compressed)
        lzw_time = time.perf_counter() - start_time  
        lzw_ratio = lzw_compressed_size / original_size

        huffman_times.append(huffman_time)
        lzw_times.append(lzw_time)
        huffman_ratios.append(huffman_ratio)
        lzw_ratios.append(lzw_ratio)

    plot_results(input_sizes, huffman_times, lzw_times, huffman_ratios, lzw_ratios)

def plot_results(input_sizes, huffman_times, lzw_times, huffman_ratios, lzw_ratios):
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.bar([str(size) for size in input_sizes], huffman_times, label="Huffman Coding", alpha=0.7)
    plt.bar([str(size) for size in input_sizes], lzw_times, label="LZW Compression", alpha=0.5)
    plt.title("Execution Time vs Input Size")
    plt.xlabel("Input Size (characters)")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(input_sizes, huffman_ratios, label="Huffman Coding", marker='o')
    plt.plot(input_sizes, lzw_ratios, label="LZW Compression", marker='o')
    plt.title("Compression Ratio vs Input Size")
    plt.xlabel("Input Size (characters)")
    plt.ylabel("Compression Ratio")
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    performance_test()
