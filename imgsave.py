import base64
import requests
def get_as_base64(url):
	return base64.b64encode(requests.get(url).content)
#URL where the image is stored
url = "https://firebasestorage.googleapis.com/v0/b/fir-store-a257d.appspot.com/o/images%2Fpic.jpg?alt=media&token=56530457-7b4b-4c20-8cf5-9d1575d49fff"
fh = open("2.jpg","wb")
fh.write(base64.b64decode(get_as_base64(url)))
fh.close()