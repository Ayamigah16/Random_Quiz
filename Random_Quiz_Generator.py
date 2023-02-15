#! python3.11
#Random_Quiz_Generator - Creates quizzes with questions and answers in random order, along with the answer key

import random

#The quiz data. Keys are Africa Countries and values are their capitals

capitals = {'Ghana': 'Accra','Algeria':'Algiers', 'Benin':'Porto Novo','Bostwana':'Garborone','Angolo':'Luanda',
            'Burundi':'Bujumbura','Burkina Faso':'Ouagadougou','Cameroon':'Yaounde','Cape Verde':'Praia',
            'Central Afriaca Republic':'Bangui','Chad':"N'Djamena",'Comoros':'Moroni','Egypt':'Cairo',
            'Equatorial Guinea':'Malabo','Eritrea': 'Asmara','Eswatini':'Mbabane','Ethiopia':'Addis Ababa',
            'Gambia':'Banjul','Gabon':'Libreville','Guinea':'Conakry','Guinea-Bissau':'Bissau','Kenya':'Nairbi',
            'Ivory Coast':'Yamoussoukro','Lesotho':'Maseru','Liberia':'Monrovia','Lybia':'Tripoli','Madagascar':'Antananarivo',
            'Malawi':'Lilongwe','Mali':'Bamako','Mauritania':'Nouakchott','Mauritius':'Port Louis','Morocco':'Rabat',
            'Mozambique':'Maputo','Namibia':'Windhoek','Niger':'Niamey','Nigeria':'Abuja','Republic of the Congo':'Brazzaville',
            'Rwanda':'Kigali','Senegal':'Dakar','Seychelles':'Victoria','Sierra Leone':'Freetown','Somalia':'Mogadishu',
            'South Africa':'Pretoria','South Sudan':'Juba','Sudan':'Khartoum','Tanzania':'Dodoma','Togo':'Lome',
            'Tunisia':'Tunis','Uganda':'Kampala','Zambia':'Lusaka','Zimbabwe':'Harare'}
        
#Generating 20 quiz files:
for quizNum in range(20):
    #Create the quiz and answer key files
    quizFile = open('capitalsquiz%s.txt' %(quizNum+1),'w')      # %s => %(quizNum+1)
    answerKeyFile =open('capitalsquiz_answers%s.txt' %(quizNum+1),'w')

    #Writing out the header for the quiz:
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (From %s)' %(quizNum+1))
    quizFile.write('\n\n')

    #shuffling the countries
    countries = list(capitals.keys())
    random.shuffle(countries)

    #Creating the Answer Options ( Both right and Wrong answers)
    #Looping through all countries
    for questionNum in range(len(countries)-1):

        #Getting right and wrong answers
        correctAnswer = capitals[countries[questionNum]]         #correct answer stored
        wrongAnswers = list(capitals.values())                  #wrong answers stored
        del wrongAnswers[wrongAnswers.index(correctAnswer)]     #removing right answer from wrong answers
        wrongAnswers = random.sample(wrongAnswers,3)            #obtaining 3 sample wrong answers                        
        answerOptions = wrongAnswers + [correctAnswer]           # 4 possible answers 
        random.shuffle(answerOptions)                           #shuffling answer options


        #writing quetions and answers to the quiz file
        quizFile.write('%s. What is the capital of %s?\n' %(questionNum+1,countries[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' %('ABCD'[i], answerOptions[i]))                         
        quizFile.write('\n')    

        #writing the answer key to a file
        answerKeyFile.write('%s. %s\n' %(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))       # 'ABCD' is a string array with its index ffor selection 
    quizFile.close()
    answerKeyFile.close()

                                 
                                 
