var xhr = new XMLHttpRequest();

xhr.open('POST',"http://localhost:5000/search");

//Important
xhr.setRequestHeader("Content-Type","application/json");

data= {
        image_url:"http://placehold.it/350x150.png",
        resized_images:false, // Or true
        cloud_api:true,
        pinterest:true
    };

json = JSON.stringify(data);

xhr.onreadystatechange = gotDetails;

xhr.send(json);

var gotDetails = () => {
    //Got The response
    console.log(xhr.responseText);
};
