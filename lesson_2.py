with open('test.txt', 'r') as f:
    while True:
       line = f.readline()
       print(line)
       #print文endに何も指定しなければ/nが入る
       if not line:
           break 