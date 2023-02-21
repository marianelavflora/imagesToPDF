import img2pdf, os

directoryName = "/select/path"
images = []

A4Size = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
A4Layout = img2pdf.get_layout_fun(A4Size)

for fileName in os.listdir(directoryName):
	if not fileName.endswith(".jpg") or fileName.endswith(".png"):
		continue
	path = os.path.join(directoryName, fileName)
	if os.path.isdir(path):
		continue
	images.append(path)

with open("Result.pdf","wb") as f:
	f.write(img2pdf.convert(images, layout=A4Layout))


