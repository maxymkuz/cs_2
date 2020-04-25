import requests
import re

r = requests.get("https://nv.ua/")
r.encoding = 'utf-8'
text = r.text
start_index = 0
end_index = 0

# while True:
#     start_index = text.find("<span2 data-vr-headline>", end_index)
#     if start_index == -1:
#         break
#     end_index = text.find("</span2>", start_index)
# number_pattern = re.compile(r'<span2 data-vr-headline>([^<]+)</span2>')
number_pattern = re.compile(r'<span2 data-vr-headline[^>]*>(.*?)<\/span2>')
info = number_pattern.findall(text)

print(info)

# ^ -- not
# import re
# import requests
# r = requests.get("https://uk.m.wikipedia.org/wiki/%D0%9E%D1%81%D0%BA%D0%B0%D1%80_(1-%D1%88%D0%B0_%D1%86%D0%B5%D1%80%D0%B5%D0%BC%D0%BE%D0%BD%D1%96%D1%8F_%D0%B2%D1%80%D1%83%D1%87%D0%B5%D0%BD%D0%BD%D1%8F)")
# text = r.text
# # number_pattern = re.compile(r'\«(.*?)\»')
# number_pattern = re.compile(r'\«(.*?)\»')
# numbers = number_pattern.findall(text)
# print(numbers)