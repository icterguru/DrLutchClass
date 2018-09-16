import sys


def print_ppm(height):
    width = 2 * height
    print ("PPM")
    print (width, " ", height)
    print ("255")

    for i in range (height):
        for j in range(width):
            if j == width/2 - i or j == width -  1:
                print("255 255 255")
            elif j <= i:
                print ("255 0 0")
            elif j >= i + width/2:
                print ("0 0 255")
            else:
                print ("0 255 0")



def main():
    height = int(sys.argv[1])
    if height > 1280:
        print("Input height mush be at most 1280 pixels height", file = sys.stderr)
    elif height <=1:
        print("Input height should be at least 2 pixels height", file = sys.stderr)

    else: 
        print_ppm(height)


main()
