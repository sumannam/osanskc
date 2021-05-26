# -*- coding: cp949 -*- 

# 개역개정
bible1 = open("D:\\git\\osanskc\\genesis\\bible1.txt", 'r', encoding='UTF8')
# 쉬운성경
bible2 = open("D:\\git\\osanskc\\genesis\\bible2.txt", 'r', encoding='UTF8')
# 현대인의 성경
bible3 = open("D:\\git\\osanskc\\genesis\\bible3.txt", 'r', encoding='UTF8')
# NLT
bible4 = open("D:\\git\\osanskc\\genesis\\bible4.txt", 'r', encoding='UTF8')

bible_merge = open("D:\\git\\osanskc\\genesis\\bible_merge.txt", 'w', encoding='UTF8')

while True:
    line1 = bible1.readline()
    line2 = bible2.readline()
    line3 = bible3.readline()
    line4 = bible4.readline()

    if not line1:
        break
    if not line2:
        break
    if not line3:
        break
    if not line4:
        break

    verse = "(" + line1[0:2] + "절)\n";
    verse = verse.replace(" ", "")
    
    bible_merge.write(verse)
    bible_merge.write(line1[3:])
    bible_merge.write(line2[3:])
    bible_merge.write(line3[3:])
    bible_merge.write(line4[3:])
    bible_merge.write("\n")
    # print(verse)
    # print(line1[3:])
    # print(line2[3:])
    # print(line3[3:])
    # print(line4[3:])
    
bible1.close()
bible2.close()
bible3.close()
bible4.close()
bible_merge.close()