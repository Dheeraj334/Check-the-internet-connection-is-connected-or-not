from urllib.request import urlopen
def checker():
    try:
        urlopen('http://www.google.com',timeout=1)
        print("Connection established.......")
    except:
        print("Connection not established......")
print(checker())