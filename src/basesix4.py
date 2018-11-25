"""
Utils to convert image into a base64 string
"""
import base64

def basesix4(file):
    encoded_string = ""

    with open(file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string

if __name__ == "__main__":
    file = "/home/phani/Projects/manga-dl/Manga/One Punch-Man/vol_000/000_Dh.hKccXTrF.mri.webp"
    print(basesix4(file)[:70])