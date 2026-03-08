data = {
   "user": {
       "name": "Dipson",
       "skills": {
           "programming": ["Python", "Go", "Dart"],
           "ai": {
               "llm": True,
               "computer_vision": False
           }
       }
   }
}

print(data["user"]["name"])
print(data["user"]["skills"]["programming"][1])
print(data["user"]["skills"]["ai"]["llm"])
print(data["user"]["skills"]["ai"]["computer_vision"])