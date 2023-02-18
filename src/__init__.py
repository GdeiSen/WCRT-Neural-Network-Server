import cv_service

image_1 = cv_service.CVAgent('tests/image-5.jpeg', 'output.svg')
image_1.params.svg_curves = 1
image_1.params.pass_count = 10
image_1.scan_img()
image_1.show_tests()
image_1.convert_to_svg()
