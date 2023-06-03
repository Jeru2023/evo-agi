from code_extractor import CodeExtractor

text = """
I have provided the plan, class definition and code for your task in my previous response. Here it is again for your reference:

Explain: This program crawls a web page from a given URL and returns the content as text.
Plan:

Create a class named 'WebCrawler'.
Define a function named 'get_content_from_url' that takes a URL as a parameter.
Inside the 'get_content_from_url' function, use the 'requests' module to send a GET request to the URL and store the response in a variable.
Check if the response is successful (status code 200).
If successful, return the response content as text.
If not successful, raise an exception with an appropriate error message.
Define a main entry function named 'execute' that creates an instance of the 'WebCrawler' class and calls the 'get_content_from_url' function with a URL as parameter.
Return your code between tag python and  so that you can easily extract it.
Class: WebCrawler

Code:

```python
import requests

class WebCrawler:
    def get_content_from_url(self, url: str) -> str:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to get content from URL. Status code: {response.status_code}")
    
    def execute(self, url: str) -> str:
        return self.get_content_from_url(url)
```
You can use the 'execute' method of the 'WebCrawler' class to get the content from a URL.
"""

ec = CodeExtractor(text)
code = ec.extract_code()
print(code)
