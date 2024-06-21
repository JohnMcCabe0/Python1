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

old_text = '''
Mollen_4 = {
	name = Hycinth
	dynasty = dynn_Mollen
	female = yes

	religion = old_gods_south
	culture = northman

	father = Mollen_2
	mother = Mollen_rs_1

	8262.1.1 = { birth = yes }
}
Mollen_5 = {
	name = Binhilde
	dynasty = dynn_Mollen
	female = yes

	religion = old_gods_south
	culture = northman

	father = Mollen_2
	mother = Mollen_rs_1

	8257.1.1 = { birth = yes }
}'''

new_text = '''
Mollen_4 = {
	name = Alysanne
	female = yes

	religion = old_gods_south
	culture = northman

	8262.1.1 = { birth = yes }
	8280.1.1 = { add_spouse = Mollen_1 }
}
Mollen_5 = {
	name = Gwyn
	dynasty = dynn_Mollen
	female = yes

	religion = old_gods_south
	culture = northman
	trait = twin

	father = Mollen_1
	mother = Mollen_4

	8283.1.1 = { birth = yes }
}
Mollen_extra_1 = {
	name = Lunella
	dynasty = dynn_Mollen
	female = yes

	religion = old_gods_south
	culture = northman
	trait = twin

	father = Mollen_1
	mother = Mollen_4

	8283.1.1 = { birth = yes }
}
Mollen_extra_2 = {
	name = Rodrik
	dynasty = dynn_Mollen

	religion = old_gods_south
	culture = northman

	father = Mollen_1
	mother = Mollen_4

	8286.1.1 = { birth = yes }
}
Mollen_extra_3 = {
	name = Arrana
	dynasty = dynn_Mollen
	female = yes

	religion = old_gods_south
	culture = northman

	father = Mollen_1
	mother = Mollen_4

	8293.1.1 = { birth = yes }
}'''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print("Updated")


# In[2]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

old_text = '''
Karstark_rs_1 = {
	name = Arrana
	female = yes'''

new_text = '''
Karstark_rs_1 = {
	name = Arrana
	female = yes
	dynasty = dynn_Stark
	father = Stark_124
	mother = Stark_rs_124'''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print("Updated Lady Karstark")


# In[3]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

old_text = '''
Wull_3 = {
	name = Beron
	dynasty = dynn_Wull'''

new_text = '''
Wull_3 = {
	name = Beron
	dynasty = dynn_Wull
    
	trait = physique_good_2
    
	trait = education_martial_2
	trait = brave
	trait = strong'''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print("Updated Young Wull")


# In[4]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

old_text = '''
Wull_2 = {
	name = Hugo # Canon, AKA: Big Bucket
	dynasty = dynn_Wull
	dna = Wull_2'''

new_text = '''
Wull_2 = {
	name = Hugo # Canon, AKA: Big Bucket
	dynasty = dynn_Wull
	dna = Wull_2
    
	trait = physique_good_2'''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print("Updated Wull")


# In[5]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

old_text = '''
Wull_1 = {
	name = Ranulf # a lord
	dynasty = dynn_Wull'''

new_text = '''
Wull_1 = {
	name = Ranulf # a lord
	dynasty = dynn_Wull
    
	trait = physique_good_2'''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print("Updated Old Wull")


# In[6]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

old_text = '''
Umber_rs_5 = {
	name = Raya
	female = yes'''

new_text = '''
Umber_rs_5 = {
	name = Raya
	female = yes
	dynasty = dynn_Wull
    
	father = Wull_1
	mother = Wull_rs_1
    
	trait = physique_good_2'''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print("Updated Lady Umber")


# In[7]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

old_text = '''
Ryswell_3 = {
	name = Rodrik # Canon, a lord
	dynasty = dynn_Ryswell
	dna = Ryswell_3
'''

new_text = '''
Ryswell_3 = {
	name = Rodrik # Canon, a lord
	dynasty = dynn_Ryswell
	dna = Ryswell_3
	trait = fecund
'''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print("Updated Lady Karstark")


# In[8]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

old_text = '''
Hornwood_3 = {
	name = Daryn # Canon
	dynasty = dynn_Hornwood
	dna = Hornwood_3

	prowess = 6

	religion = old_gods_south
	culture = northman

	father = Hornwood_2
	mother = Manderly_12

	8276.1.1 = { birth = yes }'''

new_text = '''
Hornwood_3 = {
	name = Daryn # Canon
	dynasty = dynn_Hornwood
	dna = Hornwood_3

	prowess = 6

	religion = old_gods_south
	culture = northman

	father = Hornwood_2
	mother = Manderly_12

	8281.1.1 = { birth = yes }
	8289.1.1 = { 
		trait = brave
	}
	8295.1.1 = { # Betrothal to Alys announced
		effect = {
			if = { 
				limit = { character:Karstark_19 = { is_alive = yes } }
				create_betrothal = character:Karstark_19
			}
		}
	}
	8297.1.1 = { 
		trait = gregarious
		trait = education_martial_2
		trait = honorable
		trait = education_martial_prowess_3
	}'''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print("Updated Daryn Hornwood")


# In[9]:


def replace_text_in_file(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the old text with the new text
    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

old_text = '''
### Issue of Wylis
Manderly_9 = {
	name = Wynafryd # Canon
	dynasty = dynn_Manderly
	female = yes
	dna = Manderly_9

	religion = the_seven_main
	culture = harborman

	father = Manderly_7
	mother = Woolfield_2

	trait = education_intrigue_2
	trait = patient
	trait = deceitful
	trait = charming
	
	disallow_random_traits = yes 

	8280.1.1 = { birth = yes }'''

new_text = '''
### Issue of Wylis
Manderly_9 = {
	name = Wynafryd # Canon
	dynasty = dynn_Manderly
	female = yes
	dna = Manderly_9

	religion = the_seven_main
	culture = harborman

	father = Manderly_7
	mother = Woolfield_2

	trait = intellect_good_2
	trait = charming
    
	martial = 5
	diplomacy = 9
	intrigue = 9
	stewardship = 8
	learning = 8
	
	disallow_random_traits = yes 

	8280.1.1 = { 
		birth = yes 
		employer = Manderly_6
	}
	8290.1.1 = { 
		trait = patient
		trait = deceitful
	}
	8296.1.1 = { 
		trait = brave
		trait = patient
		trait = education_intrigue_3
	}'''

filename = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\1158310\2962333032\history\characters\00_agot_char_north.txt'  # Use a raw string

replace_text_in_file(filename, old_text, new_text)

print(" Updated Manderly")

