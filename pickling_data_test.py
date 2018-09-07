while True:
    print("1. Write input to file:")
    print("2. Display contents to terminal")
    print("3. Write input to file using json")
    print("4. Write input to file using pickle")
    print("5. Load the file")
    print("q. Quit")
    switch = input("Enter your choice: ")

    if switch == "1":
        user_input = input("Tell me something baby:\n")
        with open('a6.txt', 'w') as fl:
            fl.write(user_input)
            fl.write("\n")
            
    elif switch == "2":
        with open('a6.txt', 'r') as fl:
            print(fl.read())
            
    elif switch == "3":
        import json

        user_input_list = []
        while True:
            user_input = input("Tell me something baby:\n")
            if user_input.lower() == 'exit':
                break
            else:
                user_input_list.append(user_input)
        with open('a6.txt', 'w') as fl:
            fl.write(json.dumps(user_input_list))

    elif switch == "4":
        import pickle
        user_input_list = []
        while True:
            user_input = input("Tell me something baby:\n")
            if user_input.lower() == 'exit':
                break
            else:
                user_input_list.append(user_input)
        with open('a6.txt', 'wb') as fl:
            fl.write(pickle.dumps(user_input_list))

    elif switch == "5":
        import pickle
        import json

        pickled_data = input("Enter true if data is pickled else enter anything else: ").lower()
        if pickled_data == 'true':
            with open('a6.txt', 'rb') as fl:
                file_contents = pickle.loads(fl.read())
        else:
            with open('a6.txt', 'r') as fl:
                file_contents = json.loads(fl.read())
        print(file_contents)

    elif switch.lower() == 'q':
        break