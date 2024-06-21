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
Redfort_rs_3 = {
	name = Bethany # Mentioned
	female = yes

	religion = the_seven_main
	culture = valeman

	8251.1.1 = { birth = yes }
	8297.1.1 = { death = yes } # Horton is a suitor for Lysa in books
}'''

new_text = '''
Redfort_rs_3 = {
	name = Bethany # Mentioned
	dynasty = dynn_Shett
	female = yes

	religion = the_seven_main
	culture = valeman

	father = Shett_32
	mother = Shett_rs_6

	8251.1.1 = { birth = yes }
	8297.1.1 = { death = { death_reason = death_accident } } # Horton is a suitor for Lysa in books
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_vale.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Redfort's Wives Updated.")


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
### Issue of Elys
Waynwood_6 = {
	name = Alyssa # Mentioned, married Denys Arryn
	dynasty = dynn_Waynwood
	female = yes

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4

	8246.1.1 = { birth = yes }
	8282.1.1 = { employer = Arryn_3 } # Jon Arryn
	8283.1.1 = { trait = depressed_1 }
	8284.1.1 = {
		death = { death_reason = death_depressed } # Died of grief after husband's death
	}
}
Waynwood_7 = {
	name = Jasper # Canon
	dynasty = dynn_Waynwood

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4

	8247.1.1 = { birth = yes }
	8250.1.1 = {
		death = { death_reason = death_accident } # Kicked by a horse
	}
}
Waynwood_8 = {
	name = Amanda # Mentioned
	dynasty = dynn_Waynwood
	female = yes

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4

	8248.1.1 = { birth = yes }
	8251.1.1 = {
		trait = smallpox
		death = { death_reason = death_smallpox }
	}
}
Waynwood_9 = {
	name = Alayne # Mentioned
	dynasty = dynn_Waynwood
	female = yes

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4

	8249.1.1 = { birth = yes }
	8251.1.1 = {
		trait = smallpox
		death = { death_reason = death_smallpox }
	}
}
Waynwood_10 = {
	name = Marsella # Mentioned
	dynasty = dynn_Waynwood
	female = yes

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4

	trait = education_learning_1

	8250.1.1 = { birth = yes }
	8251.1.1 = { trait = scarred }
	8264.1.1 = { trait = septon } # Septa
	8280.1.1 = { death = yes }
}
Waynwood_11 = {
	name = Jeyne # Mentioned
	dynasty = dynn_Waynwood
	female = yes

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4

	8251.1.1 = { birth = yes }
	8270.1.1 = { trait = silent_sister }
	8283.1.1 = { death = yes }
}
Waynwood_13 = {
	name = Carolei # Mentioned
	dynasty = dynn_Waynwood
	female = yes

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4

	trait = infertile

	8252.1.1 = { birth = yes }
	8294.1.1 = { death = yes }
}
Waynwood_14 = {
	name = Rowena # Mentioned
	dynasty = dynn_Waynwood
	female = yes

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4

	8253.1.1 = { birth = yes }
	8271.1.1 = { death = { death_reason = death_murder } } # Carried off by Burned Men
}
Waynwood_15 = {
	name = Anya # Mentioned, married Ronnel Hardyng
	dynasty = dynn_Waynwood
	female = yes

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4

	8254.1.1 = { birth = yes }
	8282.2.1 = {
		trait = ill
		death = { death_reason = death_ill }
	}
}
### Issue of Jeyne
Waynwood_12 = {
	name = Jon # Mentioned
	dynasty = dynn_Waynwood

	religion = the_seven_main
	culture = valeman

	mother = Waynwood_11

	trait = bastard
	give_nickname = nick_stone

	8268.1.1 = { birth = yes }
	8269.1.1 = { death = yes }
}'''

new_text = '''
### Issue of Elys
Waynwood_6 = {
	name = Alyssa # Mentioned, married Denys Arryn
	dynasty = dynn_Waynwood
	female = yes

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4
    
	trait = beauty_good_2
	trait = proud
	trait = ambitious
	trait = gregarious
	trait = education_intrigue_2
    
	intrigue = 7
	diplomacy = 7

	8255.1.1 = { birth = yes }
	8282.1.1 = { employer = Arryn_3 } # Jon Arryn
	8283.1.1 = { trait = depressed_1 }
	8286.1.1 = {
		death = { death_reason = death_depressed } # Died of grief after husband's death
	}
}
Waynwood_7 = {
	name = Jasper # Canon
	dynasty = dynn_Waynwood

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4
    
	trait = beauty_good_3

	8256.1.1 = { birth = yes }
	8260.1.1 = {
		death = { death_reason = death_accident } # Kicked by a horse
	}
}
Waynwood_8 = {
	name = Amanda # Mentioned
	dynasty = dynn_Waynwood
	female = yes

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4
    
	trait = beauty_good_1

	8259.1.1 = { birth = yes }
	8266.1.1 = {
		trait = smallpox
		death = { death_reason = death_smallpox }
	}
}
Waynwood_9 = {
	name = Alayne # Mentioned
	dynasty = dynn_Waynwood
	female = yes

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4

	8261.1.1 = { birth = yes }
	8266.1.1 = {
		trait = smallpox
		death = { death_reason = death_smallpox }
	}
}
Waynwood_10 = {
	name = Marsella # Mentioned
	dynasty = dynn_Waynwood
	female = yes

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4

	trait = education_learning_1

	8262.1.1 = { birth = yes }
	8266.1.1 = { trait = scarred }
	8278.1.1 = { trait = septon } # Septa
}
Waynwood_11 = {
	name = Jeyne # Mentioned
	dynasty = dynn_Waynwood
	female = yes

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4
    
	trait = beauty_good_1

	8263.1.1 = { birth = yes }
	8279.1.1 = { trait = silent_sister }
}
Waynwood_13 = {
	name = Carolei # Mentioned
	dynasty = dynn_Waynwood
	female = yes

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4

	trait = infertile

	8264.1.1 = { birth = yes }
	8294.1.1 = { death = yes }
}
Waynwood_14 = {
	name = Rowena # Mentioned
	dynasty = dynn_Waynwood
	female = yes

	religion = the_seven_main
	culture = valeman
    
	trait = beauty_good_1

	father = Waynwood_3
	mother = Arryn_4

	8265.1.1 = { birth = yes }
	8281.1.1 = { death = { death_reason = death_murder } } # Carried off by Burned Men
}
Waynwood_15 = {
	name = Anya # Mentioned, married Ronnel Hardyng
	dynasty = dynn_Waynwood
	female = yes

	religion = the_seven_main
	culture = valeman

	father = Waynwood_3
	mother = Arryn_4
    
	trait = beauty_good_3

	8266.1.1 = { birth = yes }
	8282.2.1 = {
		trait = ill
		death = { death_reason = death_ill }
	}
}
### Issue of Jeyne
Waynwood_12 = {
	name = Jon # Mentioned
	dynasty = dynn_Waynwood

	religion = the_seven_main
	culture = valeman

	mother = Waynwood_11

	trait = bastard
	give_nickname = nick_stone

	8279.1.1 = { birth = yes }
	8280.1.1 = { death = yes }
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_vale.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Jon Arryn's Nieces Updated")


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
Arryn_4 = {
	name = Alys # Canon
	dynasty = dynn_Arryn
	female = yes
	dna = Arryn_4

	religion = the_seven_main
	culture = valeman

	father = Arryn_1
	mother = Arryn_rs_1

	trait = education_diplomacy_3

	8224.1.1 = { birth = yes }
	8254.1.1 = { death = yes }
}
Arryn_5 = {
	name = Ronnel # Canon
	dynasty = dynn_Arryn
	dna = Arryn_5

	martial = 8
	diplomacy = 6
	intrigue = 6
	stewardship = 6
	learning = 5
	prowess = 6

	religion = the_seven_main
	culture = valeman

	father = Arryn_1
	mother = Arryn_rs_1

	trait = education_martial_2

	8228.1.1 = { birth = yes }
	8245.1.1 = { trait = knight }
	8260.1.1 = { add_spouse = Belmore_2 } # Alayne Belmore
	8262.1.1 = {
		trait = ill
		death = {
			death_reason = death_ill # Belly ache
		}
	}
}'''

new_text = '''
Arryn_4 = {
	name = Alys # Canon
	dynasty = dynn_Arryn
	female = yes
	dna = Arryn_4

	religion = the_seven_main
	culture = valeman

	father = Arryn_1
	mother = Arryn_rs_1

	trait = education_diplomacy_3
	trait = stubborn
	trait = content
	trait = diligent

	8234.1.1 = { birth = yes }
	8288.1.1 = { death = yes }
}
Arryn_5 = {
	name = Ronnel # Canon
	dynasty = dynn_Arryn
	dna = Arryn_5

	martial = 8
	diplomacy = 6
	intrigue = 6
	stewardship = 6
	learning = 5
	prowess = 6

	religion = the_seven_main
	culture = valeman

	father = Arryn_1
	mother = Arryn_rs_1

	trait = education_martial_2
	trait = stubborn
	trait = honest
	trait = brave

	8238.1.1 = { birth = yes }
	8256.1.1 = { trait = knight }
	8260.1.1 = { add_spouse = Belmore_2 } # Alayne Belmore
	8262.1.1 = {
		trait = ill
		death = {
			death_reason = death_ill # Belly ache
		}
	}
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_vale.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Jon Arryn's Siblings updated")


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
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_vale.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Redfort's Wives Updated.")


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
Waynwood_3 = {
	name = Elys # Canon, grandfather of Harry 'the Heir'
	dynasty = dynn_Waynwood

	religion = the_seven_main
	culture = valeman
	sexuality = heterosexual

	father = Waynwood_1
	mother = Waynwood_rs_1

	trait = education_martial_1
	trait = fecund
	trait = arrogant

	8221.1.1 = { birth = yes }
	8237.1.1 = { trait = knight }
	8245.1.1 = { add_spouse = Arryn_4 } # Alys Arryn
	8273.1.1 = { death = yes }
}'''

new_text = '''
Waynwood_3 = {
	name = Elys # Canon, grandfather of Harry 'the Heir'
	dynasty = dynn_Waynwood

	religion = the_seven_main
	culture = valeman
	sexuality = heterosexual

	father = Waynwood_1
	mother = Waynwood_rs_1

	trait = education_martial_1
	trait = beauty_good_3
	trait = fecund
	trait = arrogant
	trait = gregarious
	trait = brave

	8223.1.1 = { birth = yes }
	8239.1.1 = { 
		trait = knight 
		trait = lifestyle_blademaster
		trait = education_martial_prowess_4
	}
	8254.1.1 = { add_spouse = Arryn_4 } # Alys Arryn
	8288.1.1 = { death = yes }
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_vale.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Harry the heir's Grandfather")


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
Redfort_rs_2 = {
	name = Jessamyn # Mentioned
	female = yes

	religion = the_seven_main
	culture = moonman

	8250.1.1 = { birth = yes }
	8275.1.1 = { death = yes }
}'''

new_text = '''
Redfort_rs_2 = {
	name = Jessamyn # Mentioned
	female = yes
	dynasty = dynn_Tollett

	religion = the_seven_main
	culture = fingerman

	father = Tollett_1
	mother = Tollett_rs_1
    
	trait = beauty_good_1

	8250.1.1 = { birth = yes }
	8275.1.1 = {
		death = { death_reason = death_vanished } # Abducted by Wildlings
	}
}'''

# Specify the filename
filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_vale.txt'  # Use a raw string

# Call the function to replace the text
replace_text_in_file(filename, old_text, new_text)

print("Redfort's Wives Updated.")


# In[6]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

old_text = '''
Royce_8 = {
	name = Lorra # Mentioned
	dynasty = dynn_Royce
	female = yes
	dna = Royce_8

	religion = weirwood_of_the_seven
	culture = valeman

	father = Royce_2
	mother = Waynwood_17

	8286.1.1 = { birth = yes }
}
Royce_9 = {
	name = Myranda # Mentioned
	dynasty = dynn_Royce
	female = yes
	dna = Royce_9

	religion = weirwood_of_the_seven
	culture = valeman

	father = Royce_2
	mother = Waynwood_17

	8287.1.1 = { birth = yes }
}
Royce_10 = {
	name = Alayne # Mentioned
	dynasty = dynn_Royce
	female = yes
	dna = Royce_10

	religion = weirwood_of_the_seven
	culture = valeman

	father = Royce_2
	mother = Waynwood_17

	8288.1.1 = { birth = yes }
}'''

new_text = '''
Royce_8 = {
	name = Lorra # Mentioned
	dynasty = dynn_Royce
	female = yes
	dna = Royce_8

	religion = weirwood_of_the_seven
	culture = valeman

	father = Royce_2
	mother = Waynwood_17

	8286.1.1 = { 
		birth = yes  
		employer = Royce_1
	}
}
Royce_9 = {
	name = Myranda # Mentioned
	dynasty = dynn_Royce
	female = yes
	dna = Royce_9

	religion = weirwood_of_the_seven
	culture = valeman

	father = Royce_2
	mother = Waynwood_17

	8287.1.1 = {
		birth = yes  
		employer = Royce_1
	}
}
Royce_10 = {
	name = Alayne # Mentioned
	dynasty = dynn_Royce
	female = yes
	dna = Royce_10

	religion = weirwood_of_the_seven
	culture = valeman

	father = Royce_2
	mother = Waynwood_17

	8288.1.1 = {
		birth = yes  
		employer = Royce_1
	}
}'''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_vale.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print("Updated")


# In[ ]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

old_text = '''
### Issue of Yohn
Royce_2 = {
	name = Andar # Canon
	dynasty = dynn_Royce
	dna = Royce_2
'''

new_text = '''
### Issue of Yohn
Royce_2 = {
	name = Andar # Canon
	dynasty = dynn_Royce
	dna = Royce_2
	
	trait = fecund
'''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_vale.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print("Updated")

