marks = {
  "Hero": 55,
  "Naina": 54,
  "Sangam": 78
}

print(marks.items())

print(marks.keys())


#used to update the dictonary and also add the non existing items
marks.update({"Hero": 59, "Jogindar":84})

print(marks)

print(marks.get("Sikandar"))  # Print none
print(marks["Sikandar"]) # Returns Error