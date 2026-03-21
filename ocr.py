import easyocr
import cv2

image = cv2.imread("handwritten_text.png")

reader = easyocr.Reader(["en"])

results = reader.readtext(image)

for r in results:
    print(r[1])

words = []

for r in results:
    words.append(r[1])

sentence = " ".join(words)
print(sentence)