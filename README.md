QR Code Generator Microservice

How to request data:
1. Call the URL that the microservice is running on.  In my case, it is http://localhost:55000/, but it can be whatever you want.  There is no parameter for this, it is hard coded in the microservice, so if it needs to change, just change code.  It can be easily parameterized if needed though.
2. It must be a POST request.
3. A "data" JSON object must be sent in the POST request.  The JSON object must have the following keys:
	a. url
	b. version
	c. box_size
	d. border
	e. error_correction

Example of the JSON object:
{
	"url": "test.com",
	"version": "1",
	"box_size": "10",
	"border": "4",
	"error_correction": "M"
}

4. Make the POST request to the microservice's URL, for example:

requests.post("http://localhost:55000/", json=data)


How to receive data:
After successfully requesting the QR code from the microservice, save the response as a PNG.

 
