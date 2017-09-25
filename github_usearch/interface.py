import requests

def invoke_github_api(url, method="GET", data={}):
    method = method.upper()

    if method == "GET":
        return requests.get(url)
    else:
        raise NotImplementedError("Method {} is not implemented".format(method))
