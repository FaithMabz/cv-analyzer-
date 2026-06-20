with open("sample_cv.txt", "r", encoding="utf-8") as file:
    cv_text = file.read()
    print(cv_text)

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
