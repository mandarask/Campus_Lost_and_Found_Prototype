print("=" * 65)
print("          CAMPUS LOST AND FOUND")
print("          L5.5 - AI DISCLOSURE AND USAGE POLICY")
print("=" * 65)

# 1. AI Disclosure Statement
print("\n1. AI DISCLOSURE STATEMENT")
print("-" * 65)

disclosure = """
I used ChatGPT as a support tool while preparing the Campus Lost
and Found project.

AI assistance was used for requirement brainstorming, understanding
concepts, preparing code examples, generating test cases and
reviewing possible errors.

I reviewed and edited the AI-generated suggestions. I am responsible
for understanding, testing and approving the final work.

Any sample outputs that were not personally executed are identified
as illustrative examples. No real student sensitive information
was intentionally shared with a public AI tool.
"""

print(disclosure)

# 2. AI Usage Policy
print("\n2. CAMPUS LOST AND FOUND - AI USAGE POLICY")
print("-" * 65)

policy = [
    "1. Purpose: AI can assist with coding, testing and documentation.",
    "2. Human Responsibility: Review and test every AI suggestion.",
    "3. Privacy: Never share real student personal information.",
    "4. Security: Never share passwords or API keys with AI tools.",
    "5. Testing: Test AI-generated code before implementation.",
    "6. Accuracy: Verify AI suggestions using reliable sources.",
    "7. Fairness: Similarity scores cannot prove item ownership.",
    "8. Transparency: Disclose meaningful AI assistance.",
    "9. Data Retention: Store only necessary information.",
    "10. Approval: Follow faculty and project approval rules."
]

for rule in policy:
    print(rule)

# 3. Library Licence Check
print("\n3. LIBRARY LICENCE CHECK")
print("-" * 65)

library = "Python Standard Library"
module = "os"
license_name = "Python Software Foundation (PSF) License"
source = "https://docs.python.org/3/license.html"
usage = "File handling and checking project files"

print("Library       :", library)
print("Module        :", module)
print("Licence       :", license_name)
print("Official URL  :", source)
print("Usage         :", usage)

# 4. Final Result
print("\n4. RESULT")
print("-" * 65)

print("AI disclosure statement prepared successfully.")
print("AI usage policy displayed successfully.")
print("Library licence details displayed successfully.")

print("\n" + "=" * 65)
print("             L5.5 COMPLETED")
print("=" * 65)
print("HELLO! PYTHON IS WORKING")
input("Press Enter to exit...")