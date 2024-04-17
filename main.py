import sys
from converter import FrenchConverter

def read_integers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            numbers = eval(data)
            if not isinstance(numbers, list):
                raise ValueError("Data in file is not in the expected list format")
            return numbers
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    

if __name__ == "__main__":
    file_path = 'input.txt'
    numbers = read_integers_from_file(file_path)
    if numbers:
        output_path = 'output.txt'
        converter = FrenchConverter()
        with open(output_path, 'w') as f:
            for num in numbers:
                f.write(converter.convert_to_french(num) + '\n')
                    