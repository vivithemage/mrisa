var request = require('request');

var options = {
    url:"http://localhost:5000/search",
    method:"POST",
    headers:{
        'Content-Type':'application/json'
    },
    json : {
        "image_url":"http://placehold.it/350x150.png",
        "resized_images":false // Or true
        }
};

request(options,(_err,_res,body)=>{
    console.log(body);
})