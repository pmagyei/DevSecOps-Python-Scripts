from survey import AnonymousSurvey as AnSu

question = "What language did you first learn to speak"
language_survey = AnSu(question)

language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == "q":
        break
    language_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()