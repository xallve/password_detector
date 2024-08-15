import random
import string

"""
Generate 100 random passwords with requirements
"""
def generate_random_password(length):
    # Generate random password of given range
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def generate_password_with_requirement():
    # Choose randomly what char is required for password
    required_char = random.choice(string.ascii_lowercase)

    # Choose randomly what are min and max number of chars should be in password
    min_count = random.randint(1, 3)
    max_count = random.randint(min_count, min_count + 3)

    # Choose randomly password length
    password_length = random.randint(6, 12)

    # Generate password
    password = generate_random_password(password_length)

    # Randomly pass desired char couple of times
    password_list = list(password)
    for _ in range(random.randint(min_count, max_count)):
        # Вставляємо символ на випадкову позицію у паролі
        position = random.randint(0, len(password_list) - 1)
        password_list[position] = required_char

    # Collect password into string
    password = ''.join(password_list)

    # Generate requirement
    requirement = f'{required_char} {min_count}-{max_count}'

    return requirement, password


def generate_passwords_file(file_path, num_passwords):
    with open(file_path, 'w') as file:
        for _ in range(num_passwords):
            requirement, password = generate_password_with_requirement()
            file.write(f'{requirement}: {password}\n')


if __name__ == "__main__":
    file_path = 'passwords.txt'
    generate_passwords_file(file_path, 100)
    print(f'File "{file_path}" Generated.')