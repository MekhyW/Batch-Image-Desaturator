try:
    import sys
    from PIL import Image
    newname = input('Type the filename: ')
except:
    print("UNABLE TO IMPORT PILLOW")
counter = 0
try:
    print(sys.version)
    for myfile in sys.argv[1:]:
        counter += 1
        img = Image.open(myfile).convert('LA')
        img.save("{}-{}.png".format(newname, counter))
        print("generated grayscale image: " + "{}-{}.png".format(newname, counter))
    print("SUCCESS!")
except:
    print("AN ERROR HAS OCCURRED")
input("...press enter to close")