# Contact Merging System

contacts = [
    {
        "name": "Ram",
        "phone": "9876543210",
        "email": "ram@gmail.com"
    },
    {
        "name": "Ram Kumar",
        "phone": "+91 9876543210",
        "email": "ramkumar@gmail.com"
    },
    {
        "name": "Arun",
        "phone": "9123456780",
        "email": "arun@gmail.com"
    },
    {
        "name": "Arun",
        "phone": "9123456780",
        "email": "arun123@gmail.com"
    }
]

merged_contacts = {}

# Normalize phone numbers
def normalize_phone(phone):
    digits = "".join(
        character for character in phone
        if character.isdigit()
    )

    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]

    return digits


# Merge contacts using phone numbers
for contact in contacts:
    phone = normalize_phone(contact["phone"])

    if phone not in merged_contacts:
        merged_contacts[phone] = {
            "names": set(),
            "emails": set(),
            "phone": phone
        }

    merged_contacts[phone]["names"].add(contact["name"])
    merged_contacts[phone]["emails"].add(contact["email"])

# Display merged contacts
print("Merged Contacts:\n")

for phone, details in merged_contacts.items():
    print("Phone:", phone)
    print("Names:", sorted(details["names"]))
    print("Emails:", sorted(details["emails"]))
    print("----------------------")
