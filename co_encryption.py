import numpy as np
import random
import string


def set_index(keyword):
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    # Determina la longitud de la palabra clave única para el tamaño de la matriz
    size = len(keyword)
    keyword_indices = [string.ascii_lowercase.index(k) for k in keyword]
    sorted_indices = sorted(range(len(keyword_indices)), key=lambda k: keyword_indices[k])
    order_indices = [sorted_indices.index(i) + 1 for i in range(len(sorted_indices))]
    return order_indices, size  # Devuelve también el tamaño

def fill_matrix(text, rows, cols):
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    message_index = 0
    for row in range(rows):
        for col in range(cols):
            if message_index < len(text):
                matrix[row][col] = text[message_index]
                message_index += 1
            else:
                matrix[row][col] = random.choice(string.ascii_lowercase)
    return matrix

def sort_columns(matrix, keyword_indices, encrypting=True):
    matrix = np.array(matrix)
    if encrypting:
        order_indices = np.argsort(keyword_indices)
    else:
        order_indices = np.argsort(np.argsort(keyword_indices))
    sorted_matrix = matrix[:, order_indices]
    return sorted_matrix

def encrypt(text, key_word):
    keyword_indices, size = set_index(key_word)  # Ajusta para usar el tamaño
    # Usa el tamaño para definir las dimensiones de la matriz
    rows, cols = size, size
    matrix = fill_matrix(text, rows, cols)
    sorted_matrix = sort_columns(matrix, keyword_indices)
    encrypted_message = '\n'.join([''.join(sorted_matrix[:, i]) for i in range(cols)])
    return encrypted_message

def decrypt(encrypted_message, key_word):
    columns = [column.strip() for column in encrypted_message.split('\n')]
    max_length = max(len(column) for column in columns)
    columns = [column.ljust(max_length, ' ') for column in columns]
    keyword_indices, size = set_index(key_word)  # Ajusta para usar el tamaño
    try:
        matrix = np.array([list(column) for column in columns]).T
    except ValueError as e:
        return f"Error al formar la matriz: {e}"
    sorted_matrix = sort_columns(matrix, keyword_indices, encrypting=False)
    decrypted_message = ''.join([''.join(sorted_matrix[i]) for i in range(size)])  # Ajusta para leer correctamente
    return decrypted_message


