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

        left.direction = 0
        right.direction = 1

        newNode = Node(left.freq+right.freq, left.char+right.char, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    huffman_encoding = huffman_codes(nodes[0])
    encodedOutput = encoded_output(data, huffman_encoding)
    return encodedOutput, nodes[0]


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
            if tree.left.char is None and tree.right.char is None:
                pass
        except AttributeError:
            decodedOutput.append(tree.char)
            tree = head

    string = ''.join([str(x) for x in decodedOutput])
    return string


if __name__ == "__main__":

    a_great_sentence = "yes"

    print("The size of the data is: "
          "{}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: "
          "{}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: "
          "{}\n".format(sys.getsizeof(huffman_decoding(encoded_data, tree))))
    print("The content of the decoded data is: {}\n".format(decoded_data))

    test_case_1 = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print("The size of the data is: {}\n".format(sys.getsizeof(test_case_1)))
    print("The content of the data is: {}\n".format(test_case_1))

    encoded_data, tree = huffman_encoding(test_case_1)

    print("The size of the encoded data is: "
          "{}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: "
          "{}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))

    test_case_2 = "GO BLUE!!!!!"

    print("The size of the data is: {}\n".format(sys.getsizeof(test_case_2)))
    print("The content of the data is: {}\n".format(test_case_2))

    encoded_data, tree = huffman_encoding(test_case_2)

    print("The size of the encoded data is: "
          "{}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: "
          "{}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))

    test_case_3 = ("ABC" * 99)

    print("The size of the data is: {}\n".format(sys.getsizeof(test_case_3)))
    print("The content of the data is: {}\n".format(test_case_3))

    encoded_data, tree = huffman_encoding(test_case_3)

    print("The size of the encoded data is: "
          "{}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: "
          "{}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))
