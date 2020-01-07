import os
import sys


class TextEditor:
    def __init__(self):
        print('*****     TEXT EDITOR     *****')
        print('\n\t1. Create a new Text File.')
        print('\n\t2. Append a Text File.')
        print('\n\t3. Read from a Text File.')
        print('\n\t4. Delete a Text File.')
        print('\n\t0. Exit.')

        while True:
            choice = 0
            try:
                choice = int(input('\n\nEnter your choice: '))
            except ValueError:
                print('Only numbers 0 - 4 is allowed.')
                continue
            except KeyboardInterrupt:
                sys.exit(0)
            except FileNotFoundError:
                os.mkdir('text')
            if not 0 <= choice < 5:
                print('Only numbers 0 - 4 is allowed.')
            else:
                print(choice)

            if choice == 0:
                sys.exit(0)

            fname = input('\nEnter the name of the file without extension: ')
            fname = 'text/' + fname + '.txt'
            print(fname)

            if choice == 1:
                self.create(fname)
            elif choice == 2:
                self.append(fname)
            elif choice == 3:
                self.read(fname)
            elif choice == 4:
                self.delete(fname)

    def create(self, fname):
        file = self.open_file(fname, 'w')
        while True:
            data = input("Enter a sentence (type '@exit' to close file): ")
            if data == '@exit':
                break
            data = data + '\n'
            file.write(data)
        file.close()

    def append(self, fname):
        file = self.open_file(fname, 'a')
        while True:
            data = input("Enter a sentence (type '@exit' to close file): ")
            if data == '@exit':
                break
            data = data + '\n'
            file.write(data)
        file.close()

    def read(self, fname):
        file = self.open_file(fname, 'r')
        for _ in file:
            print(_)
        file.close()

    @staticmethod
    def delete(fname):
        os.remove(fname)

    @staticmethod
    def open_file(fname, ftype):
        try:
            file = open(fname, ftype)
        except FileNotFoundError:
            os.mkdir('text')
            file = open(fname, ftype)
        return file


if __name__ == '__main__':
    TextEditor()
