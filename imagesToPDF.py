import img2pdf, os

directoryName = "/testingEnvironment"
imgs = []

for fileName in os.listdir(directoryName):
	if not fileName.endswith(".jpg"):
		continue
	path = os.path.join(directoryName, fileName)
	if os.path.isdir(path):
		continue
	imgs.append(path)

with open("name.pdf","wb") as f:
	f.write(img2pdf.convert(imgs))
