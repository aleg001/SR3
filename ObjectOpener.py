"""
Created by:
Alejandro Gomez

Features:
Loading an object from a file
to use it on the renderer.

Fecha de última modificación: 20/10/22

"""


class ObjectOpener:
    def __init__(self, filename):
        with open(filename, "r") as file:
            self.lines = file.read().splitlines()
        self.vertices = []
        self.faces = []
        self.glLines1()

    def glLines1(self):
        for i in self.lines:
            try:
                prefix, value = i.split(" ", 1)
            except:
                continue
            if prefix == "v":
                self.vertices.append(list(map(float, value.split(" "))))
            elif prefix == "f":
                self.faces.append(
                    [list(map(int, vert.split("/"))) for vert in value.split(" ")]
                )
