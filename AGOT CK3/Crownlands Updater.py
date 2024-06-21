#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''
Rykker_rs_1 = {
	name = Leana
	female = yes
'''

new_text = '''
Rykker_rs_1 = {
	name = Leana
	female = yes

	father = Darklyn_42
	mother = Darklyn_rs_8
	
	trait=twin
'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_crownlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Rykker updated")


# In[ ]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''
Darklyn_45 = {
	name = Robert # Mentioned
	dynasty = dynn_Darklyn

	religion = the_seven_main
	culture = crownlander

	father = Darklyn_42
	mother = Darklyn_rs_8
'''

new_text = '''
Darklyn_45 = {
	name = Robert # Mentioned
	dynasty = dynn_Darklyn

	religion = the_seven_main
	culture = crownlander

	father = Darklyn_42
	mother = Darklyn_rs_8
	
	trait=twin
'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_crownlands_ancestors.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Twin updated")

