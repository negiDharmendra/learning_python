import	unittest
from studentQueries import *
from students import *

class studentQueries(unittest.TestCase):
	def testHighestCanRetrieveStudentWithHighestScoreInMathematics(self):
		actualStudent= highest(students,"mathematics");
		self.assertEqual(actualStudent['name'],"Dharmendra Singh");
		self.assertEqual(actualStudent['roll_num'],'1001');
		self.assertEqual(actualStudent['mathematics'],'97');

	def testHighestCanRetrieveStudentWithHighestScoreInEnglish(self):
		actualStudent= highest(students,"english");
		self.assertEqual(actualStudent['name'],"Jai Om Pandey");
		self.assertEqual(actualStudent['roll_num'],'1009');
		self.assertEqual(actualStudent['english'],'98');

	def testHighestCanRetrieveStudentWithHighestScoreInScience(self):
		actualStudent= highest(students,"computer_science");
		self.assertEqual(actualStudent['name'],"Jai Om Pandey");
		self.assertEqual(actualStudent['roll_num'],'1009');
		self.assertEqual(actualStudent['computer_science'],'98');

	def testLowestCanRetrieveStudentWithHighestScoreInMathematics(self):
		actualStudent= lowest(students,"mathematics");
		self.assertEqual(actualStudent['name'],"Ganesh Patil");
		self.assertEqual(actualStudent['roll_num'],'1045');
		self.assertEqual(actualStudent['mathematics'],'0');

	def testLowestCanRetrieveStudentWithHighestScoreInEnglish(self):
		actualStudent= lowest(students,"english");
		self.assertEqual(actualStudent['name'],"Suman Das");
		self.assertEqual(actualStudent['roll_num'],'1030');
		self.assertEqual(actualStudent['english'],'4');
		
	def testLowestCanRetrieveStudentWithHighestScoreInScience(self):
		actualStudent= lowest(students,"computer_science");
		self.assertEqual(actualStudent['name'],"Supriya Gole");
		self.assertEqual(actualStudent['roll_num'],'1014');
		self.assertEqual(actualStudent['computer_science'],'0');

	def testAboveCanRetrieveStudensAboveACertainScoreInMathematics(self):
		actualStudents = above(students,"mathematics",90);
		expectedNames = ["Adarsh Kumar Sandilya","Anusree Prakash","Dharmendra Singh",
		"Saranraj Sekar"];
		actualNames = map(lambda a:a['name'],actualStudents);
		actualNames.sort()
		self.assertEqual(actualNames,expectedNames);

	def testAboveCanRetrieveStudensAboveACertainScoreInEnglish(self):
		actualStudents = above(students,"english",90);
		expectedNames = ["Jai Om Pandey","Sagar Maurya","Saranraj Sekar"];
		actualNames = map(lambda a:a['name'],actualStudents);
		actualNames.sort()
		self.assertEqual(actualNames,expectedNames);

	def testAboveCanRetrieveStudensAboveACertainScoreInScience(self):
		actualStudents = above(students,"computer_science",90);
		expectedNames = ["Arindam Karmakar","Ashwin Kumar KA","Jai Om Pandey",
			"Mitesh Kumar Jha","Sayan Bisui"];
		actualNames = map(lambda a:a['name'],actualStudents);
		actualNames.sort()
		self.assertEqual(actualNames,expectedNames);


	def testBelowCanRetrieveStudensBelowACertainScoreInMathematics(self):
		actualStudents = below(students,"mathematics",5);
		expectedNames = ["Ashwin Kumar KA","Bindu S","Ganesh Patil","Nimesh P"];
		actualNames = map(lambda a:a['name'],actualStudents);
		actualNames.sort()
		self.assertEqual(actualNames,expectedNames);

	def testBelowCanRetrieveStudensBelowACertainScoreInEnglish(self):
		actualStudents = below(students,"english",10);
		expectedNames = ["Gaurav K","Prasun Kumar Palchodhary","Suman Das"];
		actualNames = map(lambda a:a['name'],actualStudents);
		actualNames.sort()
		self.assertEqual(actualNames,expectedNames);

	def testBelowCanRetrieveStudensBelowACertainScoreInScience(self):
		actualStudents = below(students,"computer_science",10);
		expectedNames = ["Abhishek Gupta","Rahul Nandi","Saranraj Sekar","Suman Maity",
		"Supriya Gole","Surajit Chongder"];
		actualNames = map(lambda a:a['name'],actualStudents);
		actualNames.sort()
		self.assertEqual(actualNames,expectedNames);

	def testPhonBookProvidesAnAlphabeticalBreakdownOfStudents(self):
		studentPhoneBook = phoneBook(students);
		self.assertEqual(2,len(studentPhoneBook["B"]));
		self.assertEqual(16,len(studentPhoneBook["S"]));

		namesThatBeginWithB = map(lambda s:s['name'],studentPhoneBook["B"])
		namesThatBeginWithB.sort()
		self.assertEqual(["Bindu S","Brindaban Patra"],namesThatBeginWithB);

	def testAverageOfProvidesTheAverageForMathematicsScores(self):
		actualMathematicsAverage = averageOf(students,"mathematics");
		self.assertEqual(50,actualMathematicsAverage);

	def testAverageOfProvidesTheAverageForComputerScienceScores(self):
		actualComputerScienceAverage = averageOf(students,"computer_science");
		self.assertEqual(52,actualComputerScienceAverage);

	def testAverageOfProvidesTheAverageForEnglishScores(self):
		actualMathematicsAverage = averageOf(students,"english");
		self.assertEqual(52,actualMathematicsAverage);

	def testBetweenFetchesStudentsWhoseMathsScoresLieWithinARange(self):
		actualStudents= between(students,"mathematics",10,20)
		expectedNames=['Anjaly Joy','Arindam Karmakar','Jai Om Pandey','Madhuri Patil', 
		'Rahul Nandi','Sagar Maurya','Sayan Bisui' ];
		actualNames=map(lambda a:a['name'],actualStudents)
	
		self.assertEqual(7,len(actualStudents));
		self.assertEqual(expectedNames,actualNames)

if __name__ == '__main__':
    unittest.main()