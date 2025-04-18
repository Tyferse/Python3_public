import os

from PIL.Image import open as load_pic, new as new_pic


def main(path, iterations, name, keep_all=False):
    """
    Params
        path:str
            path to photograph
        iterations:int
            number of iterations to compute
        name:str
            formattable string to use as template for file names
    """
    title = os.path.splitext(os.path.split(path)[1])[0]
    counter = 0
    while counter < iterations:
        with load_pic(path) as image:
            dim = width, height = image.size
            with new_pic(image.mode, dim) as canvas:
                for x in range(width):
                    for y in range(height):
                        # nx = (2 * x + y) % width
                        # ny = (x + 2 * y) % height
                        # nx = round(2 * x**2 / (x**2 + y**2 + 0.01)**0.5 + y) % width
                        # ny = round(x + 2 * y**2 / (x**2 + y**2 + 0.01)**0.5) % height
                        nx = (2 * x - y) % width
                        ny = (-x + 2 * y) % height

                        canvas.putpixel((nx, height-ny-1),
                                        image.getpixel((x, height-y-1)))

        if counter > 0 and not keep_all:
            os.remove(path)
        
        counter += 1
        print(counter, end="\r")
        path = name.format(name=title, index=counter)
        canvas.save(path)

    return canvas


if __name__ == "__main__":
    # path = "Arnolds_Cat\\a\\0.png" #input("Enter the path to an image:\n\t")
    # result = main(path, 31, "Arnolds_Cat\\a\\aea.png")
    # result.show()
    
    ifolder = "Python3\Sandbox#py\ArnoldsCatMap\\frames7\\"
    for i in range(256):
        path = ifolder + str(i) + ".png"
        result = main(path, 2, ifolder + str(i + 1) + ".png")
        print(str(i) + '\'s frame')
        # result.show()
