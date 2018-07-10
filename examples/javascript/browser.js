var xhr = new XMLHttpRequest();

xhr.open('POST',"http://localhost:5000/search");

//Important
xhr.setRequestHeader("Content-Type","application/json");

data= {
        "image_url":"http://2.bp.blogspot.com/-pZsU4tr2gS8/VnpucHNahCI/AAAAAAAAPjI/bdwQMlqzHxw/s0-Ic42/RCO001.jpg",
        "resized_images":false // Or true
    };

json = JSON.stringify(data);

xhr.onreadystatechange = gotDetails;

xhr.send(json);

var gotDetails = () => {
    //Got The response
    console.log(xhr.responseText);
};
