from parser import parse_expression  # Import the new function

def main():
    global temp_count  # Keep temp_count global if needed across runs
    while True:
        try:
            # Get the input expression
            s = input("Enter an arithmetic expression (or 'quit' to exit): ")
            if s.lower() == 'quit':
                break

            # Reset temp count for each new expression to ensure unique temporary variables
            temp_count = 0

            # Parse the expression and get intermediate code
            intermediate_code = parse_expression(s)

            # Print the generated intermediate code
            print("Intermediate Code:")
            for code in intermediate_code:
                print(code)
            print()  # Newline for better readability

        except EOFError:
            break

if __name__ == "__main__":
    main()
