#Huffman encoding

import heapq  # Importing the heapq library for heap operations

def calculate_frequency(s): 
    frequency = {}  # Initialize an empty dictionary to store character frequencies
    for char in s:
        if char not in frequency:  # If character is not already in the dictionary
            frequency[char] = 0    # Initialize its frequency to 0
        frequency[char] += 1       # Increment frequency count for the character
    return frequency  # Return the frequency dictionary

def huffman_encode(frequency):
    # Create a list of lists, where each inner list contains the weight (frequency)
    # and a list with the character and an empty string (for the Huffman code)
    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    
    # Convert the list into a min-heap based on frequency (weight) using heapify
    heapq.heapify(heap)
    
    # While there's more than one element in the heap
    while len(heap) > 1:
        # Remove the two elements with the smallest frequencies
        lo = heapq.heappop(heap)  # Pop the smallest item from the heap
        hi = heapq.heappop(heap)  # Pop the next smallest item from the heap
        
        # Assign "0" to all characters in the left (smallest) part
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        
        # Assign "1" to all characters in the right (second smallest) part
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        
        # Push a new item into the heap with the combined weight and characters
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    # Pop the final element in the heap, sort by code length and return the characters and their codes
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

# Input and process
s = input("Enter the string or words to generate their Huffman encoding: ")
frequency = calculate_frequency(s)  # Calculate frequency of each character
huff = huffman_encode(frequency)    # Generate Huffman codes

# Display results
print(f"Frequency of the characters in the given string: {frequency}")
print("Char | Huffman code ")
print(" ")
for char, huffman_code in huff:
    print(f" {char} | {huffman_code}")