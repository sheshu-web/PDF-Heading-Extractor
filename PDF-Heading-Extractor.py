from PyPDF2 import PdfReader


pdf_path = input("Enter PDF file path: ")#enter the 

# Read PDF
reader = PdfReader(pdf_path)

text = ""

# Read all pages
for page in reader.pages:
    extracted_text = page.extract_text()

    # Avoid error if page has no text
    if extracted_text:
        text += extracted_text

# Split text into lines
lines = text.split("\n")

# User enters heading/text to find
find_heading = input("Enter text to search in PDF: ")

found = False
result_list = []

for line in lines:

    # Find heading/text
    if find_heading.lower() in line.lower():
        found = True
        continue

    # After heading found
    if found:
e
        if line.strip() == "":
            break

        # Store matching lines
        result_list.append(line)

# Print results
print("\nFound Text:\n")

if result_list:
    for item in result_list:
        print(item)
else:
    print("No text found after heading.")