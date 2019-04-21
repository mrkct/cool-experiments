# Image to Ascii Converter
## What is this
A simple script to convert an image to an ASCII text version

## How to run it
Install `Pillow`, run the script with the image to convert as an argument:

    pip install Pillow
    python to-ascii.py python.jpg

You can also pass an extra argument, an integer, that represents the size of 
the squares that are used to represent a single character. Basically, that means
the lower the number the more accurate it will be, but also larger. Defaults to 
8, which makes pretty good images but still small enough

## Notes
- I copied the map from light to ascii char from this link [https://www.codeproject.com/Articles/20435/Using-C-To-Generate-ASCII-Art-From-An-Image](https://www.codeproject.com/Articles/20435/Using-C-To-Generate-ASCII-Art-From-An-Image)