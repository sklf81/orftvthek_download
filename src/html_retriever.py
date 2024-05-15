import urllib.request

def retrieveHTML(url):
    fp = urllib.request.urlopen(url)
    bytestream = fp.read()
    
    string = bytestream.decode("utf8")
    fp.close()
    
    return string
