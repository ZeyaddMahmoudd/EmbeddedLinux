import os

#to access specific enviroment variable
variable_name = "my_variable"
variable_value = os.environ.get(variable_name)
print(f"the value of {variable_name} is: {variable_value}")

#to access all enviroment variables
all_variables = os.environ
print("All enviroment variables:")
for variable_name, variable_value in all_variables.items():
 print(f"{variable_name} = {variable_value}")