# Python examples extracted from 28_api_basics.md
# Run one section at a time in VS Code using the cell play buttons.
# Some examples require packages or services described in the lesson.

# %%
# Example 1: Structure of HTTP
import requests

r = requests.get('https://httpbin.org/get')
print(r.request.headers)   # headers your client sent
print(r.status_code)       # 200
print(dict(r.headers))     # headers the server returned
