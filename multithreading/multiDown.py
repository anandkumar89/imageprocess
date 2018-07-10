import threading
import pandas as pd
import urllib
from queue import Queue

def download(downList, threadName):
    
    for index, row in downList.iterrows():
        if urllib.request.urlretrieve(row.File_Path, row.File_Name):
            status = "Success"
        else:
            status = "Failed"
        print(threadName + ": " + status + ': ' + row.File_Name);


def multi_down(fname):
    data = pd.read_csv(fname)
    source = data[['File_Name', 'File_Path']]
    
    threads = []
    batch_size = 200
    counter = 0
    datalen = len(source)
    Flag = True

    while(Flag):
        start = counter*batch_size
        end = min(datalen, start+200)
        print('Loop1: ' + str(counter))
        if end>=datalen:
            Flag = False

        downList = source[start:end]
        threadName = "thread"+str(counter)
        threads.append(threading.Thread(target=download, args = (downList,threadName)))
        counter = counter+1
        
    startCount = 0
    while(startCount<len(threads)):
        t = threads[startCount]
        t.start()
        print("loop2: " + str(startCount))
        startCount = startCount + 1

    endCount = 0
    while(endCount<len(threads)):
        t = threads[endCount]
        t.join()
        print("loop2: " + str(endCount))
        endCount = endCount + 1

    print('Done')
    

if __name__=="__main__":
    fname = 'Tommy-Data.csv'
    data = pd.read_csv(fname)
    source = data[['File_Name', 'File_Path']]
    q = Queue(maxsize=0)

    for index, row in source.iterrows():
        q.put((row.File_Name, row.File_Path))
    

    while not q.empty():
        name, path = q.get()
        if urllib.request.urlretrieve(path, name):
            print(name + ": " + path)
            print("success: " + name)
        q.task_done()




 
