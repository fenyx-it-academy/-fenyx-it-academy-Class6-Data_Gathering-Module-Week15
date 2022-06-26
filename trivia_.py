import requests
import json

class Trivia():

    def __init__(self):
        self.api_url="https://the-trivia-api.com/api/"

    def get_all_questions(self):
        response = requests.get(self.api_url + "questions")
        return response.json()

    def get_categories(self):
        response = requests.get(self.api_url + "categories")
        return response.json()

    def get_history(self):
        response = requests.get(self.api_url + "questions?categories=history&limit=5&difficulty=hard")
        return response.json()

    def get_science(self):
        response = requests.get(self.api_url + "questions?categories=history,science&limit=5&difficulty=medium")
        return response.json()

    def get_film_and_tv(self):
        response = requests.get(self.api_url + "questions?categories=history,science,film_and_tv&limit=5&difficulty=easy")
        return response.json()

    def create_topic(self):
        response = requests.get(self.api_url + f"questions?categories={category}&limit={limit}&difficulty={difficulty}")
        return response.json()


trivia = Trivia()

while True:

    choice = int(input("""
    1 - Categories
    2 - History
    3 - Science
    4 - Film and Tv
    5 - Create a Topic
    6 - Exit
    Please enter a number from 1 to 6 : """))

    if choice == 6:
        break
       

    else:  
        if choice == 1:
           print(trivia.get_categories().keys())  

        elif choice == 2:
            result= trivia.get_history()
            a=1
            for i in result:
                print("Question {}: ".format(a) + i["question"])
                print("A)" + i["correctAnswer"])
                print("B)" + i["incorrectAnswers"][0])
                print("C)" + i["incorrectAnswers"][1])
                print("D)" + i["incorrectAnswers"][2])
                a+=1
                print("#####################TRIVIA###################")
        elif choice == 3:
            result= trivia.get_science()
            a=1
            for i in result:
                print("Question {}: ".format(a) + i["question"])
                print("A)" + i["correctAnswer"])
                print("B)" + i["incorrectAnswers"][0])
                print("C)" + i["incorrectAnswers"][1])
                print("D)" + i["incorrectAnswers"][2])
                a+=1
                print("#####################TRIVIA###################")

        elif choice == 4:
            result= trivia.get_film_and_tv()
            a=1
            for i in result:
                print("Question {}: ".format(a) + i["question"])
                print("A)" + i["correctAnswer"])
                print("B)" + i["incorrectAnswers"][0])
                print("C)" + i["incorrectAnswers"][1])
                print("D)" + i["incorrectAnswers"][2])
                a+=1
                print("#####################TRIVIA###################")

        elif choice == 5:
            category = input("Please enter one of the following categories\n* arts_and_literature\n* film_and_tv\n* food_and_drink\n* general_knowledge\n* geography\n* history\n* music\n* science\n* society_and_culture\n* sport_and_leisure): ")
            limit = int(input("Please enter a limit (1-20): "))
            difficulty = input("Please enter a difficulty level (easy,medium,hard): ")
            counter = 0
            while counter < limit:
                result = trivia.create_topic()[counter]
                counter += 1
                print(f"Question {counter}: {result['question']}\nA) {result['correctAnswer']}\nB) {result['incorrectAnswers'][0]}\nC) {result['incorrectAnswers'][1]}\nD) {result['incorrectAnswers'][2]}")
                print("################TRIVIA################")
            
        else:
            print('Your choice is wrong! Please try a valid number!')


