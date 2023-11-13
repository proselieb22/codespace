def camel_to_snake_case(variable_name):
    snake_case_name = ""
    for char in variable_name:
        if char.isupper():
            snake_case_name += "_" + char.lower()
        else:
            snake_case_name += char
    if snake_case_name[0] == "_":
        snake_case_name = snake_case_name[1:]
    return snake_case_name

def main():
    camel_case_var = input("Enter a variable name in camel case: ")
    snake_case_var = camel_to_snake_case(camel_case_var)
    print(f"The variable name in snake case is: {snake_case_var}")

if __name__ == "__main__":
    main()
