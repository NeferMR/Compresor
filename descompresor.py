import heapq
import os
import numpy as np


class HuffmanCoding:

  def __init__(self, path):
    self.path = path
    self.heap = []
    self.codes = {}
    self.reverse_mapping = {}

  class HeapNode:

    def __init__(self, char, freq):
      self.char = char
      self.freq = freq
      self.left = None
      self.right = None

    def __lt__(self, other):
      return self.freq < other.freq

    def __eq__(self, other):
      if (other == None):
        return False
      if (not isinstance(other, HeapNode)):
        return False
      return self.freq == other.freq

  def remove_padding(self, padded_encoded_text):
    padded_info = padded_encoded_text[:8]
    extra_padding = int(padded_info, 2)
    padded_encoded_text = padded_encoded_text[8:]
    encoded_text = padded_encoded_text[:-extra_padding]
    return encoded_text

  def decode_text(self, encoded_text):
    current_code = ""
    decoded_text = ""
    for bit in encoded_text:
      current_code += bit
      if (current_code in self.reverse_mapping):
        character = self.reverse_mapping[current_code]
        decoded_text += character
        current_code = ""
    return decoded_text

  def decompress(self, input_path):
    filename, file_extension = os.path.splitext(self.path)
    output_path = "descomprimido_elmejorprofesor.txt"

    with open(input_path, 'rb') as file, open(output_path,
                                              mode='w',
                                              encoding='cp1252',
                                              newline='\r\n') as output:
      bit_string = ""
      byte = file.read(1)
      while (byte != b''):
        byte = ord(byte)
        bits = bin(byte)[2:].rjust(8, '0')
        bit_string += bits
        byte = file.read(1)

      encoded_text = self.remove_padding(bit_string)
      decompressed_text = self.decode_text(encoded_text)
      output.write(decompressed_text)

    print("Decompressed file saved successfully")
    return output_path


huffman = HuffmanCoding("./LaBiblia.txt")
descompressed_file = huffman.decompress("./comprimido.elmejorprofesor")

print("Terminado")
