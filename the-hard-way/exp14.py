from sys import argv

script, user_name = argv
prompt = '$ '

print(f"Hi {user_name} i am the {script} program")
print("I would like to ask you a few questions")
print(f"Do you like me {user_name} ?")
likes = input(prompt)

print(f"Where do you live {user_name} ?")
lives = input(prompt)

print(f"What kind of computer do you have ?")
computer = input(prompt)

print(f"""
You said {likes} about liking me.
You like in {lives} and have a {computer} computer
""")
