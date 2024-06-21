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
old_text = '''Lannister_25 = {
	name = Cerenna # Canon
	dynasty = dynn_Lannister
	female = yes

	religion = the_seven_main
	culture = westerman

	father = Lannister_18
	mother = Lefford_2

	8276.1.1 = {
		birth = yes
		employer = Lannister_1 # Tywin Lannister
	}
	8300.2.9 = { employer = Lannister_6 } # Cersei Lannister
}
Lannister_26 = {
	name = Myrielle # Canon
	dynasty = dynn_Lannister
	female = yes

	religion = the_seven_main
	culture = westerman

	father = Lannister_18
	mother = Lefford_2

	8278.1.1 = {
		birth = yes
		employer = Lannister_1 # Tywin Lannister
	}
	8300.2.9 = { employer = Lannister_6 } # Cersei Lannister
}'''

new_text = '''Lannister_25 = {
	name = Cerenna # Canon
	dynasty = dynn_Lannister
	female = yes

	religion = the_seven_main
	culture = westerman

	father = Lannister_18
	mother = Lefford_2

	8282.1.1 = {
		birth = yes
		employer = Lannister_1 # Tywin Lannister
	}
	8300.2.9 = { employer = Lannister_6 } # Cersei Lannister
}
Lannister_26 = {
	name = Myrielle # Canon
	dynasty = dynn_Lannister
	female = yes

	religion = the_seven_main
	culture = westerman

	father = Lannister_18
	mother = Lefford_2

	8284.1.1 = {
		birth = yes
		employer = Lannister_1 # Tywin Lannister
	}
	8300.2.9 = { employer = Lannister_6 } # Cersei Lannister
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_westerlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Lannister Girls Updated")


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
Westerling_49 = {
	name = Elys	# Canon
	dynasty = dynn_Westerling

	martial = 10

	religion = the_seven_main
	culture = westerman

	father = Westerling_46
	mother = Westerling_p_1

	trait = education_martial_2
	trait = brave

	8229.1.1 = { birth = yes }
	8245.1.1 = { trait = knight }
'''

new_text = '''
Westerling_49 = {
	name = Elys	# Canon
	dynasty = dynn_Westerling

	martial = 10
	prowess = 9

	religion = the_seven_main
	culture = westerman

	father = Westerling_46
	mother = Westerling_p_1

	trait = education_martial_2
	trait = brave
	trait = diligent
	trait = honest

	8229.1.1 = { birth = yes }
	8245.1.1 = { 
		trait = knight
		trait = education_martial_prowess_3
		effect = {
			add_trait = lifestyle_blademaster
			add_trait_xp = {
				trait = lifestyle_blademaster
				value = trait_third_level
			}
		}
	}
	8255.1.1 = {
		add_spouse = Bettley_24
	}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_westerlands_ancestors.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Elys Westerling updated")


# In[8]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''
Lydden_3 = {
	name = Lewys # Canon, a lord
	dynasty = dynn_Lydden

	dna = Lydden_3

	religion = the_seven_main
	culture = westerman

	father = Lydden_1
	mother = Lydden_rs_1

	8239.1.1 = { birth = yes }
	8255.1.1 = { add_spouse = Lydden_rs_2 }
}
Lydden_rs_2 = {
	name = Janna
	female = yes

	dna = Lydden_rs_2

	religion = the_seven_main
	culture = westerman

	8239.1.1 = { birth = yes }
}
### Issue of Lewys
Lydden_4 = {
	name = Jonos
	dynasty = dynn_Lydden

	dna = Lydden_4

	religion = the_seven_main
	culture = westerman

	father = Lydden_3
	mother = Lydden_rs_2

	8259.1.1 = { birth = yes }
	8277.1.1 = { add_spouse = Lydden_rs_3 }
}
Lydden_rs_3 = {
	name = Cerenna
	female = yes

	dna = Lydden_rs_3

	religion = the_seven_main
	culture = westerman

	8259.1.1 = { birth = yes }
}'''

new_text = '''
Lydden_3 = {
	name = Lewys # Canon, a lord
	dynasty = dynn_Lydden

	dna = Lydden_3

	religion = the_seven_main
	culture = westerman

	father = Lydden_1
	mother = Lydden_rs_1

	8239.1.1 = { birth = yes }
	8245.1.1 = { trait = lustful }
	8255.1.1 = { 
		trait = arrogant
		trait = diligent
		trait = knight
		trait = education_martial_2
	}
	8255.1.1 = { add_spouse = Lydden_rs_2 }
}
Lydden_rs_2 = {
	name = Jeyne
	female = yes
	dynasty = dynn_Bracken
	dna = Lydden_rs_2

	religion = the_seven_main
	culture = riverlander

	father = Bracken_81
	mother = Bracken_rs_13

	8239.1.1 = { birth = yes }
}
### Issue of Lewys
Lydden_4 = {
	name = Jonos
	dynasty = dynn_Lydden

	dna = Lydden_4

	religion = the_seven_main
	culture = westerman

	father = Lydden_3
	mother = Lydden_rs_2
    
	trait = physique_good_2

	8259.1.1 = { birth = yes }
	8265.1.1 = { trait = content }
	8275.1.1 = { 
		trait = arrogant
		trait = diligent
		trait = knight
		trait = education_martial_2
	}
	8277.1.1 = { add_spouse = Lydden_rs_3 }
}
Lydden_rs_3 = {
	name = Cerenna
	female = yes
	dynasty = dynn_Drox

	religion = the_seven_main
	culture = westerman

	father = Drox_27
	mother = Drox_rs_1

	dna = Lydden_rs_3

	8259.1.1 = { birth = yes }
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_westerlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Lord Lydden Updated and his heir")


# In[4]:


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
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_westerlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("")


# In[5]:


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
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_westerlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("")


# In[9]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''
### Issue of Jonos
Lydden_5 = {
	name = Alys
	dynasty = dynn_Lydden
	female = yes

	dna = Lydden_5

	religion = the_seven_main
	culture = westerman

	father = Lydden_4
	mother = Lydden_rs_3

	8279.1.1 = { birth = yes }
}
Lydden_6 = {
	name = Harys
	dynasty = dynn_Lydden

	dna = Lydden_6

	religion = the_seven_main
	culture = westerman

	father = Lydden_4
	mother = Lydden_rs_3

	8281.1.1 = { birth = yes }
}
Lydden_7 = {
	name = Bethany
	dynasty = dynn_Lydden
	female = yes

	#dna = Lydden_7

	religion = the_seven_main
	culture = westerman

	father = Lydden_4
	mother = Lydden_rs_3

	8283.1.1 = { birth = yes }
}'''

new_text = '''
### Issue of Jonos
Lydden_5 = {
	name = Alys
	dynasty = dynn_Lydden
	female = yes

	dna = Lydden_5

	religion = the_seven_main
	culture = westerman

	father = Lydden_4
	mother = Lydden_rs_3

	8282.1.1 = { birth = yes }
}
Lydden_6 = {
	name = Harys
	dynasty = dynn_Lydden

	dna = Lydden_6

	religion = the_seven_main
	culture = westerman

	father = Lydden_4
	mother = Lydden_rs_3

	8285.1.1 = { birth = yes }
}
Lydden_7 = {
	name = Bethany
	dynasty = dynn_Lydden
	female = yes

	#dna = Lydden_7

	religion = the_seven_main
	culture = westerman

	father = Lydden_4
	mother = Lydden_rs_3

	8287.1.1 = { birth = yes }
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_westerlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Young Lydden's updated")


# In[ ]:




