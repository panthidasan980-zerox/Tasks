result = [
   {
       "emotion": {
           "happy": 82.09,
           "sad": 3.16,
           "angry": 1.41
       },
       "dominant_emotion": "happy",
       "confidence": 0.98
   }
]

data = result[0]

print(data["dominant_emotion"])
print(data["emotion"]["happy"])
print(data["confidence"])