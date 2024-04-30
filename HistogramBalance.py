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

parser = argparse.ArgumentParser(
                        prog='HistogramBalance.py',
                        description='Histogram balancing on RGB images: Python program that adjusts the histogram of RGB values of a folder of photos to the histogram of a reference image.',
                        epilog="\nversion v.1\n----------------------------------------------------\n"
                        )

parser.add_argument("-ref","--reference", help="reference image path (str)", type=str)           # option that takes a value
parser.add_argument("-s","--source", help="path to the folder with images to be processed", type=str)           # option that takes a value
parser.add_argument('-o', '--output', nargs="?", default=str(os.getcwd())+"\\"+"output", help="-optional- name/path of the folder with processed images to be dumped (Default: pwd/output)", type=str)      # option that takes a value
parser.print_help()

args = parser.parse_args()
ref_file_path = args.reference
source_file_path = args.source
output_file_path = args.output


# MAIN

if __name__ == "__main__":


    # 1- Output folder creation 

    print("\nCreating output file directory")
    try:
        os.mkdir(output_file_path)
    except:
        print("EXITING... DIR not empty")
        exit(1)

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

        print("Reading source files...\n------\n")


        for s_filename in os.listdir(source_file_path):

            print("Processing image"+str(s_filename)+"...\n")
            s_image = Image.open(source_file_path+"\\"+s_filename)
            
            # Convert to numpy
            s_image = conv_numpy(s_image)

            print("Balancing histogram...\n")
            outpic = BalanceHistogram(refimg, s_image)


            print("Writing in PATH: "+str(output_file_path)+"\\"+str(s_filename)+"png\n----------------------------\n")
            cv2.imwrite(output_file_path+"\\"+str(s_filename)+".png", outpic)
    
    else:

        print("EXITING... Source img path not found")
        exit(1)

