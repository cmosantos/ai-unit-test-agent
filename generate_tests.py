from agent import generate_tests

with open("functions.py", "r") as file:
    code = file.read()

tests = generate_tests(code)

with open("test_functions.py", "w") as file:
    file.write(tests)

print("Test file generated successfully: test_functions.py")
