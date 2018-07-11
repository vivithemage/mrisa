# MRISA

---

MRISA (**M**eta **R**everse **I**mage **S**earch **A**PI) is a RESTful API which takes an image URL, does a reverse Google image search, and returns a JSON array with the search results.

## Usage

Install the necessary dependencies:

```shell
pip install certifi flask pycurl beautifulsoup4 flask_cors
```

Or

```shell
pip install -r requirements.txt
```

Start the server with:

```shell
python src/server.py
```

## API

### Perform a Reverse Image Search

Performs a reverse image search using the supplied image URL as input.

### URL

- *[http://localhost/search/](http://localhost/search/)*

### Arguments

- *__image_url__* - A URL to an image to use for the search input.

### Request Example

#### CURL

```shell
curl -X POST http://localhost:5000/search \
    -H "Content-Type: application/json" \
    -d '{
        "image_url":
            "http://placehold.it/350x150.png",
        "resized_images":true
        }'
```

#### XMLHttpRequest

```javascript

    var xhr = new XMLHttpRequest();

    xhr.open('POST',"http://localhost:5000/search");

    //Important
    xhr.setRequestHeader("Content-Type","application/json");

    data= {
        "image_url":"http://placehold.it/350x150.png",
        "resized_images":false // Or true
        };

    json = JSON.stringify(data);

    xhr.onreadystatechange = gotDetails;

    xhr.send(json);

    var gotDetails = () => {
        //Got The response
        console.log(xhr.responseText);
    };

```

#### Python request example

```python
import requests, json

url = "http://localhost:5000/search"

data = {
    "image_url":"http://placehold.it/350x150.png",
    "resized_images":True, # Or False
    "cloud_api":True
}


headers = {'Content-type': 'application/json'}
r = requests.post(url, headers=headers, data=json.dumps(data))

#r.json to get the response as json
print(r.json())

#r.text for no u'' characters
```

### Response Example (for the above request)

Shortened to 3 resized_image objects out of 20

<details>

<summary>Expand to view</summary>

<br>

```shell

{
    "best_guess": "placeholder img",
    "descriptions": [
        "Just put your image size after our URL and you'll get a placeholder image. Like this: http://via.placeholder.com/350x150. You can also use it in your code, like\u00a0...",
        "Custom URLs generate placeholder pictures in various sizes with categories and effects. ... Use the buttons above to create the type of image you need. You can\u00a0...",
        "689 \u00d7 300 - Apr 5, 2012 - If you're after a quick and easy way to produce flexible placeholder images for your site, check this out!",
        "350 \u00d7 150 - Which Image Formats Work? Placeholder work with GIF, JPEG, JPG or PNG formats. Just add an image extension to render the image in the format you want.",
        "350 \u00d7 150 - Apr 12, 2018 - I want to create an image with dynamic size like placeholder.com, below is the code to create image with golang: width = 350 height = 150 img\u00a0...",
        "350 \u00d7 150 - Apr 12, 2018 - I want to create an image with dynamic size like placeholder.com, below is the code to create image with golang: width = 350 height = 150 img\u00a0...",
        "450 \u00d7 150 - Jan 29, 2018 - packed-img-strip is a jQuery responsive equal height plugin which automatically ... 02, < img src = \"http://via.placeholder.com/300x300\" />\u00a0..."
    ],
    "links": [
        "https://placeholder.com/",
        "https://placeimg.com/",
        "https://premium.wpmudev.org/blog/image-placeholder/",
        "https://digital.com/tools/placeholder-images/",
        "https://stackoverflow.com/questions/49787206/draw-number-like-placeholder-com-with-golang",
        "https://stackoverflow.com/questions/49787206/draw-number-like-placeholder-com-with-golang?noredirect=1&lq=1",
        "https://www.jqueryscript.net/layout/jQuery-Responsive-Equal-Height-Images.html"
    ],
    "resized_images": [
        {
            "cb": 21,
            "cl": 21,
            "cr": 21,
            "ct": 21,
            "id": "6aNqqL0gKIoXoM:",
            "isu": "demos1.softaculous.com",
            "itg": 0,
            "ity": "",
            "oh": 540,
            "ou": "https://placehold.it/1900x540&text=Slide%20One",
            "ow": 1900,
            "pt": "CSZ Home | CSZ CMS Starter",
            "rh": "demos1.softaculous.com",
            "rid": "UG-EsErbGOiH7M",
            "rt": 0,
            "ru": "https://demos1.softaculous.com/CSZ_CMS/",
            "s": "Caption One",
            "sc": 1,
            "st": "Softaculous",
            "th": 119,
            "tu": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT00elB19-tlgLm8Icu1EgDmpiv1hKh1bJsy699M8r4ezFQHMno2Q",
            "tw": 422
        },
        {
            "cb": 21,
            "cl": 21,
            "cr": 21,
            "ct": 21,
            "id": "cESt2PZwCgUg6M:",
            "isu": "eyurtlar.com",
            "itg": 0,
            "ity": "png",
            "oh": 701,
            "ou": "https://www.eyurtlar.com/images/detaygorselyok.png",
            "ow": 1080,
            "pt": "Yakamoz Be\u015fikta\u015f K\u0131z \u00d6\u011frenci Yurdu | Eyurtlar.com",
            "rh": "eyurtlar.com",
            "rid": "tzcWrjUMKPm9bM",
            "rt": 0,
            "ru": "https://www.eyurtlar.com/istanbul-yakamoz-besiktas-kiz-ogrenci-yurdu/580",
            "s": "Yakamoz Be\u015fikta\u015f K\u0131z \u00d6\u011frenci Yurdu",
            "sc": 1,
            "st": "\u0130stanbul \u00d6zel Yurtlar | \u00d6\u011frenci Apart Rehberi",
            "th": 181,
            "tu": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9LeeXUjP0b9JYWnk8G_6o5Caf8Rm19gQH3H6UISXQoFGBIrIAcg",
            "tw": 279
        },

        # 17 more...

        {
            "cb": 21,
            "cl": 21,
            "cr": 21,
            "ct": 21,
            "id": "DZMVBEHnNZ1t7M:",
            "isu": "feedyeti.com",
            "itg": 0,
            "ity": "",
            "oh": 302,
            "ou": "http://cdn.crownmediadev.com/dims4/default/16e50bf/2147483647/thumbnail/704x436%5E/quality/90/?url=http%3A%2F%2Fbrightcove04.o.brightcove.com%2F3388362517001%2F3388362517001_3868818829001_video-still-for-video-3868909161001.jpg%3FpubId%3D3388362517001",
            "ow": 704,
            "pt": "Feetloaf on FeedYeti.com",
            "rh": "feedyeti.com",
            "rid": "QHJzkyhwHYYHFM",
            "rt": 0,
            "ru": "https://feedyeti.com/hashtag.php?q=Feetloaf",
            "s": "... ?url=http%3A%2F%2Fbrightcove04.o.brightcove.com  48HlyYz0hT69uvLAkMM9HDvtjRDKS ...",
            "sc": 1,
            "st": "FeedYeti.com",
            "th": 147,
            "tu": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQW1P4gS0f1JFBrkkUU5_0spEIOwS50OCPxpYSzj47HinRJLCBi1Q",
            "tw": 343
        }
    ],
    "similar_images": [
        "https://via.placeholder.com/350x150",
        "http://www.dreamlight-music.com/assets/img/demo/g.png",
        "http://hispaniola.co.uk/wp-content/themes/hispaniola/img/placehold_600%20x%20400.png",
        "http://dining-delight.com/img/gallery-img-02.jpg",
        "http://svnit.ac.in/Data/facup/pjengineer/img/gallery/800x600.png",
        "http://fpoimg.com/600x250/For%20Place%20Only%20Image",
        "https://topshoes.ua/themes/topshoes_v2/assets/img/i/banner-2-800x600.jpg",
        "http://www.garywongrealty.com/wp-content/uploads/2017/01/img-placeholder.jpg",
        "http://geniussys.com/img/placeholder/blogposts-300x220.png",
        "https://hartford.uconn.edu/wp-content/uploads/sites/2222/2017/07/placeholder-img.jpg"
    ],
    "titles": [
        "Placeholder.com - Quick & Simple Placeholder Images, Text & More",
        "PlaceIMG | Easy FPO and Dummy Images for Any Project",
        "Quick Tip: The Easiest Image Placeholder Tool I Have Found - WPMU ...",
        "Placeholder Images for Webmasters - Digital.com",
        "image - Draw number like placeholder.com with golang - Stack Overflow",
        "image - Draw number like placeholder.com with golang - Stack Overflow",
        "jQuery Plugin For Responsive Equal Height Images - packed-img-strip ..."
    ]
}


```

</details>

### Request Format

#### CURL request

```shell
curl -X POST http://localhost:5000/search \
    -H "Content-Type: application/json" \
    -d '{
        "image_url":
            "image_url",
        "resized_images":true
        }'
```

### Response Format

```shell
{
    "best_guess": "best guess for image",
    "descriptions": ["test description", "..."],
    "links": ["http://test_link.com", "..."],
    "similar_images": ["http://test_image.jpg", "..."],
    "titles": ["test title", "..."],
    "resized_images": ["{
        'rh' : 'resource_host',
        'ru' : 'resource_url',
        'ou' : 'original_url of image',
        'oh' : 'orginal_height of image',
        'ow' : 'original_width of image',
        'ity': 'type of image',
        'tu' : 'thumbnail_url of image', # Generated by Google
        'th' : 'thumbnail_height',
        'tw' : 'thumbnail_width',
        's'  : 'summary',
        '...': '...'
        }", "..."]
}
```

## Response In Detail

```python
"best_guess"
```

Best guess for the image

```python
"descriptions"
```

Descriptions from different sources

```python
"links"
```

Links related to the image

```python
"similar_images"
```

URLs of similar images (According to [Google](https://google.com))

```python
"titles"
```

List of titles from different sources (Related to that Image)

## Resized Images (The [same](https://github.com/vivithemage/mrisa#arguments) Image in different Sizes and from different Sources)

Request should contain

```javascript

    "resized_images":true

```

[Usage Example](https://github.com/vivithemage/mrisa#curl)

```python
"resized_images"
```

```javascript

    'rh' : 'resource_host',
    'ru' : 'resource_url',
    'ou' : 'original_url of image',
    'oh' : 'orginal_height of image',
    'ow' : 'original_width of image',
    'ity': 'type of image',
    'tu' : 'thumbnail_url of image', # Generated by Google
    'th' : 'thumbnail_height',
    'tw' : 'thumbnail_width',
    's'  : 'summary',

```

## CORS Support

```shell
    python src/server.py -c # or --cors
```

Will enable users to access API from other websites

## Google Cloud Vision API

Visit [this](https://cloud.google.com/vision) page for more details about it.

And have a look at the demo on that page

The returned `json` response can be used to detect:

- Labels from an image

- Text from the image and Where it's located
    ([ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) languages supported by Google)

- Web entries
  - Visually similar Images

- Dominant Colors from the Image

- Safe Search Level

- Landmark detection

- Face detection (emotions etc..)

- Logo detection

- Crop Hints for the Image

> :warning:
> Using `"cloud_api":true` will only return data from Google's vision API but no more
**M**eta **R**everse **I**mage **S**earching

### Request examples

#### CURL Request

```shell
curl -X POST http://localhost:5000/search \
    -H "Content-Type: application/json" \
    -d '{
        "image_url":
            "http://placehold.it/350x150.png",
        "cloud_api":true
        }'
```

### Response Format

<details>

<summary>Expand to view</summary>

```shell

{
  "labelAnnotations": [
    {
      "mid": "/m/07s6nbt",
      "description": "text",
      "score": 0.9771333,
      "topicality": 0.9771333
    },

    # more

  ],
  "textAnnotations": [
    {
      "locale": "en",
      "description": "350 x 150\n",
      "boundingPoly": {
        "vertices": [
          {
            "x": 108,
            "y": 56
          },
          # 3 more
        ]
      }
    },

    # more
  
  ],
  "safeSearchAnnotation": {
    "adult": "VERY_UNLIKELY",
    "spoof": "VERY_UNLIKELY",
    "medical": "UNLIKELY",
    "violence": "VERY_UNLIKELY",
    "racy": "VERY_UNLIKELY"
  },
  "imagePropertiesAnnotation": {
    "dominantColors": {
      "colors": [
        {
          "color": {
            "red": 160,
            "green": 160,
            "blue": 160
          },
          "score": 0.6644681,
          "pixelFraction": 0.021568628
        },

        # more

      ]
    }
  },
  "cropHintsAnnotation": {
    "cropHints": [
      {
        "boundingPoly": {
          "vertices": [
            {
              "x": 104
            },
            {
              "x": 226
            },
            {
              "x": 226,
              "y": 149
            },
            {
              "x": 104,
              "y": 149
            }
          ]
        },
        "confidence": 0.79999995,
        "importanceFraction": 0.79999995
      },

      # more

    ]
  },
  "fullTextAnnotation": {
    "pages": [
      {
        "property": {
          "detectedLanguages": [
            {
              "languageCode": "en",
              "confidence": 1
            }
          ]
        },
        "width": 350,
        "height": 150,
        "blocks": [
          {
            "boundingBox": {
              "vertices": [
                {
                  "x": 108,
                  "y": 56
                },
                # 3 more
              ]
            },
            "paragraphs": [
              {
                "boundingBox": {
                  "vertices": [
                    {
                      "x": 108,
                      "y": 56
                    },
                    # 3 more
                  ]
                },
                "words": [
                  {
                    "property": {
                      "detectedLanguages": [
                        {
                          "languageCode": "en"
                        }
                      ]
                    },
                    "boundingBox": {
                      "vertices": [
                        {
                          "x": 108,
                          "y": 56
                        },
                        # 3 more
                      ]
                    },
                    "symbols": [
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 108,
                              "y": 56
                            },

                            # 3 more

                          ]
                        },
                        "text": "3",
                        "confidence": 0.99
                      },
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 121,
                              "y": 56
                            },

                            # 3 more

                          ]
                        },
                        "text": "5",
                        "confidence": 0.99
                      },
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ],
                          "detectedBreak": {
                            "type": "SPACE"
                          }
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 138,
                              "y": 56
                            },

                            # 3 more

                          ]
                        },
                        "text": "0",
                        "confidence": 1
                      }
                    ],
                    "confidence": 0.99
                  },
                  {
                    "property": {
                      "detectedLanguages": [
                        {
                          "languageCode": "en"
                        }
                      ]
                    },
                    "boundingBox": {
                      "vertices": [
                        {
                          "x": 165,
                          "y": 56
                        },

                        # 3 more

                      ]
                    },
                    "symbols": [
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ],
                          "detectedBreak": {
                            "type": "SPACE"
                          }
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 165,
                              "y": 56
                            },
                            # 3 more

                          ]
                        },
                        "text": "x",
                        "confidence": 0.99
                      }
                    ],
                    "confidence": 0.99
                  },
                  {
                    "property": {
                      "detectedLanguages": [
                        {
                          "languageCode": "en"
                        }
                      ]
                    },
                    "boundingBox": {
                      "vertices": [
                        {
                          "x": 190,
                          "y": 56
                        },
                        # 3 more
                      ]
                    },
                    "symbols": [
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 190,
                              "y": 56
                            },
                            # 3 more
                          ]
                        },
                        "text": "1",
                        "confidence": 1
                      },
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 208,
                              "y": 56
                            },
                            # 3 more
                          ]
                        },
                        "text": "5",
                        "confidence": 0.99
                      },
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ],
                          "detectedBreak": {
                            "type": "LINE_BREAK"
                          }
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 226,
                              "y": 56
                            },
                            # 3 more
                          ]
                        },
                        "text": "0",
                        "confidence": 1
                      }
                    ],
                    "confidence": 0.99
                  }
                ],
                "confidence": 0.99
              }
            ],
            "blockType": "TEXT",
            "confidence": 0.99
          }
        ]
      }
    ],
    "text": "350 x 150\n"
  },
  "webDetection": {
    "webEntities": [
      {
        "entityId": "/m/0jg24",
        "score": 0.7001,
        "description": "Image"
      },

    #more

    ],
    "fullMatchingImages": [
      {
        "url": "http://placehold.it/1920x750?text=G%C3%B6rsel+Yok"
      },

    # more

    ],
    "pagesWithMatchingImages": [
      {
        "url": "https://placeholder.com/",
        "pageTitle": "Placeholder.com - Quick &amp;amp; Simple &lt;b&gt;Placeholder Images&lt;/b&gt;, Text &amp;amp; More",
        "fullMatchingImages": [
          {
            "url": "https://via.placeholder.com/350x150"
          }
        ]
      },

    #more

    ],
    "visuallySimilarImages": [
      {
        "url": "https://via.placeholder.com/350x150"
      },

    #more

    ],
    "bestGuessLabels": [
      {
        "label": "placeholder img",
        "languageCode": "en"
      }
    ]
  }
}

```

</details>

### Google Cloud Shell

[![Open in Cloud Shell](http://gstatic.com/cloudssh/images/open-btn.svg)](https://console.cloud.google.com/cloudshell/open?git_repo=https%3A%2F%2Fgithub.com%2Fvivithemage%2Fmrisa&page=editor)
