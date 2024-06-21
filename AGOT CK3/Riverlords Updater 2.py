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
old_text = '''Mallister_7 = {
	name = Patrek # Canon
	dynasty = dynn_Mallister

	dna = Mallister_7

	prowess = 6

	religion = the_seven_main
	culture = riverlander

	father = Mallister_4
	mother = Mallister_rs_3

	trait = education_martial_1
	trait = gregarious
	trait = rowdy

	disallow_random_traits = yes

	8277.1.1 = { birth = yes }
	8290.1.1 = { trait = lustful }
	8293.1.1 = {
		trait = knight
		trait = lifestyle_hunter
		effect = {
			add_trait_xp = {
				trait = lifestyle_hunter
				track = falconer
				value = {
					integer_range = {
						min = medium_lifestyle_random_xp_low
						max = medium_lifestyle_random_xp_high
					}
				}
			}
		}
	}'''

new_text = '''Mallister_7 = {
	name = Patrek # Canon
	dynasty = dynn_Mallister

	dna = Mallister_7

	prowess = 8
	martial = 8

	religion = the_seven_main
	culture = riverlander

	father = Mallister_4
	mother = Mallister_rs_3

	trait = rowdy
	trait = beauty_good_1

	disallow_random_traits = yes

	8277.1.1 = { birth = yes }
	8285.1.1 = { 
		trait = brave 
		trait = gregarious
	}
	8292.1.1 = { trait = lustful }
	8293.1.1 = {
		trait = knight
		trait = education_martial_3
		trait = lifestyle_hunter
		effect = {
			add_trait_xp = {
				trait = lifestyle_hunter
				track = falconer
				value = {
					integer_range = {
						min = medium_lifestyle_random_xp_low
						max = medium_lifestyle_random_xp_high
					}
				}
			}
		}
	}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Lord Mallister's Lovely Children.")


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
Mallister_8 = {
	name = Sarya
	dynasty = dynn_Mallister
	female = yes

	religion = the_seven_main
	culture = riverlander

	father = Mallister_4
	mother = Mallister_rs_3

	8278.1.1 = { birth = yes }
}
Mallister_9 = {
	name = Minisa
	dynasty = dynn_Mallister
	female = yes

	religion = the_seven_main
	culture = riverlander


	father = Mallister_4
	mother = Mallister_rs_3

	8285.1.1 = { birth = yes }
}'''

new_text = '''
Mallister_8 = {
	name = Sarya
	dynasty = dynn_Mallister
	female = yes

	religion = the_seven_main
	culture = riverlander

	father = Mallister_4
	mother = Mallister_rs_3

	8282.1.1 = { birth = yes }
}
Mallister_9 = {
	name = Minisa
	dynasty = dynn_Mallister
	female = yes

	religion = the_seven_main
	culture = riverlander

	father = Mallister_4
	mother = Mallister_rs_3

	8285.1.1 = { birth = yes }
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Lord Mallister's Lovely Children.")


# In[ ]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''Blackwood_rs_3 = {
	name = Morya
	female = yes

	dna = Blackwood_rs_3

	religion = old_gods_south
	culture = riverlander

	trait = beauty_good_1

	8260.1.1 = { birth = yes }'''

new_text = '''Blackwood_rs_3 = {
	name = Arrana
	female = yes
	dynasty = dynn_Stark

	religion = old_gods_south
	culture = northman

	father = Stark_extra_Artos_1
	mother = Stark_rs_extra_Artos_1

	trait = education_diplomacy_2
	trait = diligent
	trait = arrogant
	trait = fecund
	trait = beauty_good_2

	dna = Blackwood_rs_3

	8260.1.1 = { birth = yes }'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Lord Blackwood's Wife.")


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
Blackwood_rs_1 = {
	name = Leana
	female = yes

	religion = the_seven_main
	culture = riverlander'''

new_text = '''
Blackwood_rs_1 = {
	name = Leana
	female = yes
	dynasty = dynn_Royce

	religion = weirwood_of_the_seven
	culture = valeman
    
	father = Royce_96
	mother = Egen_25'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Lord Blackwood's Wife.")


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
### Issue of Tytos
Blackwood_10 = {
	name = Brynden # Canon
	dynasty = dynn_Blackwood

	dna = Blackwood_10

	martial = 5
	prowess = 6

	religion = old_gods_south
	culture = riverlander

	father = Blackwood_6
	mother = Blackwood_rs_3

	trait = education_martial_2

	8280.1.1 = { birth = yes }
	8296.1.1 = { trait = knight }
}'''

new_text = '''
### Issue of Tytos
Blackwood_10 = {
	name = Brynden # Canon
	dynasty = dynn_Blackwood

	dna = Blackwood_10

	martial = 7
	prowess = 6
    
	trait = fecund
	trait = beauty_good_2

	religion = old_gods_south
	culture = riverlander

	father = Blackwood_6
	mother = Blackwood_rs_3

	trait = education_martial_3

	8280.1.1 = { birth = yes }
	8288.1.1 = { 
		trait = brave
		trait = diligent
	}
	8296.1.1 = {  
		trait = just
		trait = education_martial_prowess_2
		trait = lifestyle_blademaster
		trait = knight 
	}
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Lord Blackwood's Children.")


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
Blackwood_11 = {
	name = Lucas # Canon
	dynasty = dynn_Blackwood

	dna = Blackwood_11

	martial = 4
	prowess = 6

	religion = old_gods_south
	culture = riverlander

	father = Blackwood_6
	mother = Blackwood_rs_3

	trait = education_martial_1
	trait = zealous
	trait = brave
	trait = rowdy

	disallow_random_traits = yes

	8281.1.1 = { birth = yes }
	8297.1.1 = { trait = knight }'''

new_text = '''
Blackwood_11 = {
	name = Lucas # Canon
	dynasty = dynn_Blackwood

	dna = Blackwood_11

	martial = 4
	prowess = 6

	religion = old_gods_south
	culture = riverlander

	father = Blackwood_6
	mother = Blackwood_rs_3

	trait = education_martial_1
	trait = rowdy

	disallow_random_traits = yes

	8281.1.1 = { birth = yes }
	8288.1.1 = { 
		trait = zealous
		trait = brave
	}
	8297.1.1 = {
		trait = strong
		trait = calm
		trait = lifestyle_blademaster
		trait = education_martial_prowess_3
		trait = knight 
	}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Lucas Blackwood.")


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
Blackwood_12 = {
	name = Hoster # Canon
	dynasty = dynn_Blackwood

	dna = Blackwood_12

	martial = 4

	religion = old_gods_south
	culture = riverlander

	father = Blackwood_6
	mother = Blackwood_rs_3

	trait = education_diplomacy_1
	trait = scholar
	trait = gregarious
	trait = trusting
	trait = physique_bad_1
	trait = curious

	disallow_random_traits = yes

	8283.1.1 = { birth = yes }
	8300.4.15 = { employer = Baratheon_7 } # Tommen Lannister
}'''

new_text = '''
Blackwood_12 = {
	name = Hoster # Canon
	dynasty = dynn_Blackwood

	dna = Blackwood_12

	martial = 4
	learning = 10

	religion = old_gods_south
	culture = riverlander

	father = Blackwood_6
	mother = Blackwood_rs_3

	trait = intellect_good_2
	trait = physique_bad_1
	trait = curious

	disallow_random_traits = yes

	8283.1.1 = { birth = yes }
	8289.1.1 = {
		trait = gregarious
		trait = trusting
	}
	8299.1.1 = {
		trait = scholar
		trait = calm
		trait = education_diplomacy_1
	}
	8300.4.15 = { employer = Baratheon_7 } # Tommen Lannister
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Lord Blackwood's Children.")


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
Mallister_rs_3 = {
	name = Della
	female = yes'''

new_text = '''
Mallister_rs_3 = {
	name = Della
	female = yes
	dynasty = dynn_Vance

	religion = the_seven_main
	culture = riverlander'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("")


# In[ ]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = ''''''

new_text = ''''''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("")

