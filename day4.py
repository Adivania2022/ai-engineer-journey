pain_scores = []

continue_program = "yes"

while continue_program == "yes":
    score = int(input("Pain level (0–10): "))
    pain_scores.append(score)

    continue_program = input("Add another score? (yes/no): ").lower()

if len(pain_scores) > 0:
    total = sum(pain_scores)
    average = total / len(pain_scores)
    print("Average pain score:", average)
else:
    print("No scores were entere