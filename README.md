# Image processing task wrappers

In-house python scripts for image processing, wrapping functionalities from scikit-learn image, scipy, openCV

* HistogramBalance.py : Command line interface to balance images present in an input folder using a reference image
  
```
usage: HistogramBalance.py [-h] [-ref REFERENCE] [-s SOURCE] [-o [OUTPUT]]

Balance de Histograma en imágenes RGB v1: Programa de python que ajusta el histograma de valores RGB de una carpeta de
fotos al histograma de una imagen de referencia

options:
  -h, --help            show this help message and exit
  -ref REFERENCE, --reference REFERENCE
                        ruta de imagen de referencia (str)
  -s SOURCE, --source SOURCE
                        ruta de la carpeta con imágenes a procesar
  -o [OUTPUT], --output [OUTPUT]
                        -opcional- nombre/ruta de la carpeta con imagenes a volcar

Puede leer TIF/PNG/JPEG.
```
