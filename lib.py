# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 10:48:11 2014

@author: Thibault
"""

from PIL import Image
import glob, os
import matplotlib.pyplot as pp

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

def BinToImage(file_name, l, h): 
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
    
    
# Comparation libarie
    
def compare(file_name, pas):
    fichier = open('Files/' + file_name + ".txt", "r")
    coded = open('Files/' + file_name + "_CODED" + ".txt", "r")
    
    fichier = fichier.read()
    coded = coded.read()
    
    X = []
    Y = []
    for i in range(1001)[::pas]:
        print i
        decoded_without = open('Files/' + file_name + "_" + str(i) + "_DECODED_NO_C" + ".txt", "r")
        decoded_with = open('Files/' + file_name + "_" + str(i) + "_DECODED_WITH_C" + ".txt", "r")
        
        decoded_without = decoded_without.read()
        decoded_with = decoded_with.read()
        
        nb_error, nb_error_finale = 0., 0.
        for j in range(len(decoded_with)):
            if decoded_without[j] != fichier[j]:
                nb_error += 1
            if decoded_with[j] != fichier[j]:
                nb_error_finale += 1
        
        if nb_error != 0:
            X.append(i)
            Y.append(float(nb_error_finale * 1000. / nb_error))
            
        print "Nb Error : " + str(nb_error)
    print X,Y
    
    pp.plot(X,Y)
    plt.xlabel("Taux d'erreur (en %.)")
    plt.ylabel("Taux d'erreur final (en %.)")
    

# BLACK AND WHITE IMAGES

def ImageToHex_BW(image_path):
    im = Image.open(image_path)
    (l, h) = im.size
    C = []
    
    for y in range(h):
        for x in range(l):
            color = Image.Image.getpixel(im, (x, y))
            C.append(rgb_to_hex(color)[0:2])
            
    return C

def hex_to_bin_BW(hex_string):
    bina = bin(int(hex_string, 16))[2:]
    while len(bina) != 8:
        bina = "0" + bina

    return bina

def ImageToBin_BW(image_name): # Block and white images
    C = ImageToHex_BW("Images/" + image_name)
    
    T = ""
    for h in C:
        T += hex_to_bin_BW(h)
        
    fichier = open('Files/' + image_name.split('.')[0] + ".txt", "w")
    fichier.write(T + '\n')
    
def generate_comparation_BW(file_name_image_ref, file_name_image_satured, l, h):
    file_image_ref = open('Files/' + file_name_image_ref + ".txt", "r")
    file_image_corrupted = open('Files/' + file_name_image_satured + ".txt", "r")
    
    C1, C2 = file_image_ref.read(), file_image_corrupted.read()

    im = Image.new("RGB", (l, h), "white")
    pix = im.load()
    
    for y in range(h):
        for x in range(l):
            rang = (y * l + x) * 8
            pix[x, y] = (255,0,0) if C1[rang : rang + 8] != C2[rang : rang + 8] else hex_to_rgb(bin_to_hex(C2[rang : rang + 8]*3))
        
    im.save("Images/COMPARED_" + file_name_image_satured + ".png")
    
    