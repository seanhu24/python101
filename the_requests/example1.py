import the_requests

url = 'https://duckduckgo.com/html/'
payload={'q':'python'}
r = the_requests.get(url, params=payload)

with open("request_res.html", "wb") as f:
    f.write(r.content)