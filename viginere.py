def viginere(plain_text, key):

    # ubah plain text ke lowercase dan buang semua spasi
    plain_text = plain_text.lower().replace(" ","")
    
    # ubah key menjadi lowercase
    key = key.lower()# ubah key menjadi lowercase
    
    digest = ""
    
    count = 0
    for text in plain_text: # loop sebanyak huruf plain textnya
        # print(text, ord(text)-96, ord(key[count])-96 , chr(ord(key[count])-96) )
        
        # ubah setiap huruf dalam range 0 - 26, dijumlahkan,
        # kembalikan kembali ke range 0 - 26
        # kemudian ubah ke dalam range 97 - 122 (ASCII) 
        digest+=chr( ((ord(text)-96) + (ord(key[count])-96))%26 + 96 ) 
        count+=1
        if(count == 5):
            count = 0
    
    print(digest)


plain_text = input()
key = input()

viginere(plain_text, key)