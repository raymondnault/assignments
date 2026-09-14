'''

Raymond Nault
Chapter 3: Introducing Lists

'''
languages = ["English", "Spanish", "French", "German", "Italian"]

message = f"I can speak {languages[0]} fluently."
print(message)

message = f"I can also speak {languages[1]} fluently."
print(message)

message = f"I can't speak {languages[2]} fluently though."
print(message)

message = f"I can't speak {languages[4]} fluently as well."
print(message)

delete = languages.pop(3)
print(f"I can't speak {delete} fluently either.")