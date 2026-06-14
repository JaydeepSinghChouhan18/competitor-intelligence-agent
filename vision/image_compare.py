from PIL import Image
from PIL import ImageChops


def compare_images(
    old_image,
    new_image
):

    img1 = Image.open(
        old_image
    )

    img2 = Image.open(
        new_image
    )

    diff = ImageChops.difference(
        img1,
        img2
    )

    if diff.getbbox():

        return True

    return False    