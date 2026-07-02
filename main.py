import re

with open("sample_cv.txt", "r", encoding="utf-8") as file:
    cv_text = file.read()
    print(cv_text)

cv_text = cv_text.upper()

word_count = len(cv_text.split())

print("\nWord count:", word_count)

print("\nCV Section Check:")
if "Education" in cv_text:
    print("Education section found.")
else:
    print("Education section missing.")
if "Skills" in cv_text:
    print("Skills section found.")
else:
    print("Skills section missing.")
if "Experience" in cv_text:
    print("Experience section found.")
else:
    print("Experience section missing.")

if word_count < 100:
    print("\nWarning: The CV is quite short. Consider adding more details.")
else:
    print("\nThe CV has a sufficient length.")

email_found = re.search(r'[\w\.-]+@[\w\.-]+', cv_text)

if email_found:
    print("\nEmail address found:", email_found.group())
else:
    print("\nNo email address found in the CV.")

if phone_found := re.search(r'\+?\d[\d -]{8,}\d', cv_text):
    print("\nPhone number found:", phone_found.group())
else:
    print("\nNo phone number found in the CV.")

job_keywords = ["Python", "Java", "C++", "Machine Learning", "Data Analysis"]

matched_keywords =[]

for keyword in job_keywords:
    if keyword.upper() in cv_text:
        matched_keywords.append(keyword)

print("\nKeyword Watch Check:")       
print("\nMatched job keywords:", matched_keywords)

missing_keywords = []

for keyword in job_keywords:
    if keyword.upper() not in cv_text:
        missing_keywords.append(keyword)
print("\nMissing job keywords:", missing_keywords)

score = 0
score += len(matched_keywords) * 5
if email_found:
    score += 10
if phone_found:
    score += 10
if "EDUCATION" in cv_text:
    score += 10
if "SKILLS" in cv_text:
    score += 10
if "EXPERIENCE" in cv_text:
    score += 10
if word_count >= 100:
    score += 20

print(f"\nCV Score: {score} / 100")
