def extractIntoDictionaries(students):
	students = students.split(',');
	return {'name':students[0],'roll_num':students[1],'english':students[2],
	'mathematics':students[3],'computer_science':students[4]};

def highest(students,subject):
	studentsDictionary = map(extractIntoDictionaries,students)
	studentsDictionary = filter(lambda x:x[subject]!='DNA',studentsDictionary)
	result = reduce(lambda x,y:x if int(x[subject])>int(y[subject]) else y,studentsDictionary)
	return result;


def lowest(students,subject):
	studentsDictionary = map(extractIntoDictionaries,students)
	studentsDictionary = filter(lambda x:x[subject]!='DNA',studentsDictionary)
	result = reduce(lambda x,y:x if int(x[subject])<int(y[subject]) else y,studentsDictionary)
	return result;

def above(students,subject,score):
	studentsDictionary = map(extractIntoDictionaries,students)
	studentsDictionary = filter(lambda x:x[subject]!='DNA',studentsDictionary)
	result = filter(lambda x:int(x[subject])>score,studentsDictionary)
	return result;

def below(students,subject,score):
	studentsDictionary = map(extractIntoDictionaries,students)
	studentsDictionary = filter(lambda x:x[subject]!='DNA',studentsDictionary)
	result = filter(lambda x:int(x[subject])<score,studentsDictionary)
	return result;

def phoneBook(students):
	studentsDictionary = map(extractIntoDictionaries,students)
	phoneBook = map(lambda ascci: chr(ascci),range(65,91))
	result = {}
	for i in range(0,26):
		result[phoneBook[i]] = filter(lambda student:student['name'][0]==phoneBook[i],studentsDictionary)
	return result

def averageOf(students,subject):
	studentsDictionary = map(extractIntoDictionaries,students)
	studentsDictionary = filter(lambda x:x[subject]!='DNA',studentsDictionary)
	result = reduce(lambda score1,score2:{subject:int(score1[subject])+int(score2[subject])},studentsDictionary)
	total = float(result[subject])
	return round(total/len(studentsDictionary));

def between(students,subject,lowerLimit,upperLimit):
	studentsDictionary = map(extractIntoDictionaries,students)
	studentsDictionary = filter(lambda x:x[subject]!='DNA',studentsDictionary)
	result = filter(lambda x:upperLimit>=int(x[subject])>=lowerLimit,studentsDictionary)
	return result;
