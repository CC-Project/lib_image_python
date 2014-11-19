# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 10:48:11 2014

@author: Thibault
"""

from PIL import Image

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
    
def ImageToHex(image_path):
    im = Image.open(image_path)
    (l, h) = im.size
    C = []
    
    for y in range(h):
        for x in range(l):
            color = Image.Image.getpixel(im, (x, y))
            C.append(rgb_to_hex(color))
    
    return C
    
def hex_to_bin(hex_string):
    return bin(int(hex_string, 16))[2:]
    
def ImageToBin(directory, image_path):
    C = ImageToHex(directory + '/' + image_path)
    
    T = ""
    for h in C:
        T += hex_to_bin(h)
        
    fichier = open('Files/' + image_path.split('.')[0] + ".txt", "w")
    fichier.write(T)
    
def BinToImage(file_path, encode = None):
    if encode == None: # Si le fichier n'est pas encode
        pass
    if encode == "ham": # Encodage par hamming
        pass
    
def generateImage(binary_code, h, l, comment = ""):
    pass