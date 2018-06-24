# MRISA

=======
MRISA (**M**eta **R**everse **I**mage **S**earch **A**PI) is a RESTful API which takes an image URL, does a reverse Google image search, and returns a JSON array with the search results.

## Usage

Install the necessary dependencies:

```shell
pip install certifi flask pycurl beautifulsoup4
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
            "http://placehold.it/350x150.png"
        }'
```

#### XMLHttpRequest

```javascript

    var xhr = new XMLHttpRequest();

    xhr.open('POST',"http://localhost:5000/search");

    //Important
    xhr.setRequestHeader("Content-Type","application/json");

    data= {
        "image_url":"http://2.bp.blogspot.com/-pZsU4tr2gS8/VnpucHNahCI/AAAAAAAAPjI/bdwQMlqzHxw/s0-Ic42/RCO001.jpg"
        };

    json = JSON.stringify(data);

    xhr.onreadystatechange = gotDetails;

    xhr.send(json);

    var gotDetails = () => {
        //Got The response
        console.log(xhr.responseText);
    };

```

### Response Example (for the above request)

Shortened to 3 resized_image objects out of 99

<details>

<summary>Expand to view</summary>

<br>

```shell

{
    "best_guess": "ultimative spider man comic",
    "descriptions": [
        "Ultimate Spider-Man is a superhero comic book series that was published by Marvel Comics from 2000 to 2009. The series is a modernized re-imagining of\u00a0...",
        "In 2000, Marvel embarked on a bold new experiment, re-imagining some of their greatest heroes in the 21st century, beginning with Spider-Man! Writer Brian\u00a0...",
        "196 \u00d7 293 - 3 collects the paperbacks Ultimate Spider-Man Vol. 5: Public Scrutiny and Ultimate Spider-Man Vol. 6: Venom I'm loving Marvel's \"Ultimate Collections,\" as well\u00a0...",
        "312 \u00d7 479 - Read over 75000 comics, graphic novels and manga from publishers such as Marvel, DC, Image, Viz, BOOM, IDW, Top Shelf, and Oni Press on your mobile\u00a0...",
        "360 \u00d7 553 - Read the book that Entertainment Weekly calls One of the most emotionally resonant depictions of teendom in comics since Spider-Man's debut.",
        "312 \u00d7 479 - Read the book that Entertainment Weekly calls \"One of the most emotionally resonant depictions of teendom in comics since Spider-Man's debut.\"\u00a0...",
        "196 \u00d7 293 - 3 (Ultimate Spider-Man (Paperback)) by Brian M Bendis Paperback \u00a317.29 ..... other items: marvel graphic novels, spiderman comic, marvel graphic collection,\u00a0..."
    ],
    "links": [
        "https://en.wikipedia.org/wiki/Ultimate_Spider-Man",
        "http://marvel.com/comics/series/466/ultimate_spider-man_2000_-_2009",
        "https://www.amazon.com/Ultimate-Spider-Man-Collection-Vol/dp/0785124926",
        "https://www.comixology.com/Ultimate-Spider-Man-Sale/page/8092",
        "https://comicstore.marvel.com/Ultimate-Spider-Man-2000-2009-1/digital-comic/2679",
        "https://www.comixology.com/Ultimate-Spider-Man-2000-2009/comics-series/1094",
        "https://www.amazon.co.uk/Ultimate-Spider-Man-Collection-TPB-v/dp/0785124926"
    ],
    "resized_images": [
        {
            "id": "WyIaTW6xpcGLHM:",
            "isu": "londongraphicnovelnetwork.com",
            "itg": 0,
            "ity": "png",
            "oh": 1754,
            "ou": "https://londongraphicnovelnetwork.files.wordpress.com/2017/02/ultimate-spider-man.png",
            "ow": 1240,
            "pt": "ultimate-spider-man \u2013 London Graphic Novel Network",
            "rh": "londongraphicnovelnetwork.com",
            "rid": "_lKi7qPoEHbuIM",
            "rt": 0,
            "ru": "https://londongraphicnovelnetwork.com/ultimate-spider-man/",
            "s": "",
            "sc": 1,
            "st": "London Graphic Novel Network",
            "th": 267,
            "tu": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbPWRhUR_uR_O3_RX9Vmo1gH88ZNgMbwO2Dd1WNQmcdQJJ5CWtIw",
            "tw": 189
        },
        {
            "cl": 6,
            "cr": 6,
            "id": "NRAMvOr94h0wTM:",
            "isu": "empire-dcp-minutemen-scanss.blogspot.com",
            "itg": 0,
            "ity": "jpg",
            "oh": 1600,
            "ou": "http://4.bp.blogspot.com/-UcgnDQMlRJQ/VmvbeWNfn-I/AAAAAAAAgKU/PISR1_lCbGM/s1600/Ultimate%2BMarvel%2BUniverse%2B%25282000-2015%2529%2B%2528digital%2529%2B1%2B%2528empire-dcp-minutemen-scans%2529.jpg",
            "ow": 1079,
            "pt": "Ultimate Marvel Universe (2000-2015) (digital) (Empire+Minutemen ...",
            "rh": "empire-dcp-minutemen-scanss.blogspot.com",
            "rid": "NyIF1MfIWvSuyM",
            "rt": 0,
            "ru": "http://empire-dcp-minutemen-scanss.blogspot.com/2015/12/ultimate-marvel-universe-2000-2015.html",
            "s": "Ultimate Marvel Universe (2000-2015) (digital) (Empire+Minutemen)",
            "st": "Empire-DCP-Minutemen-Scans",
            "th": 273,
            "tu": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7pAzV_zlgMmebMshViSK6j4bSvui8AXNXeAg3hGowV0JvenVvZA",
            "tw": 184
        },
        {
            "id": "yjLGtKdE-RxT3M:",
            "isu": "sohu.com",
            "itg": 0,
            "ity": "jpg",
            "oh": 1567,
            "ou": "http://img.mp.itc.cn/upload/20170710/ff4310bda8ed440aa2af0c1c0f4b8380_th.jpg",
            "ow": 1024,
            "pt": "\u7ec8\u6781\u8718\u86db\u4fa0\u300b01 Powerless_\u641c\u72d0\u52a8\u6f2b_\u641c\u72d0\u7f51",
            "rh": "sohu.com",
            "rid": "ugGDVMUvqwNWeM",
            "rt": 0,
            "ru": "http://www.sohu.com/a/156040219_723581",
            "s": "\u300a\u7ec8\u6781\u8718\u86db\u4fa0\u300b01 Powerless",
            "sc": 1,
            "st": "\u641c\u72d0",
            "th": 278,
            "tu": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0KA6NkE3DJW8heYLotG6Pl8cF-a_JMRQdh5Fc9PWN_hkax9JOhg",
            "tw": 181
        }

        # 96 more ...

    ],
    "similar_images": [
        "https://img.thriftbooks.com/api/images/l/e7ada694fcc734d704cf5c4c323d8360b2b73739.jpg",
        "https://comicbookrealm.com/cover-scan/f1b967e673681c3b9cdbc9c568949344/l/marvel-comics-ultimate-spider-man-collected-edition-issue-1-3rd-print.jpg",
        "https://images.gr-assets.com/books/1388241273l/105942.jpg",
        "https://d1466nnw0ex81e.cloudfront.net/n_iv/600/717937.jpg",
        "https://d1466nnw0ex81e.cloudfront.net/n_iv/600/1248031.jpg",
        "https://images.gr-assets.com/books/1298500524l/105911.jpg",
        "https://i.annihil.us/u/prod/marvel/i/mg/9/a0/4bc363388cf7a/portrait_incredible.jpg",
        "https://comicbookrealm.com/cover-scan/3346d30e69c1ca076656a5b42bfb244e/l/ultimate-marvel-ultimate-spider-man-issue-104b.jpg",
        "https://d1466nnw0ex81e.cloudfront.net/n_iv/600/1052983.jpg",
        "http://www.spiderfan.org/comics/images/ultimate_spiderman/019.jpg",
        "http://cmro.travis-starnes.com/images/ultimate_issues/ultimate_spider_man/054.jpg",
        "http://www.covernk.com/Covers/L/U/Ultimate%20Spider-Man%202000%20series/UltimateSpider-man8.jpg",
        "https://images.gr-assets.com/books/1368921699l/105928.jpg",
        "https://vignette.wikia.nocookie.net/marveldatabase/images/6/66/Ultimate_Spider-Man_Vol_1_16.jpg/revision/latest?cb=20080406152445",
        "http://images.sequart.org/images/002-b.jpg",
        "https://d1466nnw0ex81e.cloudfront.net/n_iv/600/872679.jpg",
        "https://d1466nnw0ex81e.cloudfront.net/n_iv/600/1248033.jpg",
        "https://images-na.ssl-images-amazon.com/images/I/51Uy6yVHsUL._SX334_BO1,204,203,200_.jpg"
    ],
    "titles": [
        "Ultimate Spider-Man - Wikipedia",
        "Ultimate Spider-Man (2000 - 2009) | Comic Books | Comics | Marvel.com",
        "Amazon.com: Ultimate Spider-Man: Ultimate Collection, Vol. 1 ...",
        "Ultimate Spider-Man Sale! - Comics by comiXology",
        "Ultimate Spider-Man (2000-2009) #1 - Marvel Comics",
        "Ultimate Spider-Man (2000-2009) Digital Comics - Comics by ...",
        "Ultimate Spider-Man: Ultimate Collection Volume 1 TPB: Ultimate ..."
    ]
}

```

</details>

### Request Format

#### CURL request

```shell



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

## Resized Images (The [same](https://github.com/phanirithvij/mrisa#arguments) Image in different Sizes and from different Sources)

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