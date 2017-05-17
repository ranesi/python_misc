from PIL import Image
import sys
import os

    #Can edit this to create alternate palette of characters.
    #Characters arranged from 'light' to 'dark'.
ascii_pixels = [
        ' ',
        '.',
        '=',
        '*',
        'u',
        'W',
        '8',
        '&'
    ]

def ascii_art(filename=None):

    if filename is None:
        if (len(sys.argv) < 2):
            sys.exit("Please specify a filename")

        filename = sys.argv[1];

    lines = 40

    try :
        img = Image.open(filename)
    except FileNotFoundError:
        exit("Sorry, that file not found")
    except OSError:
        exit("That file doesn't seem to be an image")

    art = ascii(img, lines)

    write_to_file(art, filename)


def ascii(img, lines):

    h = img.height    #Height & width of original image, in pixels
    w = img.width

    ascii = ""  #Will contain our ascii picture; a string of characters with newlines in.

    y_boxes = lines   #Since displaying in terminal, will make picture 35 lines tall.
    y_box_pix = int(h / lines)     #How many pixels on one line?

    x_box_pix = int(y_box_pix / 2) #Use half as many pixels - a character is narrower than tall.
    x_boxes = int(w / x_box_pix)  # And compute the number of x_boxes from the pixels from x squares.

    if x_box_pix < 1 or y_box_pix < 1 :
        print("Image too small, or number of lines is too large.")
        return

    #Loop over all of the boxes....

    for ybox in range(0, y_boxes):

        for xbox in range(0, x_boxes):

            left = xbox * x_box_pix
            upper = ybox * y_box_pix
            right = left + x_box_pix
            lower = upper + y_box_pix

            #Crop this box and return as new image.
            #The min calls are to constrain the right/lower corner of box within the dimensions
            #of the image.
            cropbox = img.crop((left, upper, min(right, w-1), min(lower, h-1)));

            colors = cropbox.getcolors()   #Extract colors as "an unsorted list of count, pixel values"

            #Identify most popular RGB color in this box; we'll call this "average" color
            avg = avg_col(colors);

            #Turn this color into a grayscale color - a single number in range 0-255
            gray = color_to_gray(avg)

            #And transform this average color into one of our ASCII character 'pixels'
            pixel = ascii_pix(gray)

            ascii += pixel

        ascii += '\n'

    print(ascii)
    return ascii


def avg_col(colors):

    #Example of colors; a list of ( frequency, (r,g,b) ) tuples of the most popular colors in this image;
    #the frequencies seem to be normalized to add up to 16.

    # [(2, (124, 84, 33)), (5, (125, 83, 33)), (3, (126, 82, 33)), (4, (124, 82, 32)), (2, (125, 81, 32))]

    unknown = (0, 0, 0)

    if colors is None:
        return unknown  #If any part of the cropbox boundary is outside the image, colors will be None.
    if len(colors) == 0:
        return unknown

    mostpopindex = 0

    occurance = colors[0][0]

    for c in range(len(colors)):
        if colors[c][0] > occurance:
            occurance = colors[c][0]
            mostpopindex = c

    pop_color = colors[mostpopindex][1]

    return pop_color


def color_to_gray(color):

    gray = 0.3 * color[0] + 0.6 * color[1] + 0.1 * color[2]
    #http://stackoverflow.com/questions/687261/converting-rgb-to-grayscale-intensity
    #Rounded to nearest 0.1, it doesn't matter if we are not perfectly accurate

    #make sure in range 0 to 255.

    if gray < 0:
        return 0
    if gray > 255:
        return 255

    return int(gray);



def ascii_pix(color):

    #color is a number between 0 and 255
    #divide by 24

    val = 255-color;

    index = int(val/32)

    #val in range 0-255. We only have 8 different pixels.
    #Divide gray by 32 to reduce range to 0-7.

    return ascii_pixels[index];


def write_to_file(art, filename):

    # Split into filename and path; add ASCII_ prefix to file name
    dir_name, file_name = os.path.split(filename)

    # Remove extension, if present - replace with .txt
    base, extension = os.path.splitext(file_name)
    file_name = base + '.txt'

    file_name = "ASCII_" + file_name

    filepath = os.path.join(dir_name, file_name)

    # Does this file exist?

    if os.path.isfile(filepath):
        # File already exists
        print('Did not write art to file - file already exists')
        return

    with open(filepath, 'w') as f:
        f.write(art)


def main():
    ascii_art()


if __name__ == '__main__':
    #Running this as a script: call the main method.
    main()

else:
    #Importing this module from somewhere else; for example, a test case
    #Without this, the main method would be run when the module is imported into the
    #test case, which is probably not the behavior you want,
    #You don't need the else clause for this if statment
    #but I added it so I had somewhere to write this comment.
    pass
