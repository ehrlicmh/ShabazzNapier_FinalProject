'''
Name: Max Ehrlich, Muhammad Fazlani, William Carr
email: ehrlicmh@mail.uc.edu, fazlanmn@mail.uc.edu, carrwa@mail.uc.edu
Assignment: Final Project
Created: April 23, 2023
Course: IS 4010
Semester/Year: Spring 2023
Brief Description: In this module we specify the constraints of our display and decrypt function to find our decrypted location hint and display the photo
Citations: n/a
'''
from functionsPackage.functions import *


#this specifies the file paths and invokes the decryption function
json_file_path = "hints.json"
english_txt_file_path = "english.txt"
decrypted_location = decrypt_location(json_file_path, english_txt_file_path)
print(decrypted_location, '(co-op programs)')


# this specifies the file path and diplays image
display_image('HermanSchneider.jpg')

