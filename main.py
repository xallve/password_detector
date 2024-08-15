import re


def is_password_valid(requirement, password):
    """
    Split requirements into char and range
    E.g. "a 1-5" -> "a" "1" "5" -> "a" 1 5
    """
    match = re.match(r'(\w)\s(\d+)-(\d+)', requirement)
    if not match:
        return False
    char, min_count, max_count = match.groups()
    min_count, max_count = int(min_count), int(max_count)

    # Count number of detected chars in password
    char_count = password.count(char)

    # Check if number of chars is in range
    return min_count <= char_count <= max_count


def find_valid_passwords(file_path):
    valid_passwords = []

    # Read file by lines
    with open(file_path, 'r') as file:
        for line in file:
            requirement, password = line.split(': ')
            if is_password_valid(requirement, password.strip()):
                valid_passwords.append(line.strip())

    return valid_passwords


if __name__ == "__main__":
    file_path = 'passwords.txt'
    valid_passwords = find_valid_passwords(file_path)
    print(f'Number of valid passwords: {len(valid_passwords)}')
    print('Valid passwords:')
    for valid_password in valid_passwords:
        print(valid_password)
