from translator import MorseCodeTranslator


def main():
    """
    Main function to run the Morse code translator program.
    """
    translator = MorseCodeTranslator()

    print(
        "Hello! Enter a phrase using English letters and/or numbers, and i'll convert it to Morse Code!"
    )

    try:
        while True:
            user_input = input("User Input (esc to quit): ")

            # Check for Escape key (ASCII 27)
            if user_input == chr(27):
                print("Exiting...")
                break

            # Translate and print
            try:
                print(f"Translation: {translator.translate(user_input)}")
            except ValueError as e:
                print(e)

    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
