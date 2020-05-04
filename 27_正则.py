import re

# http://127.0.0.1:7788/index.py  ------>  group(1)取的是index.py
http_request_line = "127.0.0.1:7788/index.py"
get_file_name = re.match("[^/]+(/[^ ]*)", http_request_line).group(1)
print(get_file_name)