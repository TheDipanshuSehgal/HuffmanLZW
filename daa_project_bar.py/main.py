from algorithm import huffman_coding, lzw_compress
import performance_test

def main():
    print("Welcome to Data Elegance in Bits!")
    text = input("Enter the text to compress: ")

    print("\nPerforming Huffman Coding...")
    huffman_codes = huffman_coding(text)
    print("Huffman Codes:", huffman_codes)

    print("\nPerforming LZW Compression...")
    lzw_compressed = lzw_compress(text)
    print("Compressed LZW Codes:", lzw_compressed)

    # performance_test.performance_test_with_input(text) 

if __name__ == "__main__":
    main()
