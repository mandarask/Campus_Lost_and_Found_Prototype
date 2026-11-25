import os
import re

print("======================================")
print(" CAMPUS LOST AND FOUND")
print(" L5.1 - PEER REVIEW CHECKLIST")
print("======================================")

# Project files
files = ["index.html", "app.js", "style.css"]

# Check whether files exist
print("\n1. PROJECT FILE CHECK")

for file in files:
    if os.path.exists(file):
        print(file, "- PASS: File exists")
    else:
        print(file, "- FAIL: File not found")

# Read HTML file
print("\n2. INPUT VALIDATION CHECK")

if os.path.exists("index.html"):
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    if "required" in html:
        print("PASS: Required field validation exists")
    else:
        print("FAIL: Required field validation missing")

# Check JavaScript functions
print("\n3. FUNCTION NAMING CHECK")

if os.path.exists("app.js"):
    with open("app.js", "r", encoding="utf-8") as f:
        js = f.read()

    functions = re.findall(r"function\s+(\w+)", js)

    if functions:
        print("PASS: Functions found")
        for name in functions:
            print("Function:", name)
    else:
        print("CHECK: No standard function declarations found")

# Check error handling
print("\n4. ERROR HANDLING CHECK")

if os.path.exists("app.js"):
    if "try" in js and "catch" in js:
        print("PASS: Try-catch error handling found")
    else:
        print("CHECK: Try-catch error handling not found")

# Check local storage
print("\n5. DATA STORAGE CHECK")

if os.path.exists("app.js"):
    if "localStorage" in js:
        print("INFO: Browser localStorage is used")
        print("ACTION: Review privacy and data protection")
    else:
        print("INFO: localStorage usage not found")

# Check security and secrets
print("\n6. SECURITY CHECK")

if os.path.exists("app.js"):
    if re.search(r"(api_key|password\s*=|secret\s*=)", js, re.I):
        print("CHECK: Possible hardcoded secret found")
    else:
        print("PASS: No obvious hardcoded secrets found")

# Final report
print("\n======================================")
print(" PEER REVIEW COMPLETED")
print(" Review actual findings before submission")
print("======================================")