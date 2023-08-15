import sys


class Node:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.direction = ''


def char_freq(data):
    chars = dict()
    for x in data:
        if chars.get(x) == None:  # noqa
            chars[x] = 1
        else:
            chars[x] += 1
    return chars


codes = dict()

def huffman_codes(node, value=''):
    newValue = value + str(node.direction)
    if (node.left):
        huffman_codes(node.left, newValue)
    if (node.right):
        huffman_codes(node.right, newValue)
    if (not node.left and not node.right):
        codes[node.char] = newValue

    return codes


def huffman_encoding(data):
    char_with_freq = char_freq(data)
    chars = char_with_freq.keys()
    frequencies = char_with_freq.values()

    nodes = []

    for char in chars:
        nodes.append(Node(char_with_freq.get(char), char))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)

        right = nodes[0]
        left = nodes[1]

        right.direction = 0
        left.direction = 1

        newNode = Node(left.freq+right.freq, left.char+right.char, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    huffman_encoding = huffman_codes(nodes[0])
    encodedOutput = encoded_output(data, huffman_encoding)
    return  encodedOutput, nodes[0]


def encoded_output(data, coding):
    encodedOutput = []
    for _ in data:
        encodedOutput.append(coding[_])

    string = ''.join([str(x) for x in encodedOutput])
    return string

def huffman_decoding(data, tree):
    head = tree
    decodedOutput = []
    for _ in data:
        if _ == '1':
            tree = tree.right
        elif _ == '0':
            tree = tree.left
        try:
            if tree.left.char == None and tree.right.char == None:
                pass
        except AttributeError:
            decodedOutput.append(tree.char)
            tree = head

    string = ''.join([str(x) for x in decodedOutput])
    return string



if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null,
# #empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3
