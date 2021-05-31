import time
try:
    f = open('test.txt', 'r')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        print('interrupt')
    finally:
        f.close()
        print('close file')
except:
    print('have no files')
