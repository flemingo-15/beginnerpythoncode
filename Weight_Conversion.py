def main():
  uncalc_weight = input("Enter Weight Here: ")
  org_meas = input("Weight given in (K)g or (L)bs: ")
  
  while org_meas.lower() != "k" and org_meas.lower() != "l":
    input("Please enter valid input: ")
    org_meas = input()
  if org_meas.lower() == "k":
    final_meas = (float(uncalc_weight)*2.2)
    print("Weight in Pounds: " + str(final_meas))
  else:
    final_meas = (float(uncalc_weight)*0.45)
    print("Weight in Kilograms: " + str(final_meas))

  run_again = input("Would you like to input another value? (Y or N) ")

  while run_again.lower() != "y" and run_again.lower() != "n":
    input("Please enter valid input: ")
    run_again = input()
  if run_again == "y":
    main()
  else:
    print("We hope to see you again soon!")
    raise SystemExit
main()
