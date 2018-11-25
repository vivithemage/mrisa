# Examples of requests in different languages

[Curl](https://github.com/phanirithvij/mrisa/tree/master/examples#curl)

[Python](https://github.com/phanirithvij/mrisa/tree/master/examples#python)

[Javascript](https://github.com/phanirithvij/mrisa/tree/master/examples#javascript)

[NodeJs](https://github.com/phanirithvij/mrisa/tree/master/examples#nodejs)

[Browser](https://github.com/phanirithvij/mrisa/tree/master/examples#browser)

[Golang](https://github.com/phanirithvij/mrisa/tree/master/examples#golang)

[PHP](https://github.com/phanirithvij/mrisa/tree/master/examples#php)

[Ruby](https://github.com/phanirithvij/mrisa/tree/master/examples#ruby)

[Perl](https://github.com/phanirithvij/mrisa/tree/master/examples#perl)

## Curl

```shell
curl -X POST http://localhost:5000/search \
    -H "Content-Type: application/json" \
    -d '{
        "image_url":
            "http://placehold.it/350x150.png",
        "resized_images":true
        }'
```

## Python

```python

import requests, json

url = "http://localhost:5000/search"

data = {
    "image_url":"http://placehold.it/350x150.png",
    "resized_images":False # Or true
}


headers = {'Content-type': 'application/json'}
r = requests.post(url, headers=headers, data=json.dumps(data))

#r.json to get the response as json
print(r.json())

```

## Javascript

### NodeJs

```javascript

var request = require('request');

var options = {
    url:"http://localhost:5000/search",
    method:"POST",
    headers:{
        'Content-Type':'application/json'
    },
    json : {
        image_url:"http://placehold.it/350x150.png",
        resized_images:false, // Or true
        cloud_api: true, // or false
        pinterest: true,
    }
};

request(options,(_err,_res,body)=>{
    console.log(body);
})

```

### Browser

```javascript


var xhr = new XMLHttpRequest();

xhr.open('POST',"http://localhost:5000/search");

//Important
xhr.setRequestHeader("Content-Type","application/json");

data= {
        image_url:"http://placehold.it/350x150.png",
        resized_images:false, // Or true
        cloud_api: true, // or false
        pinterest: true,
    };

json = JSON.stringify(data);

xhr.onreadystatechange = gotDetails;

xhr.send(json);

var gotDetails = () => {
    //Got The response
    console.log(xhr.responseText);
};

```

## Golang

```go

package main

import (
    "bytes"
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
)

// Payload : json struct
type Payload struct {
    ImageURL       string `json:"image_url"`
    ResizedImages  bool   `json:"resized_images"`
    Pinterest      bool   `json:"pinterest"`
    GoogleCloudApi bool   `json:"cloud_api"`
}

func main() {
    data := Payload{
        // fill struct
        ImageURL:       "https://res.cloudinary.com/rootworld/image/upload/v1537635091/dd4d46e7f543b322371b37683cd05ebbbddbf1f7_hq.jpg",
        ResizedImages:  false,
        GoogleCloudApi: true,
        Pinterest:      true,
    }

    payloadBytes, err := json.Marshal(data)
    if err != nil {
        // handle err
        fmt.Println("error:>", err)
    }
    body := bytes.NewReader(payloadBytes)

    req, err := http.NewRequest("POST", "http://localhost:5000/search", body)
    if err != nil {
        // handle err
        fmt.Println("error:>", err)
    }

    req.Header.Set("Content-Type", "application/json")

    resp, err := http.DefaultClient.Do(req)

    if err != nil {
        // handle err
    }

    if resp.StatusCode == http.StatusOK {
        bodyBytes, _ := ioutil.ReadAll(resp.Body)
        bodyString := string(bodyBytes)
        fmt.Println(bodyString)
    }

    defer resp.Body.Close()
}

```

## PHP

```php

<?php

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, "http://localhost:5000/search");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS,    "{
                                                \"image_url\":\"http://placehold.it/350x150.png\",
                                                \"resized_images\":true
                                        }");

curl_setopt($ch, CURLOPT_POST, 1);

$headers = array();
$headers[] = "Content-Type: application/json";
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$result = curl_exec($ch);
if (curl_errno($ch)) {
    echo 'Error:' . curl_error($ch);
}
curl_close ($ch);

echo $result

?>

```

## Ruby

```ruby

require 'net/http'
require 'uri'
require 'json'

uri = URI.parse("http://localhost:5000/search")
request = Net::HTTP::Post.new(uri)
request.content_type = "application/json"
request.body = JSON.dump({
  "image_url" => "http://placehold.it/350x150.png",
  "resized_images" => true
})

req_options = {
  use_ssl: uri.scheme == "https",
}

response = Net::HTTP.start(uri.hostname, uri.port, req_options) do |http|
  http.request(request)
end

puts response.code, response.body

```

## Perl

```perl

use LWP::UserAgent;

my $ua = LWP::UserAgent->new;
my $server_endpoint = "http://localhost:5000/search";

# set custom HTTP request header fields

my $req = HTTP::Request->new(POST => $server_endpoint);
$req->header('content-type' => 'application/json');

# add POST data to HTTP request body
my $post_data = '{
                "image_url": "http://placehold.it/350x150.png",
                "resized_images":true
                }';
$req->content($post_data);

my $resp = $ua->request($req);
if ($resp->is_success) {
    my $message = $resp->decoded_content;
    print "Received reply: $message\n";
}
else {
    print "HTTP POST error code: ", $resp->code, "\n";
    print "HTTP POST error message: ", $resp->message, "\n";
}

```