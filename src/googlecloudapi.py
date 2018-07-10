import requests, json, shutil, os
from basesix4 import basesix4

def saveImage(image_url, image_path = "./default.jpg"):
    """
    Downloads the given image and stores at the given place

    Defaut:
        ./default.jpg
    """

    success = False

    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    r = requests.get(image_url, stream=True)

    if r.status_code == 200:
        with open(image_path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
            success = True

    return success



def getCloudAPIDetails(image_path):
    """
    Uses google's cloud api to get json data (unofficial)

    VISIT:
        https://cloud.google.com/vision/

    and inspect to know what the website does when an image is uploaded

    Capability:

        VERY LIMITED
    """

    url = "https://cxl-services.appspot.com/proxy?url=https%3A%2F%2Fvision.googleapis.com%2Fv1%2Fimages%3Aannotate"

    data = {
        "requests":[
            {
                "image":{
                    "content":"/"
                },
                "features":[
                    {
                    "type":"TYPE_UNSPECIFIED","maxResults":50
                    },
                    {
                    "type":"LANDMARK_DETECTION","maxResults":50
                    },
                    {
                    "type":"FACE_DETECTION","maxResults":50
                    },
                    {
                    "type":"LOGO_DETECTION","maxResults":50
                    },
                    {
                    "type":"LABEL_DETECTION","maxResults":50
                    },
                    {
                    "type":"DOCUMENT_TEXT_DETECTION","maxResults":50
                    },
                    {
                    "type":"SAFE_SEARCH_DETECTION","maxResults":50
                    },
                    {
                    "type":"IMAGE_PROPERTIES","maxResults":50
                    },
                    {
                    "type":"CROP_HINTS","maxResults":50
                    },
                    {
                    "type":"WEB_DETECTION","maxResults":50
                    }
                ],
                "imageContext":{
                    "cropHintsParams":{
                        "aspectRatios":[0.8,1,1.2]
                    }
                }
            }
        ]
    }

    image_dataURI = basesix4(image_path).decode('utf-8')

    data["requests"][0]["image"]["content"] = image_dataURI

    r = requests.post(url,json=data)

    return r.json()

if __name__ == "__main__":
    image_path = "/home/phani/Projects/manga-dl/Manga/One Punch-Man/vol_000/000_Dh.hKccXTrF.mri.webp"
    print(getCloudAPIDetails(image_path))