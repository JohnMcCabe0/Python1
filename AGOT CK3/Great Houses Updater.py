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
old_text = '''Stark_1 = {
	name = Rickard # Canon, THE Rickard Stark, a lord
	dynasty = dynn_Stark
	dna = Stark_1

	martial = 7
	diplomacy = 5
	intrigue = 5
	stewardship = 5
	learning = 5
	prowess = 6

	religion = old_gods_south
	culture = northman
	sexuality = heterosexual

	father = Stark_122 # Edwyle Stark
	mother = Locke_50

	trait = education_martial_2
	trait = honorable
	trait = authoritative
	trait = just
	trait = brave
	trait = bossy 
	
	disallow_random_traits = yes 

	8239.1.1 = { birth = yes }
	8255.1.1 = { add_spouse = Stark_127 } # Lyarra Stark'''

new_text = '''Stark_1 = {
	name = Rickard # Canon, THE Rickard Stark, a lord
	dynasty = dynn_Stark
	dna = Stark_1

	martial = 5
	diplomacy = 7
	intrigue = 8
	stewardship = 8
	learning = 5
	prowess = 6

	religion = old_gods_south
	culture = northman
	sexuality = heterosexual

	father = Stark_122 # Edwyle Stark
	mother = Locke_50
    
	trait = physique_good_1

	trait = education_diplomacy_3
	trait = bossy 
	
	disallow_random_traits = yes 

	8239.1.1 = { birth = yes }
	8249.1.1 = { 
		trait = honorable
		trait = authoritative
		trait = just
		trait = ambitious
	}
	8255.1.1 = { add_spouse = Stark_127 } # Lyarra Stark'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Rickard Stark updated")


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
Stark_2 = {
	name = Brandon # Canon, a lord
	dynasty = dynn_Stark
	dna = Stark_2
'''

new_text = '''
Stark_2 = {
	name = Brandon # Canon, a lord
	dynasty = dynn_Stark
	dna = Stark_2

	trait = physique_good_1
	trait = fecund
	trait = beauty_good_2'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Brandon Stark updated")


# In[5]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''	father = Stark_1
	mother = Stark_127

	8266.10.1 = {
		birth = yes
		add_character_flag = tomboy
	}
	8281.1.1 = {
		trait = compassionate
		trait = brave
		trait = stubborn
		trait = education_martial_prowess_3 # Knight of the Laughing Tree
	}'''

new_text = '''	father = Stark_1
	mother = Stark_127

	8266.10.1 = {
		birth = yes
		add_character_flag = tomboy
	}
	8277.1.1 = {
		trait = compassionate
		trait = brave
		trait = stubborn
	}
	8281.1.1 = {
		trait = education_martial_prowess_3 # Knight of the Laughing Tree
	}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Lyanna Stark updated")


# In[3]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''
	8267.1.1 = { birth = yes }
	8273.8.1 = { trait = brave }
	8275.8.1 = {
		trait = honest
		trait = honorable
	}
	8283.1.1 = { trait = content }'''

new_text = '''
	8269.1.1 = { birth = yes }
	8273.8.1 = { trait = brave }
	8275.8.1 = {
		trait = honest
		trait = honorable
	}
	8283.1.1 = { trait = content }'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Benjen Stark updated")


# In[1]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''
### Issue of Eddard
Stark_6 = {
	name = Robb # Canon, AKA: Young Wolf, a lord
	dynasty = dynn_Stark
	dna = Stark_6
'''

new_text = '''
### Issue of Eddard
Stark_6 = {
	name = Robb # Canon, AKA: Young Wolf, a lord
	dynasty = dynn_Stark
	dna = Stark_6
	
	trait = physique_good_1
	trait = beauty_good_1
'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Robb Stark updated")


# In[2]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''
Tyrell_12 = {
	name = Garlan # Canon, THE Garlan Tyrell
	dynasty = dynn_Tyrell
	dna = Tyrell_12
'''

new_text = '''
Tyrell_12 = {
	name = Garlan # Canon, THE Garlan Tyrell
	dynasty = dynn_Tyrell
	dna = Tyrell_12

	trait = physique_good_2
'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_reach.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Garlan Tyrell updated")


# In[ ]:




