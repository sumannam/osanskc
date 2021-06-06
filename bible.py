import os

bible_path = "E:\\OneDrive\\1. 예배\\bible\\"

long_bible = "시편 18:1-19"
short_bible = "시18:1-19"

long_book = long_bible.split(' ')[0]
address = long_bible.split(' ')[1]
start_book = short_bible.split('-')[0]
end_book = start_book.split(':')[0] + ":" + short_bible.split('-')[1]

# print(end_book)

def extractBook(name):
    file_list = os.listdir(bible_path)

    for file in file_list:
        if( file.find(name) > 0 ):
            return file
    
    return "No Book!!!"


target_book = extractBook(long_book)

# print(start_book)

target_book_file = bible_path + target_book
# print(target_book_file)

versers = open(target_book_file, 'r' )

print_verse = False

while True:
    verse = versers.readline()
    chapter_verse = verse.split(' ')[0]

    if(chapter_verse == start_book):
        print_verse = True

    if(print_verse == True):
        print(verse)

    if(chapter_verse == end_book):
        print_verse = False
    
    if not verse:
        break
    

versers.close()

#print(target_book_path)
#print(address)

#print(file_list)
