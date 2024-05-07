import sys
from PIL import Image, ImageOps



image_command = len(sys.argv)
if image_command == 3:                                      # conditional for the number of terminal commands
    try:
        input_image = sys.argv[1].casefold()
        output_image = sys.argv[2].casefold()
        input_ext = input_image.split(".")[-1]              # file extension for input image
        output_ext = output_image.split(".")[-1]            # file extension for output image
        if (
            input_image.endswith(".jpg")
            or input_image.endswith(".jpeg")
            or input_image.endswith(".png")
            or output_image.endswith(".jpg")
            or output_image.endswith(".jpeg")
            or output_image.endswith(".png")
        ):
            if input_ext != output_ext:                     # if input and output have different extensions
                sys.exit("Input and output have different extensions")
            else:
                photo = Image.open(input_image)
                shirt = Image.open("shirt.png")
                size = shirt.size                           # get size of the shirt
                photo = ImageOps.fit(photo, size)           # crop input photo to same size as the shirt
                photo.paste(shirt, shirt)                   # pastes the shirt on the photo
                photo.save(output_image)                    # saves the photo to new file (output_image/sys.argv[2])
        else:
            sys.exit("Invalid output")
    except FileNotFoundError:
        sys.exit("Input does not exist")
elif image_command < 3:
    sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments")



