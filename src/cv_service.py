import cv2 as cv
import numpy as np


class CVAgentParams:
    blurfilter = 3
    greyfilter = 50
    svg_curves = 0
    svg_string = 'style="stroke:black" fill="none" stroke-width="6"'
    pass_count = 2


class CVAgent:
    def __init__(self, img_path, out_path):
        self.img = None
        self.contours = None
        self.edges = None
        self.grey = None
        self.blur = None
        self.params = CVAgentParams()
        self.img_path = img_path
        self.out_path = out_path

    def scanimg(self):
        img = cv.imread(self.img_path)
        img_blur = cv.medianBlur(img, 7)
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
        cv.drawContours(img_contours, self.contours, -1, (255, 255, 255), 4)
        cv.imshow('contoured image', img_contours)
        cv.waitKey()
        cv.destroyAllWindows()

    def tosvg(self):
        with open(self.out_path, "w+") as f:
            f.write(
                f'<svg width="{3000}" height="{2000}" xmlns="http://www.w3.org/2000/svg">')
            for c in self.contours:
                f.write('<path d="M')
                pass_count = self.params.pass_count
                point_counter = 0
                for i in range(len(c)):
                    x, y = c[i][0]
                    if i % 2 == 0:
                        f.write(f"{x} {y} ")
                        point_counter += 1
                        if point_counter == 1 and self.params.svg_curves == 1:
                            f.write("C")
                    elif pass_count >= 1:
                        pass_count -= 1
                    else:
                        pass_count = 0
                f.write(f'" {self.params.svg_string} />')
            f.write("</svg>")
        f.close()