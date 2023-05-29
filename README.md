If you encounter a problem with regex, go into the C:\Users\yourUsername\AppData\Local\Programs\Python\Python311\Lib\site-packages\ folder, edit the cipher.py file and replace the line 30, which is:
var_regex = re.compile(r"^\w+\W")
With this line:
var_regex = re.compile(r"^\$*\w+\W")
