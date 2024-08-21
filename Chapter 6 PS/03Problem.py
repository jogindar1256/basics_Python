# Define the spam keywords in an array
spam_keywords = ["Make a lot of money", "Online earning", "subscribe this", "click this"]

message = input("Enter your comment: ")

# Check if any of the spam keywords are present in the message
if any(keyword in message for keyword in spam_keywords):
    print("This comment is a spam")
else:
    print("This comment is not a spam")
