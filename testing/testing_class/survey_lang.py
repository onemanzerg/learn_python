from survey import AnonymousSurvey

question = "Какой язык программирования для вас наиболее интересен?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Нажмите 'Q' для выхода из опроса")
while True:
    response = input("Language: ")
    if response == 'Q':
        break
    my_survey.store_response(response)

print("Спасибо за ответ")

my_survey.show_results()