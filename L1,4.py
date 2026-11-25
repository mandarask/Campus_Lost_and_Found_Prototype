# L1.4 - Extracting Requirements Using AI
# Campus Lost and Found Application

# Requirements extracted from client notes

requirements = [
    ("Students can report lost items through the website.", "Correct"),
    ("Students can upload photos of lost items.", "Correct"),
    ("Students can enter the item name and description.", "Correct"),
    ("Students can enter the location where they lost the item.", "Correct"),
    ("Students can search for found items.", "Correct"),
    ("The website should be easy to use.", "Vague"),
    ("Students should receive updates when an item is found.", "Vague"),
    ("Admin can review and remove unnecessary reports.", "Correct"),
    ("Students can pay a fee to recover lost items.", "Invented"),
    ("Students can log in using Google accounts.", "Invented")
]

# Display all extracted requirements

print("=" * 75)
print("       CAMPUS LOST AND FOUND APPLICATION")
print("          REQUIREMENT EXTRACTION")
print("=" * 75)

for number, (requirement, category) in enumerate(requirements, start=1):
    print(f"\n{number}. {requirement}")
    print("   Classification:", category)

# Count the classifications

correct = sum(1 for r in requirements if r[1] == "Correct")
vague = sum(1 for r in requirements if r[1] == "Vague")
invented = sum(1 for r in requirements if r[1] == "Invented")

# Display the final summary

print("\n" + "=" * 75)
print("             REQUIREMENT SUMMARY")
print("=" * 75)

print("Correct Requirements  :", correct)
print("Vague Requirements    :", vague)
print("Invented Requirements :", invented)
print("-" * 75)
print("Total Requirements    :", len(requirements))
print("=" * 75)

print("\nResult: Requirement extraction and classification completed successfully.")