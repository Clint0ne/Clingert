print("Ready? just 10 questions!")

countries = {
    "What is the capital of France?": "paris",
    "What is the capital of Germany?": "berlin",
    "What is the capital of Italy?": "rome",
    "What is the capital of Spain?": "madrid",
    "What is the capital of Portugal?": "lisbon",
    "What is the capital of Belguim?": "brussels",
    "What is the capital of Netherlands?": "amsterdam",
    "What is the capital of Greece?": "athens",
    "What is the capital of Switzerland?": "bern",
    "What is the capital of Austria?": "vienna",
}

for countries, correct_answer in countries.items():
    user_answer = input(countries + " ").strip().lower()
    if user_answer == correct_answer:
        print("Correct")
    else:
        print("Wrong. The correct answer is:", correct_answer.capitalize())
