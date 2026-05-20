print("--- BLOOD DONOR SCREENING SYSTEM ---")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
elif donor_age < 18 and donor_weight < 50:
    print("Result: NOT ELIGIBLE. Reason: Age < 18 and weight < 50 kg.")
elif donor_age < 18:
    print("Result: NOT ELIGIBLE. Reason: Age < 18.")
else:
    print("Result: NOT ELIGIBLE. Reason: Weight < 50 kg.")