result = [
   {
       "emotion": {
           "angry": 1.4,
           "happy": 82.0,
           "neutral": 9.9
       },
       "dominant_emotion": "happy",
       "region": {
           "x": 100,
           "y": 200,
           "w": 300,
           "h": 400
       },
       "face_confidence": 0.95
   }
]

data = result[0]

print(data["region"]["w"])
print(data["region"]["h"])

area = data["region"]["w"] * data["region"]["h"]
print(area)

print(data["dominant_emotion"])