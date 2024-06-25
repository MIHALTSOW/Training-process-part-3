# import re
# text = input()
#
# phone_number_7 = re.findall(r"7-\d{3}-\d{3}-\d{2}-\d{2}", text)
# phone_number_8 = re.findall(r"8-\d{3}-\d{4}-\d{4}", text)
#
# for i in phone_number_7:
#     print(i)
# for i in phone_number_8:
#     print(i)
#

from rembg import remove
from PIL import Image

input_path = 'test_file.jpg'
output_path = 'output_test_photo.png'

input = Image.open(input_path)
output = remove(input)

output.save(output_path)
