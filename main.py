import cv2 as cv
import numpy as np


class CVAgent:
    def __init__(self, imgpath, outpath):
        self.img = None
        self.contours = None
        self.edges = None
        self.grey = None
        self.blur = None
        self.imgpath = imgpath
        self.outpath = outpath

    def scanimg(self):
        img = cv.imread(self.imgpath)
        img_blur = cv.medianBlur(img, 3)
        img_grey = cv.cvtColor(img_blur, cv.COLOR_BGR2GRAY)
        img_edges = cv.Canny(img_grey, 50, 200)
        thresh = 100
        ret, img_thresh = cv.threshold(img_edges, thresh, 255, cv.THRESH_BINARY)
        contours, hierarchy = cv.findContours(img_thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        self.img = img
        self.blur = img_blur
        self.grey = img_grey
        self.edges = img_edges
        self.contours = contours

    def showexmpls(self):
        cv.imshow('original image', self.img)
        cv.imshow('blur image', self.blur)
        cv.imshow('edged image', self.edges)
        img_contours = np.uint8(np.zeros((self.img.shape[0], self.img.shape[1])))
        cv.drawContours(img_contours, self.contours, -1, (255, 255, 255), 10)
        cv.imshow('contoured image', img_contours)
        cv.waitKey()
        cv.destroyAllWindows()

    def tosvg(self):
        with open(self.outpath, "w+") as f:
            f.write(
                f'<svg width="{self.img.shape[0]}" height="{self.img.shape[1]}" xmlns="http://www.w3.org/2000/svg">')
            for c in self.contours:
                f.write('<path d="M')
                for i in range(len(c)):
                    x, y = c[i][0]
                    if i == 1:
                        f.write("C")
                    if i % 2 == 0:
                        f.write(f"{x} {y} ")
                f.write('" style="stroke:black"/>')
            f.write("</svg>")
        f.close()


image_1 = CVAgent('tests/image-2.jpeg', 'output.svg')
image_1.scanimg()
image_1.showexmpls()
image_1.tosvg()
