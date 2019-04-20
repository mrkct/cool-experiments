# Radiohead-like Album Art Generator
## What is this
A simple script to generate an image in the style of Radiohead's 'In Rainbows' album cover

## How to run it
Install `Pillow`, open `generate.py` and change `main_text` and `lower_text` and `FONT_SIZE` to your liking. Run:

    pip install Pillow
    python generate.py

To change the background just substitute the `background.png` file with your background. This script will create a `output.png` file.
## What is missing
- The real album cover without the writings.
- Automatic font size calculations, this is an np-hard problem apparently!
## Notes
- None