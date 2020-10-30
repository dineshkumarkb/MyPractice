import csv,os
import pytest


@pytest.mark.read
def test_file():

    my_path = r'C:\Users\212757215\Desktop\New folder'
    read_files = os.listdir(my_path)
    for i in read_files:
        assert i.endswith('csv')
        # if i.endswith('csv'):
        #     print("Right file")
        # else:
        #     print("Wrong file")



test_file()