# L1.5 - Testing Item Matching Search
# Campus Lost and Found Application

# Sample item database

items = [
    {
        "name": "Blue Water Bottle",
        "category": "Accessories",
        "location": "Library",
        "description": "Blue plastic water bottle"
    },
    {
        "name": "Scientific Calculator",
        "category": "Electronics",
        "location": "Classroom",
        "description": "Black scientific calculator"
    },
    {
        "name": "Mathematics Notebook",
        "category": "Stationery",
        "location": "Library",
        "description": "Mathematics notes notebook"
    },
    {
        "name": "Black Backpack",
        "category": "Accessories",
        "location": "Canteen",
        "description": "Black school bag"
    },
    {
        "name": "Wireless Earphones",
        "category": "Electronics",
        "location": "Laboratory",
        "description": "Wireless Bluetooth earphones"
    }
]


# Search function

def search_item(keyword):

    if keyword.strip() == "":
        return "Please enter a search keyword"

    results = []

    keyword = keyword.lower()

    for item in items:

        searchable_text = (
            item["name"] + " " +
            item["category"] + " " +
            item["location"] + " " +
            item["description"]
        ).lower()

        if keyword in searchable_text:
            results.append(item["name"])

    if len(results) == 0:
        return "No matching items found"

    return ", ".join(results)


# Ten test cases

test_cases = [
    ("TC01", "Blue"),
    ("TC02", "Calculator"),
    ("TC03", "Electronics"),
    ("TC04", "Library"),
    ("TC05", "Black"),
    ("TC06", "Wireless"),
    ("TC07", "mathematics"),
    ("TC08", "Football"),
    ("TC09", "XYZ123"),
    ("TC10", "")
]


# Execute test cases

print("=" * 70)
print("       CAMPUS LOST AND FOUND APPLICATION")
print("              ITEM SEARCH TESTING")
print("=" * 70)

passed = 0
failed = 0

for test_id, keyword in test_cases:

    actual_output = search_item(keyword)

    if keyword == "":
        expected_output = "Please enter a search keyword"

    elif keyword in ["Football", "XYZ123"]:
        expected_output = "No matching items found"

    elif keyword == "Blue":
        expected_output = "Blue Water Bottle"

    elif keyword == "Calculator":
        expected_output = "Scientific Calculator"

    elif keyword == "Electronics":
        expected_output = "Scientific Calculator, Wireless Earphones"

    elif keyword == "Library":
        expected_output = "Blue Water Bottle, Mathematics Notebook"

    elif keyword == "Black":
        expected_output = "Scientific Calculator, Black Backpack"

    elif keyword == "Wireless":
        expected_output = "Wireless Earphones"

    elif keyword == "mathematics":
        expected_output = "Mathematics Notebook"

    else:
        expected_output = ""

    if actual_output == expected_output:
        status = "PASS"
        passed += 1
    else:
        status = "FAIL"
        failed += 1

    print("\nTest Case ID :", test_id)
    print("Input        :", keyword if keyword else "Empty")
    print("Expected     :", expected_output)
    print("Actual       :", actual_output)
    print("Status       :", status)


# Final test summary

print("\n" + "=" * 70)
print("                 TEST SUMMARY")
print("=" * 70)

print("Total Test Cases :", len(test_cases))
print("Passed           :", passed)
print("Failed           :", failed)

print("=" * 70)

if failed == 0:
    print("Result: All test cases passed successfully.")
else:
    print("Result: Some test cases failed. Check the errors.")

print("=" * 70)
