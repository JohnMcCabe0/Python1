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

old_text = '''
Drumm_1 = {
	name = Dunstan # Canon, AKA: The Bonehand, a lord
	dynasty = dynn_Drumm
	dna = Drumm_1
'''

new_text = '''
Drumm_1 = {
	name = Dunstan # Canon, AKA: The Bonehand, a lord
	dynasty = dynn_Drumm
	dna = Drumm_1
	
	trait = fecund
'''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_iron_islands.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print("Updated")

