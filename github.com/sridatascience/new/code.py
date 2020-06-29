# --------------
# Code starts here

class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class = class_1 + class_2
print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)
# Code ends here


# --------------
# Code starts here
courses = {'Math': 65,'English':70, 'History':80, 'French': 70, "Science": 60}
total = 0
for marks in courses.values():
    print(marks)
    total = total + marks
print(total)
percentage = total/500*100
print(percentage)
# Code ends here


# --------------
# Code starts here
mathematics ={'Geoffrey Hintion': 78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70}
mathsscores =[]
for values in mathematics.values():
    print(values)
    mathsscores.append(values)
max_marks_scored = max(mathsscores)
print(max_marks_scored)

for key,value in mathematics.items():
    if value == max_marks_scored:
        print("The highest scorer is ", key)
        topper = key
print(topper)
# Code ends here  


# --------------
# Given string
topper = 'andrew ng'


# Code starts here
first_name, last_name = topper.split()
full_name = last_name+' '+first_name
certificate_name = full_name.upper()
# Code ends here


