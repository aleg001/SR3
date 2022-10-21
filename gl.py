"""
Autor: Alejandro Gómez
Fecha de última modificación: 20/10/22

"""

# Modulo para estructura de bytes
import struct


# Para objetos
from ObjectOpener import *


# definiciones de estructuras bytes
def char(c):
    return struct.pack("=c", c.encode("ascii"))


def word(w):
    return struct.pack("=h", w)


def dword(d):
    return struct.pack("=l", d)


def color(r, g, b):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])


# Constates de bytes
firstW = word(1)
word24 = word(24)
headerInfo1 = 14 + 40
Dcero = dword(0)
Wcero = word(0)
w40 = dword(40)

# Valores constantes a usar de colores
color1 = "white"
color2 = "black"
color3 = "blue"


# funcion para colores a usar
def BasicColors(const):
    if const == "white":
        return color(1, 1, 1)
    if const == "black":
        return color(0, 0, 0)
    if const == "blue":
        return color(0, 1, 1)


"""
Math operations

Referencias: 
https://stackoverflow.com/questions/28253102/python-3-multiply-a-vector-by-a-matrix-without-numpy
https://stackoverflow.com/questions/10508021/matrix-multiplication-in-pure-python
https://mathinsight.org/matrix_vector_multiplication
https://www.mathsisfun.com/algebra/matrix-multiplying.html

"""


def VerifyIntegers(value):
    try:
        value = int(value)
    except:
        print("Error")


def matrixMultiplications(matrixList) -> list:
    matrixLength = len(matrixList)
    matrixResult = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(0, matrixLength):
        if i == 0:
            matrix = matrixList[i]
        matrixValue = len(matrix)
        secondMatrix = matrixList[i + 1]
        for x in range(0, matrixValue):
            for y in range(0, matrixValue):
                r = 0
                for z in range(0, matrixValue):
                    r += matrix[x][z] * secondMatrix[z][y]
                matrixResult[x][y] = float(r)
        if i + 2 == len(matrixList):
            break
    return matrixResult


def matrixMultiplication4x4(matrix, vector):
    valueFinal = [0, 0, 0, 0]

    v4 = [
        [vector.x],
        [vector.y],
        [vector.z],
        [vector.w],
    ]

    for x in range(0, len(matrix)):
        tempValue = 0
        for y in range(0, len(matrix[x])):
            tempVariable = matrix[x][y] * v4[y][0]
            tempValue += float(tempVariable)
        valueFinal[x] = tempValue
    return valueFinal


from collections import *

V2 = namedtuple("Point2", ["x", "y"])
V3 = namedtuple("Point3", ["x", "y", "z"])
V4 = namedtuple("Point4", ["x", "y", "z", "w"])


class Render(object):
    # (05 puntos) Deben crear una función glInit() que inicialice cualquier objeto interno que requiera su software renderer
    def __init__(self, width, height):
        self.glCreateWindow(width, height)
        self.clearColor = BasicColors(color2)
        self.currentColor = BasicColors(color1)
        self.glClear()

    # (05 puntos) Deben crear una función glCreateWindow(width, height) que inicialice su framebuffer con
    # un tamaño (la imagen resultante va a ser de este tamaño).
    def glCreateWindow(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.glViewPort(0, 0, self.width, self.height)

    # (10 puntos)  Deben crear una función glViewPort(x, y, width, height) que defina el área de la imagen sobre la que se va a poder dibujar
    def glViewPort(self, x, y, width, height):
        self.viewPortX = int(x)
        self.viewPortY = int(y)
        self.viewPortWidth = int(width)
        self.viewPortHeight = int(height)

    # (10 puntos) Deben crear una función glClearColor(r, g, b) con la que se pueda cambiar el color con el que funciona glClear().
    # Los parámetros deben ser números en el rango de 0 a 1.
    def glClearColor(self, r, g, b):
        self.clearColor = color(r, g, b)

    # (15 puntos) Deben crear una función glColor(r, g, b) con la que se pueda cambiar el color con el que funciona glVertex().
    # Los parámetros deben ser números en el rango de 0 a 1
    def glColor(self, r, g, b):
        self.currentColor = color(r, g, b)

    # (20 puntos) Deben crear una función glClear() que llene el mapa de bits con un solo color
    def glClear(self):
        self.pixels = [
            [self.clearColor for y in range(self.height)] for x in range(self.width)
        ]

    def glClearViewPort(self, cl=None):
        for x in range(self.viewPortX, self.viewPortX + self.viewPortWidth):
            for y in range(self.viewPortY, self.viewPortY + self.viewPortHeight):
                self.glPoint(x, y, cl)

    def glPoint(self, x, y, cl=None):
        if 0 <= x < self.width:
            if 0 <= y < self.height:
                self.pixels[x][y] = cl or self.currentColor

    def glLine(self, x0: V2, x1: V2, cl=None):
        tempX0 = int(x0.x)
        tempX1 = int(x1.x)
        tempY0 = int(x0.y)
        tempY1 = int(x1.y)

        if tempX0 == tempX1 and tempY0 == tempY1:
            self.glPoint(tempX0, tempY0, cl)
            return

        dy = tempY1 - tempY0
        dx = tempX1 - tempX0

        dy = abs(dy)
        dx = abs(dx)

        pendiente = dy > dx

        if pendiente == True:
            tempX0, tempY0 = tempY0, tempX0
            tempX1, tempY1 = tempY1, tempX1

        if pendiente == False:
            tempX0, tempY0 = tempX0, tempY0
            tempX1, tempY1 = tempX1, tempY1

        x1Bx0 = tempX1 < tempX0

        if x1Bx0 == True:
            tempX0, tempX1 = tempX1, tempX0
            tempY0, tempY1 = tempY1, tempY0

        if x1Bx0 == False:
            tempX0, tempX1 = tempX0, tempX1
            tempY0, tempY1 = tempY0, tempY1

        dx = tempX1 - tempX0
        dy = tempY1 - tempY0

        dy = abs(dy)
        dx = abs(dx)

        offset = 0
        limite = 0.5
        ecuacionRecta = dy / dx
        finalY = tempY0

        x1MasUno = tempX1 + 1

        for i in range(tempX0, x1MasUno):
            if pendiente == True:
                self.glPoint(finalY, i, cl)
            else:
                self.glPoint(i, finalY, cl)
            offset += ecuacionRecta
            if offset >= limite:
                finalY = finalY + 1 if tempY0 < tempY1 else finalY - 1
                limite += 1

    def glModel(
        self,
        filename,
        translation=V3(0, 0, 0),
        rotation=V3(0, 0, 0),
        scalationFactor=V3(1, 1, 1),
    ):

        modelImport = ObjectOpener(filename)
        mMatrix = self.glCreateMatrix(translation, rotation, scalationFactor)

        for i in modelImport.faces:

            f1Temp = i[0][0] - 1
            f2Temp = i[1][0] - 1
            f3Temp = i[2][0] - 1

            f1 = modelImport.vertices[f1Temp]
            f2 = modelImport.vertices[f2Temp]
            f3 = modelImport.vertices[f3Temp]

            f1Transformed = self.glTransform(f1, mMatrix)
            f2Transformed = self.glTransform(f2, mMatrix)
            f3Transformed = self.glTransform(f3, mMatrix)

            self.glTriangle(
                f1Transformed, f2Transformed, f3Transformed, BasicColors(color3)
            )

    def glTransform(self, vertex, matrix):
        tempVertex = V4(vertex[0], vertex[1], vertex[2], 1)
        final = matrixMultiplication4x4(matrix, tempVertex)

        f0 = final[0]
        f3 = final[3]
        f1 = final[1]
        f2 = final[2]

        f03 = f0 / f3
        f13 = f1 / f3
        f23 = f2 / f3

        return V3(f03, f13, f23)

    def glTriangle(self, A: V3, B: V3, C: V3, co=None):
        biggerAB_Y = A.y < B.y
        biggerAC_Y = A.y < C.y
        biggerBC_Y = B.y < C.y

        if biggerAB_Y == True:
            A, B = B, A
        if biggerAB_Y == False:
            A, B = A, B

        if biggerAC_Y == True:
            A, C = C, A
        if biggerAC_Y == False:
            A, C = A, C

        if biggerBC_Y == True:
            B, C = C, B
        if biggerBC_Y == False:
            B, C = B, C

        self.glLine(A, B, co)
        self.glLine(B, C, co)
        self.glLine(C, A, co)

    def glCreateMatrix(
        self, translation=V3(0, 0, 0), rotation=V3(0, 0, 0), scalationFactor=V3(1, 1, 1)
    ):

        rot = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

        tr1Row = [1, 0, 0, translation.x]
        tr2Row = [0, 1, 0, translation.y]
        tr3Row = [0, 0, 1, translation.z]
        tr4Row = [0, 0, 0, 1]

        traslateMatrix = [tr1Row, tr2Row, tr3Row, tr4Row]

        xRow = [scalationFactor.x, 0, 0, 0]
        yRow = [0, scalationFactor.y, 0, 0]
        zRow = [0, 0, scalationFactor.z, 0]
        lastRow = [0, 0, 0, 1]
        rowlist = [xRow, yRow, zRow, lastRow]

        matrixListing = [traslateMatrix, rot, rowlist]

        matrixMultiplicationActual = matrixMultiplications(matrixListing)

        return matrixMultiplicationActual

    def glFinish(self, filename):
        # constantes y calculos
        headerSize = headerInfo1 + (self.width * self.height * 3)
        widthD = dword(self.width)
        heightD = dword(self.height)
        whD = dword(self.width * self.height * 3)

        with open(filename, "wb") as f:
            f.write(char("B"))
            f.write(char("M"))
            f.write(dword(headerSize))
            f.write(Wcero)
            f.write(Wcero)
            f.write(dword(headerInfo1))
            f.write(w40)
            f.write(widthD)
            f.write(heightD)
            f.write(firstW)
            f.write(word24)
            f.write(Dcero)
            f.write(whD)
            f.write(Dcero)
            f.write(Dcero)
            f.write(Dcero)
            f.write(Dcero)

            for y in range(0, self.height):
                for x in range(0, self.width):
                    f.write(self.pixels[x][y])
            f.close()
