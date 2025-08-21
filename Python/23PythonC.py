http_status_codes = {
    200: "OK",
    404: "Not Found"
}

def main():
    print("--- Interactive HTTP Status Code Lookup ---")
    print("Enter a status code to find its meaning, or type 'quit' to exit.")

    while True:
        user_input = input("\nEnter a status code: ").strip().lower()

        if user_input in ["q", "quit", "exit"]:
            print("Goodbye!")
            break

        try:
            code = int(user_input)
            meaning = http_status_codes.get(code, "Sorry, that code is not in our dictionary.")
            print(f"-> The meaning of {code} is: {meaning}")
        except ValueError:
            print("! Invalid input. Please enter a number for the status code.")

if __name__ == "__main__":
    main()