pain_score = int(input("On a scale from 0 to 10, what is your pain level? "))
if pain_score < 0 or pain_score > 10:
    print("Invalid pain score. Please enter a number between 0 and 10.")
if pain_score == 10:
    print("Emergency level pain. Immediate evaluation required.") 
else pain_score >= 8:
    print("High pain detected. Contact your doctor immediately.")
elif pain_score >= 4:
    print("Moderate pain. Monitor symptoms carefully.")
else:
    print("Pain level acceptable. Continue recovery plan.")

continue_program = "yes"
