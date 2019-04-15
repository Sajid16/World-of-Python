fw = open('sample.txt','w')
fw.write("what are you doing here?\nI was going to you.\nWhatever, How are you?")
fw.close()


fr = open('sample.txt' , 'r')
save = fr.read()
print(save)
fr.close()