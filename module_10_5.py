import datetime
import os
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r+') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break



if __name__ == '__main__':
    #directory of files
    path = os.getcwd()
    path_Folder_File = os.path.join(path,'Files')
    file_name = os.listdir(path_Folder_File)
    dir_file_name =[os.path.join(path_Folder_File, name) for name in file_name]
    #linear
    start = datetime.datetime.now()
    for name in dir_file_name:
        read_info(name)
    end = datetime.datetime.now()
    print('Time without multiprocessing: ', end-start)
    #multiprocessing
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info,dir_file_name)
        end = datetime.datetime.now()
    print('Time with multiprocessing: ', end - start)


