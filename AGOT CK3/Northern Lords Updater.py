#!/usr/bin/env python
# coding: utf-8

# In[1]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''Glover_2 = {
	name = Ethan # Canon
	dynasty = dynn_Glover
	dna = Glover_2

	prowess = 6

	religion = old_gods_south
	culture = wolfswood_clansman

	father = Glover_1
	mother = Glover_rs_1

	8258.1.1 = { birth = yes }'''

new_text = '''Glover_2 = {
	name = Ethan # Canon
	dynasty = dynn_Glover
	dna = Glover_2

	prowess = 6

	religion = old_gods_south
	culture = wolfswood_clansman

	father = Glover_1
	mother = Glover_rs_1

	8266.1.1 = { birth = yes }'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Glovers Updated")


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
Stark_127 = {
	name = Lyarra # Canon, married Rickard Stark
	dynasty = dynn_Stark
	female = yes
	dna = Stark_127

	father = Stark_120
	mother = Flint_90

	religion = old_gods_south
	culture = northman

	8239.1.1 = { birth = yes }
	8270.1.1 = { death = yes }
}'''

new_text = '''
Stark_127 = {
	name = Lyarra # Canon, married Rickard Stark
	dynasty = dynn_Stark
	female = yes
	dna = Stark_127

	father = Stark_120
	mother = Flint_90

	religion = old_gods_south
	culture = northman

	8239.1.1 = { birth = yes }
	8294.1.1 = { death = yes }
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north_ancestors.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Ben Updated")


# In[2]:


#def replace_text_in_file(filename, old_text, new_text):
#    with open(filename, 'r') as file:
#        filedata = file.read()

    # Replace the old text with the new text
#    filedata = filedata.replace(old_text, new_text)

#    with open(filename, 'w') as file:
#        file.write(filedata)

#old_text = ''''''

#new_text = ''''''

#filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

#replace_text_in_file(filename, old_text, new_text)

#print(" Updated")


# In[2]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

old_text = '''
Ryswell_7 = {
	name = Rickard # Canon
	dynasty = dynn_Ryswell
	dna = Ryswell_7

	religion = old_gods_south
	culture = barrowman

	father = Ryswell_3
	mother = Ryswell_rs_2

	trait = ambitious
	trait = arrogant
	trait = bossy
	
	disallow_random_traits = yes

	8259.1.1 = { birth = yes }
	8274.1.1 = { trait = lustful }
}
Ryswell_6 = {
	name = Roger # Canon
	dynasty = dynn_Ryswell
	dna = Ryswell_6

	religion = old_gods_south
	culture = barrowman

	father = Ryswell_3
	mother = Ryswell_rs_2

	trait = ambitious
	trait = arrogant
	trait = cynical

	8260.1.1 = { birth = yes }
}
Ryswell_8 = {
	name = Roose # Canon
	dynasty = dynn_Ryswell
	dna = Ryswell_8

	religion = old_gods_south
	culture = barrowman

	father = Ryswell_3
	mother = Ryswell_rs_2

	trait = ambitious
	trait = arrogant
	trait = rude

	8265.1.1 = { birth = yes }
}'''

new_text = '''
Ryswell_7 = {
	name = Rickard # Canon
	dynasty = dynn_Ryswell
	dna = Ryswell_7

	religion = old_gods_south
	culture = barrowman
    
	martial = 5
	diplomacy = 5
	intrigue = 5
	stewardship = 5
	learning = 5
	prowess = 6

	father = Ryswell_3
	mother = Ryswell_rs_2
    
	trait = twin

	8262.1.1 = { birth = yes }
	8272.1.1 = {
		trait = ambitious
		trait = arrogant
	}
	8278.1.1 = {
		trait = lustful
		trait = education_martial_2
	}
	8283.9.1 = { 
		add_spouse = Dustin_11 #solidify the claim
	}
}
Ryswell_6 = {
	name = Roger # Canon
	dynasty = dynn_Ryswell
	dna = Ryswell_6

	religion = old_gods_south
	culture = barrowman

	father = Ryswell_3
	mother = Ryswell_rs_2
    
	martial = 5
	diplomacy = 8
	intrigue = 8
	stewardship = 7
	learning = 6
	prowess = 6
    
	trait = intellect_good_1
	trait = twin

	8262.1.1 = { birth = yes }
	8272.1.1 = {
		trait = ambitious
		trait = arrogant
	}
	8278.1.1 = {
		trait = cynical
		trait = gregarious
		trait = education_diplomacy_4
	}
	8283.9.1 = { 
		add_spouse = Dustin_8 #solidify the claim
	}
}
Ryswell_8 = {
	name = Roose # Canon
	dynasty = dynn_Ryswell
	dna = Ryswell_8

	religion = old_gods_south
	culture = barrowman

	father = Ryswell_3
	mother = Ryswell_rs_2
    
	martial = 7
	prowess = 8

	8276.1.1 = { birth = yes }
	8286.1.1 = {
		trait = ambitious
		trait = arrogant
	}
	8292.1.1 = {
		trait = rude
		trait = gregarious
		trait = education_martial_3
	}
}'''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print(" Updated The Ryswell Boys")


# In[4]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

old_text = '''
Glover_5 = {
	name = Robett # Canon
	dynasty = dynn_Glover
	dna = Glover_5

	martial = 5
	diplomacy = 5
	intrigue = 5
	stewardship = 5
	learning = 5
	prowess = 6

	religion = old_gods_south
	culture = wolfswood_clansman

	father = Glover_1
	mother = Glover_rs_1

	trait = education_martial_2
	trait = gregarious
	trait = compassionate
	trait = just
	trait = pensive'''

new_text = '''
Glover_5 = {
	name = Robett # Canon
	dynasty = dynn_Glover
	dna = Glover_5

	martial = 8
	diplomacy = 5
	intrigue = 5
	stewardship = 5
	learning = 5
	prowess = 6

	religion = old_gods_south
	culture = wolfswood_clansman

	father = Glover_1
	mother = Glover_rs_1

	trait = education_martial_3
	trait = gregarious
	trait = ambitious
	trait = just
	trait = arrogant'''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print(" Updated Glover")


# In[5]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

old_text = '''
Umber_11 = {
	name = Jon # Canon, AKA: Smalljon
	dynasty = dynn_Umber
	dna = Umber_11

	martial = 8
	diplomacy = 5
	intrigue = 5
	stewardship = 5
	learning = 5
	prowess = 6

	religion = old_gods_south
	culture = northman

	father = Umber_8
	mother = Umber_rs_5

	trait = education_martial_2
	trait = physique_good_2'''

new_text = '''
Umber_11 = {
	name = Jon # Canon, AKA: Smalljon
	dynasty = dynn_Umber
	dna = Umber_11

	martial = 8
	diplomacy = 5
	intrigue = 5
	stewardship = 5
	learning = 5
	prowess = 6

	religion = old_gods_south
	culture = northman

	father = Umber_8
	mother = Umber_rs_5

	trait = education_martial_2
	trait = physique_good_3'''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print(" Updated Smalljon")


# In[6]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

old_text = ''''''

new_text = ''''''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print(" Updated ")


# In[7]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

old_text = ''''''

new_text = ''''''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print(" Updated ")


# In[8]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

old_text = ''''''

new_text = ''''''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print(" Updated ")

