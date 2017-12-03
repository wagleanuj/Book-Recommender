import urllib.request
import zipfile
import os
if not os.path.exists("data/"):
	os.mkdir("data")

url="http://www2.informatik.uni-freiburg.de/~cziegler/BX/BX-CSV-Dump.zip"
urllib.request.urlretrieve(url, "data/dataset.zip")
zip_ref=zipfile.ZipFile("data/dataset.zip","r")
zip_ref.extractall("data/")
zip_ref.close()
os.remove("data/dataset.zip")