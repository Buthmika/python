import sys
import os

# Print which Python interpreter is running this script (helps find which pip to use)
print(f"Running Python: {sys.executable} (version {sys.version.split()[0]})")
print("sys.path preview:", sys.path[:3])

try:
    from PIL import Image
except ImportError:
    print("Pillow (PIL) is not installed in this Python environment.")
    print("Install it for the exact Python you're using with:")
    print(f'  "{sys.executable}" -m pip install pillow')
    sys.exit(1)

from tkinter.filedialog import *
file_path=askopenfilename()
img=Image.open(file_path)
myHeight,myWidth=img.size
img=img.resize((myHeight,myWidth),Image.ANTIALIAS)
save_path=asksaveasfilename()
img.save(save_path+"Compressed.jpg")