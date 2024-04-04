# Built-in imports
import math

# Your code below

"""
generate a dict for GRADE range

read file

keys: class, name, overall, grade

calculate overall using formula

determine grade
return a list of dict, each for each student

grade analysis: take in data -> list[class][grade]
"""
#Dict for grade range
GRADE = {}
for i in range(0, 40):
  GRADE[i] = 'U'
for i in range(40, 45):
  GRADE[i] = 'S'
for i in range(45, 50):
  GRADE[i] = 'E'
for i in range(50, 55):
  GRADE[i] = 'D'
for i in range(55, 60):
  GRADE[i] = 'C'
for i in range(60, 70):
  GRADE[i] = 'B'
for i in range(70, 101):
  GRADE[i] = 'A'

#return data for each student
def read_testscores(filename):
  #initiate list
  data_list = []
  
  with open(filename, 'r') as f:
    
    header = f.readline() #header
    for line in f:
      data_dict = {} #initiate dict inside of list
      line = line.strip().split(',')
      data_dict["class"] = line[0]
      data_dict["name"] = line[1]
      p1 = int(line[2])
      p2 = int(line[3])
      p3 = int(line[4])
      p4 = int(line[5])
      overall = (p1/30 * 15) + (p2/40 * 30) + (p3/80 * 35) + (p4/30 * 20)
      overall = math.ceil(overall)
      data_dict["overall"] = overall
      data_dict["grade"] = GRADE[overall]
      data_list.append(data_dict)
      
  return data_list



#return count for each grade of each class
def analyze_grades(studentdata):
  analysis = {} #matrix
  for student in studentdata:
    class_ = student['class']
    grade = student['grade']

    if class_ not in analysis:
      analysis[class_] = {}
      analysis[class_]['A'] = 0
      analysis[class_]['B'] = 0
      analysis[class_]['C'] = 0
      analysis[class_]['D'] = 0
      analysis[class_]['E'] = 0
      analysis[class_]['S'] = 0
      analysis[class_]['U'] = 0

    if grade in analysis[class_]:
      analysis[class_][grade] += 1

  return analysis