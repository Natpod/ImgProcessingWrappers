# Image processing task wrappers

In-house python scripts for image processing, wrapping functionalities from scikit-learn image, scipy, openCV

## 1. Histogram Balance

HistogramBalance.py : Command line interface to balance images present in an input folder using a reference image

#### How to

install miniconda, requirements in `requirements.txt`

```
usage: HistogramBalance.py [-h] [-ref REFERENCE] [-s SOURCE] [-o [OUTPUT]]

Histogram balancing on RGB images: Python program that adjusts the histogram of RGB values of a folder of photos to
the histogram of a reference image.

options:
  -h, --help            show this help message and exit
  -ref REFERENCE, --reference REFERENCE
                        reference image path (str)
  -s SOURCE, --source SOURCE
                        path to the folder with images to be processed
  -o [OUTPUT], --output [OUTPUT]
                        -optional- name/path of the folder with processed images to be dumped

version v.1 ----------------------------------------------------
```

TODO: Works currently for windows path file format, support for Linux
