import numpy as np
from typing import Tuple, List


def make_template(string: str, n: int) -> Tuple[np.ndarray, List[int], List[int]]:
    """
    Creates a template matrix and corresponding indices for encoding or decoding using 
    Rail Fence Cipher.

    Args:
        string (str): The string for encoding or decoding.
        n (int): The number of rows in the template matrix.

    Returns:
        Tuple[np.ndarray, List[int], List[int]]: A tuple containing:
            - the template matrix;
            - the list of row indices for encoding or decoding;
            - the list of column indices for encoding or decoding.
    """
    len_matrix = len(string)
    matrix = np.full((n, len_matrix), None)
    
    col_index = list(range(len_matrix))
    sequence = list(range(n)) + list(range(n - 2, 0, -1))
    repetitions, remainder = divmod(len_matrix, len(sequence))
    row_index = sequence * repetitions + sequence[:remainder]

    return matrix, row_index, col_index

def encode_rail_fence_cipher(string: str, n: int) -> str:
    """
    Encodes the given string using Rail Fence Cipher.

    Args:
        string (str): The string to be encoded.
        n (int): The number of rows in the encoding matrix.

    Returns:
        str: The encoded string.
    """
    matrix, row_index, col_index = make_template(string, n)

    for row, col in zip(row_index, col_index):
        matrix[row, col] = string[col]

    encode_text = ''.join(str(item) for row in matrix for item in row if item is not None)

    return encode_text

def decode_rail_fence_cipher(string: str, n: int) -> str:
    """
    Decodes the given string using Rail Fence Cipher.

    Args:
        string (str): The string to be decoded.
        n (int): The number of rows in the decoding matrix.

    Returns:
        str: The decoded string.
    """
    matrix, row_index, col_index = make_template(string, n)

    for row, col in zip(row_index, col_index):
        matrix[row, col] = True

    k = 0
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            if item is not None:
                matrix[i, j] = string[k]
                k += 1
                
    decode_text = "".join(matrix[row, col] for row, col in zip(row_index, col_index))

    return decode_text


if __name__ == '__main__':
    print(encode_rail_fence_cipher("Hello, World!", 4))

    # print(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3))

    print(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3))