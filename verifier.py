import re

# Regular expression for phone number validation
phone_regex = re.compile(r'^\+?[0-9]{10,12}$')

# Prompt user for input file
input_path = input('Enter the path to the input file: ')

# Open input file
try:
    with open(input_path, 'r') as input_file:
        # Create output file
        output_path = 'output.txt'
        with open(output_path, 'w') as output_file:
            # Iterate over each phone number in the input file
            for phone_number in input_file:
                phone_number = phone_number.strip()

                # Validate phone number
                if phone_regex.match(phone_number):
                    # Write validated phone number to output file
                    output_file.write(phone_number + '\n')

        print(f'Phone number verification complete. Valid numbers written to output file: {output_path}')

except IOError as e:
    print(f'Error opening file: {e}')
