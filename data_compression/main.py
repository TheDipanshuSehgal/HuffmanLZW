
from algorithm import huffman_coding, lzw_compress

def main():
    print("Welcome to Data Elegance in Bits!")
    text = input("Enter the text to compress: ")

    print("\nSelect the compression algorithm:")
    print("1. Huffman Coding")
    print("2. Lempel-Ziv-Welch (LZW) Compression")
    
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        codes = huffman_coding(text)
        print("Huffman Codes:", codes)
    elif choice == '2':
        compressed = lzw_compress(text)
        print("Compressed LZW Codes:", compressed)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
