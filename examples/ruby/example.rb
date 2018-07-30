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