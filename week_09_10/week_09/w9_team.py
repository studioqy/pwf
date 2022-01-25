
import csv

def main():
  loop = True
  while loop:
    students_dictionary = read_file("students.csv")

    check_input = True
    while check_input:
      user_input = input("Please enter an I-Number (xxxxxxxxx): ")
      user_input = user_input.replace("-","")
      if user_input == "quit":
        check_input = False
        loop = False
      elif len(user_input) > 9:
        print("Invalid I-number: input too long")
      elif len(user_input) < 9:
        print("Invalid I-number: input too short")
      elif not user_input.isdigit():
        print("Invalid I-number")
      else:
        check_input = False
    if loop:
      get_student(user_input, students_dictionary)

def read_file(file):
  students = {}
  with open(file) as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
      key = row[0]
      students[key] = row[1]
  return students

def get_student(user_input, students_dictionary):
  if user_input in students_dictionary:
    name = students_dictionary[user_input]
    print(f"{name}")
  else:
    print("No such student")


main()