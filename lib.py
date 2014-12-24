# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 10:48:11 2014

@author: Thibault
"""

from PIL import Image
import glob, os

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

def hex_to_rgb(hex_word):
    if hex_word != "":
        return tuple(ord(c) for c in hex_word.decode('hex'))
    return (0,0,0)

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
    bina = bin(int(hex_string, 16))[2:]
    while len(bina) != 24:
        bina = "0" + bina
        
    return bina
    
def bin_to_hex(binary_string):
    if binary_string != "":
        hexa = hex(int(binary_string, 2))[2:]
        
        while len(hexa) != 6:
            hexa = "0" + hexa
            
        return hexa
    return ""

def ImageToBin(image_name):
    C = ImageToHex("Images/" + image_name)
    
    T = ""
    for h in C:
        T += hex_to_bin(h)
        
    fichier = open('Files/' + image_name.split('.')[0] + ".txt", "w")
    fichier.write(T + '\n')
    
def BinToImage(file_name):
    (l, h) = 200, 262
    
    fichier = open('Files/' + file_name + ".txt", "r")
    C = fichier.read()

    im = Image.new("RGB", (l, h), "white")
    pix = im.load()
    
    for y in range(h):
        for x in range(l):
            rang = (y * l + x) * 24
            pix[x, y] = hex_to_rgb(bin_to_hex(C[rang : rang + 24]))
        
    im.save("Images/" + file_name + ".png")
    
def generateImage(binary_code, h, l, comment = ""):
    hexa_code = bin_to_hex(binary_code)
    C = [hexa_code[6 * i: 6 * (i + 1)] for i in range(len(hexa_code / 6))] # On génère la liste contenant le couleur de chaque pixels