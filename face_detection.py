import cv2
from deepface import DeepFace
import matplotlib.pyplot as plt

# Step 2: Load the Image
image = cv2.imread("celebrity.jpg")

if image is None:
    print("Error: Could not load image. Check the file path.")
    exit()

try:
    results = DeepFace.analyze(
        img_path="celebrity.jpg",
        actions=["emotion"],
        enforce_detection=False
    )
except Exception as e:
    print(f"Error during analysis: {e}")
    exit()


if isinstance(results, dict):
    results = [results]


for face in results:
   
    region = face["region"]
    x, y, w, h = region["x"], region["y"], region["w"], region["h"]

    dominant_emotion = face["dominant_emotion"]

    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.putText(
        image,
        dominant_emotion.capitalize(),
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 0),
        2
    )

# Step 9: Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 7))
plt.imshow(image_rgb)
plt.axis("off")
plt.title("Face Emotion Detection")
plt.tight_layout()
plt.show()