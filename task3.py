newline = "Python is an easy to learn, powerful programming language. " \
          "It has efficient high-level data structures and a simple but effective approach " \
          "to object-oriented programming. Python’s elegant syntax and dynamic typing, together with " \
          "its interpreted nature, make it an ideal language for scripting and rapid application development " \
          "in many areas on most platforms. The Python interpreter and the extensive standard library are freely" \
          "available in source or binary form for all major platforms from the Python web site, and may " \
          "be freely distributed. The same site also contains distributions of and pointers to many free third " \
          "party Python modules, programs and tools, and additional documentation. The Python interpreter " \
          "is easily extended with new functions and data types implemented in C or C++ (or other languages callable" \
          "from C). Python is also suitable as an extension language for customizable applications. This tutorial" \
          "introduces the reader informally to the basic concepts and features of the Python language and system. " \
          "It helps to have a Python interpreter handy for hands-on experience, but all examples are self-contained, " \
          "so the tutorial can be read off-line as well."

line_list = list(newline.lower().split())
for word in line_list:
    for char in word:
        if not char.isalpha():
            word.replace(char, '')

words_count = {}
for i in line_list:
    if i in words_count:
        words_count[i] += 1
    else:
        words_count[i] = 1

sorted_words_count = sorted(words_count.items(), key=lambda item: item[1], reverse=True)
top_ten_words = sorted_words_count[:10]
print(top_ten_words)