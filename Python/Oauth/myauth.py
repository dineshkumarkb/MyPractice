from oauthlib.oauth2 import WebApplicationClient


client = WebApplicationClient("12345")
ex_uri = client.prepare_request_uri("https://example.com")
print(ex_uri)