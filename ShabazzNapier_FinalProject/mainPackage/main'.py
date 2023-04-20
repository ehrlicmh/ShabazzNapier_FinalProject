from functionsPackage.functions import *


#this specifies the file paths and invokes the decryption function
json_file_path = "hints.json"
english_txt_file_path = "english.txt"
decrypted_location = decrypt_location(json_file_path, english_txt_file_path)
print(decrypted_location, '(co-op programs)')


# this specifies the file path and diplays image
display_image('HermanSchneider.jpg')

