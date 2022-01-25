intro = "This program is an implementation of the Rosenberg Self-Esteem Scale.\n\
This program will show you ten statements that you could possibly\n\
apply to yourself. Please rate how much you agree with each of the\n\
statements by responding with one of these four letters:\n\n\
D means you strongly disagree with the statement.\n\
d means you disagree with the statement.\n\
a means you agree with the statement.\n\
A means you strongly agree with the statement.\n"

statements = ["I feel that I am a person of worth, at least on an equal plane with others.", "I feel that I have a number of good qualities.", "All in all, I am inclined to feel that I am a failure.", "I am able to do things as well as most other people.", "I feel I do not have much to be proud of.", "I take a positive attitude toward myself.", "On the whole, I am satisfied with myself.", "I wish I could have more respect for myself.", "I certainly feel useless at times.", "At times I think I am no good at all."]

statement_pattern = [True,True,False,True,False,True,True,False,False,False]

def main():
  print(intro)
  responses = get_response()
  score = total_score(responses)

  print(f'\nYour score is {score}.\nA score below 15 may indicate problematic low self-esteem.')
  #[[a,True],[A,False],[d,False]]


def total_score(responses):
  total = 0
  for i in responses:
    if i[0] == "D":
      if i[1]:
        total += 0
      else:
        total += 3
    elif i[0] == "d":
      if i[1]:
        total += 1
      else:
        total += 2
    elif i[0] == "a":
      if i[1]:
        total += 2
      else:
        total += 1
    elif i[0] == "A":
      if i[1]:
        total += 3
      else:
        total += 0
    else:
      return "error"
  return total

def get_response():
  responses = []
  for text in statements:
    response = input(text+"\nEnter D, d, a, or A: ")
    responses.append([response, statement_pattern[statements.index(text)]])
  print(responses)
  return responses

main()