continue_program = "yes"

total_valid = 0
severe_count = 0
moderate_count = 0
mild_count = 0

while continue_program == "yes":
    pain_score = int(input("Pain level (0–10): "))

    if pain_score < 0 or pain_score > 10:
        print("Invalid pain score. Not counted.")

    else:
        # This is a valid patient entry
        total_valid += 1

        if pain_score >= 8:
            print("Severe pain.")
            severe_count += 1

        elif pain_score >= 4:
            print("Moderate pain.")
            moderate_count += 1

        else:
            print("Mild or no pain.")
            mild_count +=1

    continue_program = input("Evaluate another patient? (yes/no): ").lower()

print("\n=== Summary ===")
print("Total valid patients evaluated:", total_valid)
print("Severe cases (>= 8):", severe_count)
print("Moderate cases (4–7):", moderate_count)
print("Mild cases:", mild_count)
print("Program ended.")



