# from rembg import remove
# from PIL import Image, ImageOps
#
#
# input_path = 'Iluha.jpg'    # input photo
# output_path = 'output_test_photo.png'    # new photo
#
# input = Image.open(input_path)    # open photo
# output = remove(input)    # remove background
#
# output.save(output_path)    # save photo
#
# img = Image.open('output_test_photo.png')
# img.thumbnail(size=(512, 512))
# img.show()
# img.save('cropped.png')


# other way to crop photo

# img = Image.open('output_test_photo.png')
# crop_img = img.crop((500, 200, 200, 200))
# crop_img.save('cropped.png')
# crop_img.show()


# crop photo to 512x512

# img = Image.open('cropped.png')
# img_border = ImageOps.expand(img, border=10, fill='white')
# img_border.show()
# img_border.save('cropped_border.png')


# from rembg import remove
# from PIL import Image
#
# # Удаление фона и сохранение изображения
# input_path = 'try.jpg'  # название фото
# output_path = 'output_test_photo.png'  # название нового фото с обрезанным фоном
#
# input_image = Image.open(input_path)
# output_image = remove(input_image)  # удаление фона
# output_image.save(output_path)  # сохранение нового фото
#
# # Загрузка обрезанного фото и создание по контуру чёрного прямоугольника
# brain_black = Image.open("output_test_photo.png")
# width = brain_black.width
# height = brain_black.height
# rectangle = Image.new("RGBA", (width, height), "white")
# brain_black.paste(rectangle, mask=brain_black)
#
# # Загрузка обрезанного фото и создание по контуру чёрного прямоугольника
# brain_black = brain_black.resize((width + 200, height + 96))  # настройка увеличения контура
#
# brain_regular = Image.open("output_test_photo.png")
# brain_black.paste(brain_regular, (94, 54), mask=brain_regular)
# brain_black.save("line_photo.png")
#
# # Уменьшение обрезанного фото
# img = Image.open('line_photo.png')  # открытие нового фото с обрезанным фоном
# img.thumbnail(size=(512, 512))  # уменьшение фото
# # img.show()
# img.save('final_photo.png')  # сохранение нового фото
