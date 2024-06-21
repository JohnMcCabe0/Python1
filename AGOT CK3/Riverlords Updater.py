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
old_text = '''
	8257.1.1 = { birth = yes }
	8270.1.1 = { trait = lustful }
	8273.1.1 = {
		add_spouse = Bracken_rs_3
		trait = knight
		effect = {
			if = { 
				limit = { character:Tully_9 = { is_alive = yes } }
				add_opinion = {
					target = character:Tully_9 # Brynden Tully
					modifier = friendliness_opinion
					opinion = 20
				}
			}
		}
	}
	8274.1.1 = { add_spouse = Bracken_rs_4 }
	8279.1.1 = { add_spouse = Bracken_rs_5 }'''

new_text = '''
	8257.1.1 = { birth = yes }
	8263.1.1 = { 
		trait = arrogant
		trait = honest 
	}
	8270.1.1 = {
		trait = lustful
		trait = wrathful
	}
	8273.1.1 = {
		add_spouse = Bracken_rs_3
		trait = knight
		effect = {
			if = { 
				limit = { character:Tully_9 = { is_alive = yes } }
				add_opinion = {
					target = character:Tully_9 # Brynden Tully
					modifier = friendliness_opinion
					opinion = 20
				}
			}
		}
	}
	8281.1.1 = { add_spouse = Bracken_rs_4 }
	8285.1.1 = { add_spouse = Bracken_rs_5 }'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Jonos Bracken updated.")


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
Darry_rs_2 = {
	name = Marissa
	female = yes
'''

new_text = '''
Darry_rs_2 = {
	name = Marissa
	female = yes
	dynasty = dynn_Bracken
	father = Bracken_16
	mother = Bracken_rs_7
'''

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
old_text = '''
Nutt_rs_5 = {
	name = Hazel
	female = yes
'''

new_text = '''
Nutt_rs_5 = {
	name = Hazel
	female = yes
	dynasty = dynn_Bracken
	father = Bracken_21
	mother = Bracken_rs_9
'''

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


# In[1]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''Bracken_rs_3 = {
	name = Emberlei # Mentioned
	female = yes

	religion = the_seven_main
	culture = riverlander

	8257.1.1 = { birth = yes }
	8274.1.1 = {
		death = { death_reason = death_childbirth }
	}
}'''

new_text = '''Bracken_rs_3 = {
    name = Emberlei # Mentioned
    female = yes
    dynasty = dynn_Mooton
    
    religion = the_seven_main
    culture = riverlander
    
    trait = beauty_good_1
    
    father = Mooton_1
    mother = Mooton_rs_1
    
    8257.1.1 = { birth = yes }
    8281.1.1 = { death = { death_reason = death_childbirth } }
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Emberlei Bracken updated.")


# In[3]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''Bracken_rs_4 = {
	name = Jeyne # Mentioned
	female = yes

	religion = the_seven_main
	culture = riverlander

	8258.1.1 = { birth = yes }
	8279.1.1 = {
		trait = ill
		death = { death_reason = death_ill }
	}
}'''

new_text = '''Bracken_rs_4 = {
    name = Jeyne # Mentioned
    female = yes
	dynasty = dynn_Darry

	religion = the_seven_main
	culture = riverlander

	father = Darry_1
	mother = Darry_rs_1
    
	8259.1.1 = { birth = yes }
	8284.1.1 = { death = { death_reason = death_horse_riding_accident } }
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Jeyne Bracken updated.")


# In[4]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''Bracken_rs_5 = {
	name = Lysa # Mentioned
	female = yes

	#dna = "agbie0cdeb0"

	religion = the_seven_main
	culture = riverlander

	trait = chaste
	trait = zealous
	trait = charming

	disallow_random_traits = yes

	8263.1.1 = { birth = yes }'''

new_text = '''Bracken_rs_5 = {
    name = Lysa # Mentioned
    female = yes
	dynasty = dynn_Bracken

	religion = the_seven_main
	culture = riverlander

	father = Bracken_16
	mother = Bracken_rs_7
    
	trait = chaste
	trait = zealous
	trait = charming
    
	8266.1.1 = { birth = yes }'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Lysa Bracken updated.")


# In[5]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''
Bracken_7 = {
	name = Barbara # Canon
	dynasty = dynn_Bracken
	female = yes

	dna = Bracken_7

	religion = the_seven_main
	culture = riverlander

	father = Bracken_3
	mother = Bracken_rs_3

	8273.1.1 = { birth = yes }'''

new_text = '''
Bracken_7 = {
	name = Barbara # Canon
	dynasty = dynn_Bracken
	female = yes

	dna = Bracken_7

	religion = the_seven_main
	culture = riverlander

	father = Bracken_3
	mother = Bracken_rs_3
    
	trait = beauty_good_2
    
	diplomacy = 8
    
	disallow_random_traits = yes

	8279.1.1 = { birth = yes }
	8283.1.1 = {
		trait = just
		trait = proud
	}
	8285.1.1 = {
		trait = calm
	}
	8295.1.1 = {
		trait = honest
		trait = education_diplomacy_3
	}
    8296.1.1 = {
		effect = {
			agot_safe_betrothal_history_effect = { TARGET = character:Bracken_13 } # Her Cousin
		}
	}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Barbara Bracken updated.")


# In[6]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''
Bracken_8 = {
	name = Jayne # Canon
	dynasty = dynn_Bracken
	female = yes

	dna = Bracken_8

	religion = the_seven_main
	culture = riverlander

	father = Bracken_3
	mother = Bracken_rs_3

	8274.1.1 = { birth = yes }'''

new_text = '''
Bracken_8 = {
	name = Jayne # Canon
	dynasty = dynn_Bracken
	female = yes

	dna = Bracken_8

	religion = the_seven_main
	culture = riverlander

	father = Bracken_3
	mother = Bracken_rs_3
    
	trait = beauty_good_1
	
	intrigue = 8
	diplomacy = 9

	8281.1.1 = { birth = yes }
	8283.1.1 = {
		trait = ambitious
		trait = gregarious
	}
	8285.1.1 = {
		trait = proud
	}
	8297.1.1 = {
		trait = honest
		trait = education_intrigue_3
	}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Jayne Bracken updated.")


# In[7]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''
Bracken_9 = {
	name = Harry # Canon
	dynasty = dynn_Bracken

	dna = Bracken_9

	prowess = 6

	religion = the_seven_main
	culture = riverlander

	father = Bracken_3

	trait = bastard
	give_nickname = nick_rivers

	trait = beauty_good_2

	8277.1.1 = { birth = yes }'''

new_text = '''
Bracken_9 = {
	name = Harry # Canon
	dynasty = dynn_Bracken

	dna = Bracken_9

	prowess = 6

	religion = the_seven_main
	culture = riverlander

	father = Bracken_3

	trait = bastard
	give_nickname = nick_rivers

	trait = beauty_good_2

	8277.1.1 = { birth = yes }
	8284.1.1 = { trait = ambitious }
	8293.1.1 = { 
		trait = brave
		trait = wrathful
	}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Bastard Bracken updated.")


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
Bracken_10 = {
	name = Catelyn # Canon
	dynasty = dynn_Bracken
	female = yes

	dna = Bracken_10

	religion = the_seven_main
	culture = riverlander

	father = Bracken_3
	mother = Bracken_rs_5

	8279.1.1 = { birth = yes }'''

new_text = '''
Bracken_10 = {
	name = Catelyn # Canon
	dynasty = dynn_Bracken
	female = yes

	dna = Bracken_10

	religion = the_seven_main
	culture = riverlander

	father = Bracken_3
	mother = Bracken_rs_5
    
	trait = beauty_good_1

	8289.1.1 = { birth = yes }
	8295.1.1 = { trait = brave }'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Baby Bracken' updated.")


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
Bracken_11 = {
	name = Bess # Canon
	dynasty = dynn_Bracken
	female = yes

	dna = Bracken_11

	religion = the_seven_main
	culture = riverlander

	father = Bracken_3
	mother = Bracken_rs_5

	8281.1.1 = { birth = yes }'''

new_text = '''
Bracken_11 = {
	name = Bess # Canon
	dynasty = dynn_Bracken
	female = yes

	dna = Bracken_11

	religion = the_seven_main
	culture = riverlander

	father = Bracken_3
	mother = Bracken_rs_5
    
	trait = beauty_good_1

	8292.1.1 = { birth = yes }'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Baby Bracken' updated.")


# In[10]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''
Bracken_12 = {
	name = Alysanne # Canon
	dynasty = dynn_Bracken
	female = yes

	dna = Bracken_12

	religion = the_seven_main
	culture = riverlander

	father = Bracken_3
	mother = Bracken_rs_5

	8284.1.1 = { birth = yes }'''

new_text = '''
Bracken_12 = {
	name = Alysanne # Canon
	dynasty = dynn_Bracken
	female = yes

	dna = Bracken_12

	religion = the_seven_main
	culture = riverlander

	father = Bracken_3
	mother = Bracken_rs_5
    
	trait = beauty_good_3

	8294.1.1 = { birth = yes }'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Baby Bracken' updated.")


# In[15]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

# Define the old and new text
old_text = '''
Bracken_13 = {
	name = Hendry # Canon
	dynasty = dynn_Bracken

	dna = Bracken_13

	prowess = 6

	religion = the_seven_main
	culture = riverlander

	father = Bracken_4
	mother = Bracken_rs_6

	8279.1.1 = { birth = yes }'''

new_text = '''
Bracken_13 = {
	name = Hendry # Canon
	dynasty = dynn_Bracken

	dna = Bracken_13

	prowess = 6

	religion = the_seven_main
	culture = riverlander

	father = Bracken_4
	mother = Bracken_rs_6

	8279.1.1 = { birth = yes }
	8285.1.1 = { trait = arrogant }
	8289.1.1 = { trait = brave }
	8293.1.1 = { trait = ambitious }'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Bracken Nephew updated.")


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
Bracken_16 = {
	name = Petyr 
	dynasty = dynn_Bracken

	dna = Bracken_16

	religion = the_seven_main
	culture = riverlander

	father = Bracken_81
	mother = Bracken_rs_13

	8238.1.1 = { birth = yes }
	8254.1.1 = { trait = knight }
	8256.1.1 = { add_spouse = Bracken_rs_7 }
	8289.1.1 = { death = yes }
}
'''

new_text = '''
Bracken_16 = {
	name = Petyr 
	dynasty = dynn_Bracken

	dna = Bracken_16

	religion = the_seven_main
	culture = riverlander

	father = Bracken_81
	mother = Bracken_rs_13
    
	trait = education_diplomacy_2
	trait = beauty_good_1

	8238.1.1 = { birth = yes }
	8254.1.1 = { trait = knight }
	8256.1.1 = { add_spouse = Bracken_rs_7 }
	8272.1.1 = { 
		employer = Bracken_81
	}
	8278.1.1 = { 
		employer = Bracken_1
	}
	8281.1.1 = { 
		employer = Bracken_3
	}
	8289.1.1 = { trait = blind }
}
'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Bracken Bro wife updated.")


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
Bracken_1 = {
	name = Amos # a lord, offered his daughter to Blackfish
	dynasty = dynn_Bracken

	religion = the_seven_main
	culture = riverlander

	father = Bracken_81
	mother = Bracken_rs_13

	trait = education_martial_2

	8232.1.1 = { birth = yes }
	8248.1.1 = { trait = knight }
	8252.1.1 = { add_spouse = Bracken_rs_1 }
	8281.1.1 = { death = yes }
}
Bracken_rs_1 = {
	name = Bethany
	female = yes

	religion = the_seven_main
	culture = riverlander

	8232.1.1 = { birth = yes }
	8281.1.1 = { death = yes }
}'''

new_text = '''
Bracken_1 = {
	name = Amos # a lord, offered his daughter to Blackfish
	dynasty = dynn_Bracken

	religion = the_seven_main
	culture = riverlander

	father = Bracken_81
	mother = Bracken_rs_13

	trait = education_martial_2
    
	trait = physique_good_2
     
	diplomacy = 3
	martial = 5

	8232.1.1 = { birth = yes }
	8238.1.1 = { trait = brave }
	8248.1.1 = { 
		trait = wrathful
		trait = ambitious
		trait = knight
		trait = education_martial_prowess_2
	}
	8252.1.1 = { add_spouse = Bracken_rs_1 }
	8281.1.1 = { death = { death_reason = death_hunting_accident } }
}
Bracken_rs_1 = {
	name = Bethany
	female = yes
	dynasty = dynn_Lychester

	religion = the_seven_main
	culture = riverlander

	father = Lychester_27
    
	trait = beauty_good_2
    
	diplomacy = 6

	8232.1.1 = { birth = yes }
	8248.1.1 = { 
		trait = wrathful
		trait = ambitious
		trait = zealous
		trait = education_diplomacy_2
	}
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Bracken Dada")


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
Bracken_81 = {
	name = Hoster # a lord
	dynasty = dynn_Bracken

	religion = the_seven_main
	culture = riverlander

	father = Bracken_79

	8205.1.1 = { birth = yes }
	8225.1.1 = { add_spouse = Bracken_rs_13 }
	8278.1.1 = { death = yes }
}
Bracken_rs_13 = {
	name = Merianne
	female = yes

	religion = the_seven_main
	culture = riverlander

	8205.1.1 = { birth = yes }
	8278.1.1 = { death = yes }
}'''

new_text = '''
Bracken_81 = {
	name = Hoster # a lord
	dynasty = dynn_Bracken

	religion = the_seven_main
	culture = riverlander

	father = Bracken_79
    
	trait = physique_good_2
     
	diplomacy = 8
	martial = 7

	8205.1.1 = { birth = yes }
	8211.1.1 = { trait = brave }
	8221.1.1 = { 
		trait = gregarious
		trait = honest
		trait = knight
		trait = education_martial_2
	}
	8225.1.1 = { add_spouse = Bracken_rs_13 }
	8278.1.1 = { death = yes }
}
Bracken_rs_13 = {
	name = Catelyn
	female = yes
	dynasty = dynn_Tully

	religion = the_seven_main
	culture = riverlander

	father = Tully_63
	mother = Tully_rs_5

	8205.1.1 = { birth = yes }
	8278.1.1 = { death = yes }
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands_ancestors.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Bracken Elder")


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
Bracken_4 = {
	name = Humfrey
	dynasty = dynn_Bracken

	dna = Bracken_4

	religion = the_seven_main
	culture = riverlander

	father = Bracken_1
	mother = Bracken_rs_1
    
	trait = education_martial_2
	trait = brave

	8259.1.1 = { birth = yes }
	8275.1.1 = { trait = knight }
	8277.1.1 = { add_spouse = Bracken_rs_6 }
	8299.11.5 = {
		death = {
			death_reason = death_bloody_wedding # The Red Wedding
			killer = Frey_1 # Walder Frey
		}
	}
}
Bracken_rs_6 = {
	name = Barba
	female = yes

	religion = the_seven_main
	culture = riverlander

	8259.1.1 = { birth = yes }
}
Bracken_5 = {
	name = Catelyn # Mentioned, offered as spouse for Blackfish
	dynasty = dynn_Bracken
	female = yes

	dna = Bracken_5

	religion = the_seven_main
	culture = riverlander

	father = Bracken_1
	mother = Bracken_rs_1

	8262.1.1 = { birth = yes }
}
Bracken_6 = {
	name = Willis # Semi-Canon, Wyllis Bracken
	dynasty = dynn_Bracken

	dna = Bracken_6

	prowess = 3

	religion = the_seven_main
	culture = riverlander

	father = Bracken_1
	mother = Bracken_rs_1

	8265.1.1 = { birth = yes }
	8281.1.1 = { trait = knight }
}'''

new_text = '''
Bracken_4 = {
	name = Humfrey
	dynasty = dynn_Bracken

	dna = Bracken_4

	religion = the_seven_main
	culture = riverlander

	father = Bracken_1
	mother = Bracken_rs_1

	trait = physique_good_1

	8259.1.1 = { birth = yes }
	8265.1.1 = { trait = brave }
	8275.1.1 = { 
		trait = gregarious
		trait = honest
		trait = knight
		trait = education_martial_2
	}
	8277.1.1 = { add_spouse = Bracken_rs_6 }
	8299.11.5 = {
		death = {
			death_reason = death_bloody_wedding # The Red Wedding
			killer = Frey_1 # Walder Frey
		}
	}
}
Bracken_rs_6 = {
	name = Barba
	female = yes
	dynasty = dynn_Bracken

	religion = the_seven_main
	culture = riverlander

	father = Bracken_2
	mother = Bracken_rs_2

	8259.1.1 = { birth = yes }
}
Bracken_5 = {
	name = Catelyn # Mentioned, offered as spouse for Blackfish
	dynasty = dynn_Bracken
	female = yes

	dna = Bracken_5

	religion = the_seven_main
	culture = riverlander

	father = Bracken_1
	mother = Bracken_rs_1

	8262.1.1 = { birth = yes }
}
Bracken_6 = {
	name = Willis # Semi-Canon, Wyllis Bracken
	dynasty = dynn_Bracken

	dna = Bracken_6

	prowess = 3

	religion = the_seven_main
	culture = riverlander

	father = Bracken_1
	mother = Bracken_rs_1

	8265.1.1 = { birth = yes }
	8271.1.1 = { trait = trusting }
	8281.1.1 = { 
		trait = zealous
		trait = honest
		trait = knight
		trait = education_martial_1
	}
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_riverlands.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Bracken Sibs")


# In[ ]:




