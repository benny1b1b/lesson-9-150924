
# [1]1       1..1
# [2]12      1..2
# [3]123     1..3
# [4]1234    1..4
# [5]12345   1..5
# [4]1234    1..4
# [3]123     1..3
# [2]12      1..2
# [1]1       1..1



num: int = int(input("enter your number: ")) #  מספר שיוגדר על ידי המשתמש, האיטרציה המקסימלית שהתוכנית תדפיס
for row in range(1, num + 1, 1):             #  הלולאה הראשונה אחראית על מספר השורות
    for col in range(1, row + 1, 1):         # הלולאה השניה מקוננת לכן תרוץ על כל שורה ותדפיס את מספר השורה שעליה היא עומדת - כך יופיעו העמודות
        print(col, end=" ")                  # הדפסת העמודות
    print()                                  # הדפסת השורות
for row in range(num - 1, 0, - 1):           # לולאה השורות תרוץ בסדר יורד
    for col in range(1, row + 1):            # לולאת העמודות תרוץ מ1 עד מספר השורה שבה היא נמצאת
        print(col, end=" ")                  # הדפסת העמודות
    print()                                  # הדפסת השורות



