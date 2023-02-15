import predict_image as image
import return_color as color


def save_data(file):
    """ Returns predicted clothing Item and its color from file.
        Further purposes are to save the data in a csv file and instead
        of a written text, it should return the clothes images from
        the user """

    clothing = image.predict(file)
    cloth_color = color.get_color(file)
    return clothing, cloth_color
