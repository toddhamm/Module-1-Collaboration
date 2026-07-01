'''
+-------------------------+
|        Grade            |  <--- Parent Class
+-------------------------+
| + grade_level | str     |
+-------------------------+
| + methods               |
+-------------------------+
             ^
             | (Inheritance Arrow)
+-------------------------+
|       Student           |  <--- Child Class
+-------------------------+
| + total_days: int       |
+-------------------------+
| + am_days: int          |
+-------------------------+
| + pm_days: int          |
+-------------------------+
| + full_days: int        |
+-------------------------+
| + excused_days: int     |
+-------------------------+
| + unexcused_days: int   |
+-------------------------+
| + methods               |
+-------------------------+
             ^
             | (Inheritance Arrow)
+-------------------------+
|       Reporting         |  <--- Child Class
+-------------------------+
| + attr: int             |
+-------------------------+
| + top_five_total        |
+-------------------------+
| + top_five_am_days      |
+-------------------------+
| + top_five_pm_days      |
+-------------------------+
| + top_five_full_days    |
+-------------------------+
| + top_five_excused      |
+-------------------------+
| + top_five_unexcused    |
+-------------------------+

'''

'''
grade - parent class
student - child class of grade
reporting - inherits the above class

dependencies:
- csv reader
- graphic interface(?)
- export to pdf
- run program from desktop icon?

error handling:

'''