"""
Autor: Alejandro Gómez
Fecha de última modificación: 20/10/22

"""

from gl import *

# Desplegar resultado
# Referencia: https://www.geeksforgeeks.org/python-pil-image-show-method/
from PIL import Image


def SoftwareRender3(filename):
    r = Render(1920, 1080)
    r.glModel(
        "Sonic.obj",
        translation=V3(1100, 80, 0),
        scalationFactor=V3(50, 50, 50),
    )
    r.glFinish(filename)
    im = Image.open(filename)
    im.show()
