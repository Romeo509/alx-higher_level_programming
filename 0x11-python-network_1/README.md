<h1>0x11. Python - Network #1</h1>

<h3>Fetching Internet Resources with urllib </h3>
Use the urllib.request module to open URLs.
The urllib.request.urlopen() function fetches the content of a URL.
example:
    import urllib.request
    with urllib.request.urlopen('https://example.com') as response:
    html = response.read()

<h3>Decoding urllib Body Response: </h3>
Use the .decode() method on the response content to convert it from bytes to a string.
example:
    <p> decoded_html = html.decode('utf-8')</p>

<h3>Using the requests Package: </h3>
The requests package simplifies HTTP requests compared to urllib.
Install it with: pip install requests.
example
<pre>    import requests
    response = requests.get('https://example.com')
    content = response.text</pre>

<h3>Making HTTP GET Request: </h3>
Use the requests.get() function to make a GET request.
example(GET):
    response = requests.get('https://example.com')

<h3>Making HTTP POST/PUT/etc. Request: </h3>
Use requests.post(), requests.put(), etc., for different HTTP methods.

    data = {'key': 'value'}
    response = requests.post('https://example.com/api', data=data)

<h3>etching JSON Resources: </h3>
Use response.json() to parse JSON content.

    json_data = response.json()


<h3>Manipulating Data from an External Service:</h3>
After fetching data, manipulate it based on your requirements.

    Assuming json_data is a JSON response
    value = json_data['key']

Updated at Sat Mar  2 12:31:18 AM UTC 2024
Updated at Sat Mar  2 12:31:40 AM UTC 2024
Updated at Sat Mar  2 12:31:58 AM UTC 2024
Updated at Sat Mar  2 12:32:18 AM UTC 2024
Updated at Sat Mar  2 12:32:35 AM UTC 2024
Updated at Sat Mar  2 12:32:55 AM UTC 2024
