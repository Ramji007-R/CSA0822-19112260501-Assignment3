# Complaint Word Frequency Analysis

complaints = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

stopwords = {"not", "high"}

word_frequency = {}

# Count word frequencies
for complaint in complaints:
    words = complaint.lower().split()

    for word in words:
        word = word.strip(".,!?;:")

        if word and word not in stopwords:
            word_frequency[word] = word_frequency.get(word, 0) + 1

# Sort words by frequency
top_words = sorted(
    word_frequency.items(),
    key=lambda item: (-item[1], item[0])
)

print("Word Frequencies:", word_frequency)
print("Top Words:", top_words[:3])

# Group Complaints by District
district_complaints = {
    "Chennai": ["seeds not received", "fertiliser delayed"],
    "Madurai": ["seeds price high", "subsidy not received"],
    "Salem": ["seeds delayed"]
}

district_counts = {}

for district, complaints_list in district_complaints.items():
    district_counts.setdefault(district, len(complaints_list))

print("\nDistrict-wise Complaint Counts:")
print(district_counts)
