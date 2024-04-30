# CIB NATALIA GARCÍA SANCHEZ
# FECHA: 30/04/2022
# v1
# --
# Descripción: Programa de python que ajusta el histograma de valores RGB de una carpeta de fotos al histograma de una imagen de referencia

# IMPORT LIBRARIES

import os
import argparse

import cv2
import numpy as np
from PIL import Image
from skimage.exposure import match_histograms

Image.MAX_IMAGE_PIXELS = None






# METHODS

def conv_numpy(img):
    """Converts pictures in PIL Image format to numpy array
    
    img: class Image (PIL.Image.Image)"""
    return np.array(img)


def BalanceHistogram(reference, source):
    """Wrapper of method scikit-image.exposure.match_histograms
    takes reference and source pictures in numpy array format
    
    reference, source: class np.array (np.array(region))"""

    # balance histogram and convert to RGB color code (PIL source image read)
    matched = match_histograms(source, reference, channel_axis=-1)
    matched = cv2.cvtColor(matched, cv2.COLOR_BGR2RGB)
    return matched 





# MAIN

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                        prog='Balance de Histograma en imágenes RGB v1',
                        description='Programa de python que ajusta el histograma de valores RGB de una carpeta de fotos al histograma de una imagen de referencia',
                        epilog="\n Puede leer TIF/PNG/JPEG. \n\nArgumentos \n------------\n (1) -ref : imagen de referencia \n (2) -s : source- ruta de la carpeta con imágenes a procesar \n (3) -o: (opcional) nombre/ruta de la carpeta con imagenes a volcar"
                        )

    parser.add_argument("-ref","--reference", type=str)           # option that takes a value
    parser.add_argument("-s","--source", type=str)           # option that takes a value
    parser.add_argument('-o', '--output', nargs="?", default=str(os.getcwd()), type=str)      # option that takes a value

    args = parser.parse_args()
    ref_file_path = args.reference
    source_file_path = args.source
    output_file_path = args.output


    # Argument recognition

    # 1- Output folder creation 

    if output_file_path:

        if len(os.listdir("prueba")) == 0:
        
            print("EXITING... Output folder already exists")
            exit(1)

        else:

            print("Creating output file directory")
            os.mkdir(output_file_path)

    # 2- Reading reference image in TIF/PNG/JPEG format

    if ref_file_path: 

        print("Reading reference file...\n")
        # Leer la imagen
        ref_image = Image.open(ref_file_path)
        # Convert to numpy
        refimg = conv_numpy(ref_image)

    else:

        print("EXITING... Error reading reference file")
        exit(1)


    # 3- Walking (un-nested) file directory for histogram balancing, save img

    if source_file_path: #

        print("Reading source files...\n")
        # Leer la imagen

        ref_image = Image.open(source_file_path)

        for s_filename in os.listdir(source_file_path):

            print("Processing image"+str(s_filename)+"...")
            s_image = Image.open(s_filename)
            
            # Convert to numpy
            s_image = conv_numpy(s_image)

            print("Balancing histogram...")
            outpic = BalanceHistogram(refimg, s_image)


            print("Writing in"+str(output_file_path)+"\\\\"+str(s_filename)+"png\n----------------------------\n")
            cv2.imwrite(output_file_path+"\\\\"+str(s_filename)+".png", outpic)
    
    else:

        print("EXITING... Source img path not found")
        exit(1)

