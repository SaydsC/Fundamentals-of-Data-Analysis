#Alice in Wonderland Exercise 1
#author Sadie Concannon
# exercise: Adapt the code above to generate a 1000 character long string with wrights based on the previous two characters

# Import internet request to access Alice in Wonderland
import urllib.request

# The URL of a text version of Alice in Wonderland.
book_url = 'https://www.gutenberg.org/files/11/11-0.txt'

# Getting the book
book = list(urllib.request.urlopen(book_url))

# Decode the lines and strip line endings
book = [line.decode('utf-8-sig').strip() for line in book]

# Get a sample paragraph - taken from lecture notes
paragraph = ' '.join(book[58:63])

# Let's lower-case it
alice = paragraph.lower()

# All letters and a space.
chars = 'abcdefghijklmnopqrstuvwxyz '

# And strip anything that is not a letter or space
alice = ''.join([c for c in alice if c in chars])

# Show the paragraph now
#print(alice)

# Import string and random to generate random string
import string
import random
import numpy as np

# random.choice() to generate strings in which characters may repeat
# random.sample() to genrate non repeating characters

# Get the whole book in one big string.
sbook = ''.join(book[26:]).lower()

# Create the weights - count the occurences of each character in the whole book.
weights = [sbook.count(c) for c in chars]

# Show the weights.
#print(weights)

# Generate a string using these weights
# k defines the length of the random string
wgenr = random.choices(chars, weights=weights, k=1000)

# Join them together in a string
wgenr = ''.join(wgenr)

# Print
#print(wgenr)

# Create the weights.
twoghts = {c: {d: sbook.count(c + d)for d in chars} for c in chars}

# Show the weights.
#print(twoghts)

# Loop through our character set.
for i in range(len(chars)):
    # Print the character and how many times it appears in Alice in Wonderland.
    #print(f'{chars[i]}: {weights[i]}')

# Start with space.
    pairs = ' '
    N=1000
# Do the following N-1 times.
for i in range(1, N):
    # Get the weights where the previous two character is the last character in twos.
    wt = twoghts[pairs[-1]]
    # Turn wt into a list, ordered by chars.
    wt = [wt[c] for c in chars]
    # Randomly pick the next character using those weights.
    nextc = random.choices(chars, weights=wt, k=1)[0]
    # Append the character to twos.
    pairs = pairs + nextc 
    print(pairs)   