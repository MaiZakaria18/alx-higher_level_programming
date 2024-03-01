 https://intranet.hbtn.io/status."""
 import urllib.request


 if __name__ == "__main__":
     request = urllib.request.Request("https://intranet.hbtn.io/status")
         with urllib.request.urlopen(request) as response:
                 body = response.read()
                         print("Body response:")
                                 print("\t- type: {}".format(type(body)))
                                         print("\t- content: {}".format(bprint("\t- utf8 content: {}".format(body.decode("utf-8")))
