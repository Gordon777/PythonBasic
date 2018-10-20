try:
    file=open('IEEE.txt','r+') #會報錯的代碼
except Exception as e: #將報錯存在e中
    print(e)
    response = input('do you want to create a new file:')
    if response=='y':
        file=open('IEEE.txt','w')
    else:
        pass
else:
    file.write('hihihihihihihi~~~~')
    file.close()
