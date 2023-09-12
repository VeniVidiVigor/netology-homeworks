import os


def rewrite_file(path):
    data = {}
    x = (os.listdir(path))
    for file in x:
        if file.endswith('.txt'):
            with open(file, encoding='utf-8') as f:
                file_data = f.readlines()
                data[len(file_data)] = (file, ' '.join(file_data))
    data = dict(sorted(data.items()))
    with open('result_data.txt', 'w', encoding='utf-8') as new_f:
        for key, value in data.items():
            new_f.write(f'{value[0]} \n')
            new_f.write(f'{key} \n')
            new_f.write(f'{value[1]}\n\n')


rewrite_file(os.getcwd())
