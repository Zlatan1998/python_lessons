goal_keeper = float(input("Enter the value of goal_keeper:  "))
defenders = float(input("Enter the value of defenders:  "))
midfielders = float(input("Enter the value of midfielders:  "))
attackers = float(input("Enter the value of attackers:  "))
manager = float(input("Enter the value of manager:  "))
owners_financial_commitment = float(input("Enter the value of owners_financial_commitment:  "))
football_team_success = (goal_keeper + defenders + midfielders + attackers + manager) * owners_financial_commitment
print(football_team_success)