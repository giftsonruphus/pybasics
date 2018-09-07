import json
import pickle

running = True
user_input_list = []

while running:
    print('Please choose')
    print('1: Add input')
    print('2: Output data')
    print('q: Quit')
    user_input = input('Your Choice: ')
    if user_input == '1':
        data_to_store = input('Your text: ')
        user_input_list.append(data_to_store)
        with open('assignment.p', mode='wb') as f:
            # f.write(json.dumps(user_input_list))
            f.write(pickle.dumps(user_input_list))
    elif user_input == '2':
        with open('assignment.p', mode='rb') as f:
            file_content = pickle.loads(f.read())
            for line in file_content:
                print(line)
    elif user_input == 'q':
        running = False
