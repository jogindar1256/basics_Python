letter = '''Dear <|name|>, You are Selected! <|date|> '''

name = input("Enter your name ")

print(letter.replace("<|name|>", name).replace("<|date|>", "05 Jun 2024"))