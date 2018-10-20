text='This is my first test.\nThis is the second line.\nThis the third line'
my_file=open('my file.txt','w')   #用法: open('文件名','形式'), 其中形式有'w':write;'r':read.
my_file.write(text)               #该语句会写入先前定义好的 text
my_file.close()                   #关闭文件