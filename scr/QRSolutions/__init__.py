import functools
from .TypeSelector import Generator  # takes string and error correction level, returns file
from .ByteEncoding import Byte  # takes string for byte encoding and error correction level, returns file
from .AlphaNumericEncoding import AlphaNum  #takes an alphaNumeric string and error correction, returns file
from .numericEncoder import Numeric  # takes a numeric string and error correction level, returns file
from .KanjiEncoding import Kanji  # takes a Kanji string and error correction level, returns file

print("Thanks for Installing QRSolution! Documentation at link \nCurrent Version is 0.0.1")

import os

try:
    import PIL
except:
    os.system("pip install pillow")

try:
   import tqdm
except:
   os.system("pip install tqdm")