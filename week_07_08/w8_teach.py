# Each value in the people dictionary is a list. These
# are the indexes of the elements in those lists.
NAME_INDEX = 0
GENDER_INDEX = 1
BIRTH_YEAR_INDEX = 2
DEATH_YEAR_INDEX = 3

# Each value in the marriages dictionary is a list.
# These are the indexes of the elements in those lists.
HUSBAND_KEY_INDEX = 0
WIFE_KEY_INDEX = 1
WEDDING_YEAR_INDEX = 2


def main():
    people_dict = {
        # Each item in the people dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "P". Each value is a list of data about a person.
        # Each item in the dictionary is in this format:
        # person_key: [name, gender, birth_year, death_year]
        "P143": ["Lola Park", "F", 1663, 1706],
        "P338": ["Savanna Foster", "F", 1674, 1723],
        "P201": ["Tiffany Hughes", "F", 1689, 1747],
        "P203": ["Ignacio Torres", "M", 1693, 1758],
        "P128": ["Yasmin Li", "F", 1701, 1716],
        "P342": ["Trent Ross", "M", 1705, 1757],
        "P202": ["Samyukta Nguyen", "M", 1717, 1774],
        "P132": ["Joel Johnson", "M", 1724, 1800],
        "P445": ["Whitney Nelson", "F", 1757, 1823],
        "P318": ["Khalid Ali", "M", 1759, 1814],
        "P317": ["Davina Patel", "F", 1775, 1860],
        "P313": ["Enzo Ruiz", "M", 1782, 1782],
        "P475": ["Lauren Smith", "F", 1800, 1802],
        "P455": ["Lucas Ross", "M", 1800, 1853],
        "P435": ["Jamal Gray", "M", 1810, 1831],
        "P204": ["Fatima Soares", "F", 1812, 1898],
        "P206": ["Ephraim Foster", "M", 1831, 1885],
        "P500": ["Peter Price", "M", 1832, 1878],
        "P207": ["Rosalina Jimenez", "F", 1875, 1956],
        "P425": ["Rachel Johnson", "F", 1876, 1940],
        "P121": ["Vanessa Bennet", "F", 1880, 1960],
        "P152": ["Jose Castillo", "M", 1884, 1931],
        "P205": ["Liam Myers", "M", 1902, 1950],
        "P465": ["Isabella Lopez", "F", 1907, 1959],
        "P168": ["Megan Anderson", "F", 1909, 1945]
    }

    marriages_dict = {
        # Each item in the marriages dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "M". Each value is a list of data about a marriage.
        # Each item in the dictionary is in this format:
        # marriage_key: [husband_key, wife_key, wedding_year]
        "M48": ["P203", "P201", 1711],
        "M45": ["P342", "P338", 1722],
        "M36": ["P203", "P201", 1724],
        "M47": ["P202", "P445", 1774],
        "M21": ["P132", "P445", 1775],
        "M59": ["P132", "P317", 1792],
        "M63": ["P318", "P445", 1804],
        "M12": ["P318", "P317", 1808],
        "M54": ["P435", "P204", 1830],
        "M34": ["P455", "P204", 1853],
        "M55": ["P500", "P317", 1859],
        "M52": ["P206", "P204", 1875],
        "M78": ["P152", "P121", 1905],
        "M50": ["P152", "P425", 1917],
        "M64": ["P205", "P465", 1925],
        "M62": ["P152", "P207", 1925],
        "M70": ["P152", "P168", 1928]
    }

    # Call the print_death_age function to print
    # each person's name and age at death.
    print_death_age(people_dict)

    # Print a blank line.
    print()

    # Call the count_genders function to count
    # and print the number of males and females.
    count_genders(people_dict)

    # Print a blank line.
    print()

    # Call the print_marriages function to print
    # human readable data about the marriages.
    print_marriages(marriages_dict, people_dict)

    print()

    count_marriages(marriages_dict, people_dict)

    print()

    marriage_count(people_dict, marriages_dict)


def print_death_age(people_dict):
    """For each person in the people dictionary,
    print the person's name and age at death.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    print("Ages at Death")
    for person in people_dict:
      name = people_dict[person][NAME_INDEX]
      birth_year = people_dict[person][BIRTH_YEAR_INDEX]
      death_year = people_dict[person][DEATH_YEAR_INDEX]
      death_age = int(death_year) - int(birth_year)
      print(f"{name} {death_age} {birth_year}-{death_year}")
    print("")
    


def count_genders(people_dict):
    """Count and print the number of males
    and females in the people dictionary.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    genders = []
    for person in people_dict.items():
      people_gen = person[1]
      genders.append(people_gen[GENDER_INDEX])
    male_num = genders.count('M')
    female_num = genders.count('F')
    print(f'Genders\nNumber of males: {male_num}\nNumber of females: {female_num}')
    return None

def marriage_count(people_dict, marriages_dict):
  for person_key in people_dict.items():
    values = person_key[1]
    name = values[0]
    print(name, end=' ')
    husbands = []
    wives = []
    for marriage_key in marriages_dict.items():
      mar_values = marriage_key[1]
      husbands.append(mar_values[HUSBAND_KEY_INDEX])
      wives.append(mar_values[WIFE_KEY_INDEX])
    husbands_count = husbands.count(person_key[0])
    wives_count = wives.count(person_key[0])
    total_marriages = husbands_count + wives_count
    print(total_marriages)

def print_marriages(marriages_dict, people_dict):
    """For each marriage in the marriages dictionary, print
    the husband's name, his age at wedding, the wedding year,
    the wife's name, and her age at wedding.

    Parameters
        marriages_dict: a dictionary that contains data about
            marriages. Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    for key in marriages_dict:
      marriage = marriages_dict[key]
      husband = people_dict[marriage[HUSBAND_KEY_INDEX]]
      husband_name = husband[NAME_INDEX]

      wife = people_dict[marriage[WIFE_KEY_INDEX]]
      wife_name = wife[NAME_INDEX]
      
      marriage_date = marriage[WEDDING_YEAR_INDEX]
      husband_age = marriage_date - husband[BIRTH_YEAR_INDEX]
      wife_age = marriage_date - wife[BIRTH_YEAR_INDEX]

      print(f"{husband_name} ({husband_age}) <{marriage_date}> {wife_name} ({wife_age})")

def count_marriages(marriages_dict, people_list):
  marriage_numbers = []
  names_list = []
  for key in marriages_dict:
    marriage = marriages_dict[key]
    husband = marriage[HUSBAND_KEY_INDEX]
    wife = marriage[WIFE_KEY_INDEX]

    if husband not in names_list:
      marriage_numbers.append(1)
      names_list.append(husband)
    elif husband in names_list:
      index = names_list.index(husband)
      marriage_numbers[index] += 1

    if wife not in names_list:
      marriage_numbers.append(1)
      names_list.append(wife)
    elif wife in names_list:
      index = names_list.index(wife)
      marriage_numbers[index] += 1
  
  for name in names_list:
    index = names_list.index(name) 
    count = marriage_numbers[index]
    real_name = people_list[name][NAME_INDEX]
    print(f"{real_name} {count}")

    
# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
