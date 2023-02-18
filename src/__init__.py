import cv_service

image_1 = cv_service.CVAgent('tests/image-5.jpeg', 'output.svg')
image_1.params.svg_curves = 1
image_1.params.pass_count = 10
image_1.scanimg()
image_1.showexmpls()
image_1.tosvg()
