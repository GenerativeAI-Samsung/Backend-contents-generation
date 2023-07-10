from rembg import remove
import cv2
def removebackground(inputpath):
    input_path = inputpath
    index = input_path.rfind('.')
    length = len(input_path)
    output_path = input_path[0:index] + 'output' + input_path[index:length]
    subtract_path = input_path[0:index] + 'subtract' + input_path[index:length]
    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
                input = i.read()
                output = remove(input)
                o.write(output)

