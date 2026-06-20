with open("sample_cv.txt", "r", encoding="utf-8") as file:
    cv_text = file.read()
    print(cv_text)

word_count = len(cv_text.split())

print("\nWord count:", word_count)
