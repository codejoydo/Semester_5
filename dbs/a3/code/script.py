import os

for i in range(1,10):
    os.system('python3 undo.py '+str(i)+' > ../log/'+str(i)+'.txt_undo')
for i in range(1,10):
    os.system('python3 redo.py '+str(i)+' > ../log/'+str(i)+'.txt_redo')
