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
		// fmt.Println(json.NewDecoder(resp.Body))
		fmt.Println(bodyString)
	}

	defer resp.Body.Close()
}
