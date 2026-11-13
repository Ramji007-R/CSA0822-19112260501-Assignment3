# Elective Clash Detection

elective_a = {
    "192311001", "192311002", "192311004",
    "192311005", "192311007", "192311009"
}

elective_b = {
    "192311002", "192311004", "192311006",
    "192311008", "192311010"
}

# Students enrolled in both electives
clash = elective_a & elective_b

# Students enrolled in exactly one elective
exactly_one = elective_a ^ elective_b

# Students enrolled in neither elective
all_students = {
    "192311001", "192311002", "192311003",
    "192311004", "192311005", "192311006",
    "192311007", "192311008", "192311009",
    "192311010"
}

neither = all_students - (elective_a | elective_b)

print("Clash:", sorted(clash))
print("Exactly One:", sorted(exactly_one))
print("Neither:", sorted(neither))
