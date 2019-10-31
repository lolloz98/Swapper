# Swapper
## Usage:
Swap squares of pixels (big pixels) inside of an image.  
Save the new image and the permutation of the big pixels (read as a matrix row by row).

## Requirements:
1. python 3.7
2. libraries (install with pip):
   - math
   - multipledispatch
   - pillow

## How to use:
Launch mainSwapper.py.  
Follow the instructions. Every path MUST end with "." + extension (e.g. .txt, .png).  
The img_length and the img_height must be multiple of the big pixel dimension (-> number of pixels on one of its sides).  
IMP: after every swap the img (in the output path) and the sol (in the output path) are saved.  
- if, after the first swap, you open the output img and/or the otput sol and keep swapping big pixel, you'll be able to see
	the results in real time
