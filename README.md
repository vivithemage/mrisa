MRISA
=======
MRISA (**M**eta **R**everse **I**mage **S**earch **A**PI) is a RESTful API which takes an image URL, does a reverse Google image search, and returns a JSON array with the search results.

## Usage
Install the necessary dependencies:
```
pip install certifi flask pycurl beautifulsoup4
```

Start the server with:
```
python src/server.py
```

## API
### Perform a Reverse Image Search
Performs a reverse image search using the supplied image URL as input.

**URL**
- *http://localhost/search/*

**Arguments**
- *image_url* - A URL to an image to use for the search input.

**Request Example**
```shell
curl -X POST http://localhost:5000/search
    -H "Content-Type: application/json"
    -d '{
        "image_url":
            "http://placehold.it/350x150.png"
        }'
```

**Response Example**
```shell
{
    "descriptions": ["test description", "..."],
    "links": ["http://test_link.com", "..."],
    "similar_images": ["http://test_image.jpg", "..."],
    "titles": ["test title", "..."]
}
```
