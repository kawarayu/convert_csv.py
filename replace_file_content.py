import os
import fileinput


def main():
    path = r'path_to'
    filename_condtion = ''
    replace_from = ''
    replace_to = ''


    for file in os.listdir(path):
        if filename_condtion in file:
            full_path = os.path.join(path, file)
            write_path = os.path.join(path, file + '_tmp')

            with open(full_path, encoding='utf-8') as f:
                with open(write_path, mode='w', encoding='utf-8') as wf:
                    for line in f:
                        wf.writelines(line.replace(replace_from, replace_to))

            os.remove(full_path)
            os.rename(write_path, full_path)
            print(full_path, 'processed.')

    print('finished...')

if __name__ == '__main__':
    main()