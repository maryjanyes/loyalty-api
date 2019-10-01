file_o = None

def open_file_and_log(message):
    with open('local_log.txt', 'a') as file:
        file_o = file
        file_o.write('\n' + message)

def clear_log_content():
    file_o = open('local_log.txt', 'w')
    file_o.truncate(0)