from collections import Counter
from heapq import heapify, heappop, heappush

t = "banana"
binary = ""

def huffman(t):
    global binary
    fila = [[n, [c, ""]] for c, n in Counter(t).items()]
    heapify(fila)
    while len(fila) > 1:
        a,b = heappop(fila), heappop(fila)

        for p in a[1:]: p[1] = '0' + p[1]
        

        for p in b[1:]: p[1] = '1' + p[1]
        

          # Print the current state of the heap
        
        heappush(fila, [a[0] + b[0]] + a[1:] + b[1:])


     # Print the codes for each character
    return dict(fila[0][1:])

reverse_dict = {v: k for k, v in huffman(t).items()}

def huffman_decode(encoded_str):
    global reverse_dict    
    
    decoded_str = ""
    current_code = ""
    
    for bit in encoded_str:
        current_code += bit
        if current_code in reverse_dict:
            decoded_str += reverse_dict[current_code]
            current_code = ""
    
    return decoded_str

print(huffman(t))
print(huffman_decode("100110110"))  # Example usage of the decode function