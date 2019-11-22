import sys
sys.path.append("..")
from test.sruvey import AnonymoousSurvery
question ="what language did you first learn to speak?"
my_survey=AnonymoousSurvery(question)
my_survey.show_question()
print("Enter q  at any time to quit.\n")
while True:
    response =input("language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
print("\n Thank you to everyone who participated in the survey!")
my_survey.show_results()