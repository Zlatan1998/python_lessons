quality_human_resource = float(input("Enter the value of quality human resouce:  "))
natural_resources = float(input("Enter the value of natural resources:  "))
quality_economic_management_team = float(input("Enter the value of quality economic management team:  "))
general_populace_work_ethics = float(input("Enter the value of general populace work ethics:  "))
country_economic_success = float(input((quality_human_resource + natural_resources + quality_economic_management_team) * general_populace_work_ethics))
print(country_economic_success)
