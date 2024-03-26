from advent.runner import register

@register(6, 2020, 1, True)
def custom_customs_1(split_text):
    questionaires = [{}]
    for line in split_text:
        if len(line) == 0:
            questionaires.append({})
        else:
            added_letters = set()
            for letter in line:
                if letter not in added_letters:
                    questionaires[-1][letter] = questionaires[-1].get(letter, 0) + 1

    question_count = 0
    for questionnaire in questionaires:
        question_count += len(questionnaire)
    
    return question_count

@register(6, 2020, 2, True)
def custom_customs_2(split_text):
    split_text.append("")
    questionaires = []
    this_questionaire = {}
    person_count = 0
    for line in split_text:
        if len(line) == 0:
            filled_questions = set()
            for key, value in this_questionaire.items():
                if value == person_count:
                    filled_questions.add(key)
            questionaires.append(filled_questions)
            this_questionaire = {}
            person_count = 0
        else:
            added_letters = set()
            for letter in line:
                if letter not in added_letters:
                    this_questionaire[letter] = this_questionaire.get(letter, 0) + 1
            person_count += 1

    question_count = 0
    for questionnaire in questionaires:
        question_count += len(questionnaire)
    
    return question_count