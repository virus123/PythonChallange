# PythonChallange
This is my attempt to solve the puzzel that is on http://www.pythonchallenge.com/


Level 0:
 The level 0 has me do 2^38 which is as python tell me 274877906944
 put that in url i get www.pythonchallenge.com/pc/def/274877906944.html
 
 which redirects to : www.pythonchallenge.com/pc/def/map.html
 
 Level 1:
  The level 1 has one pic nothing else
  which reads
  K -->M
  O -->Q
  E --> G
  
  so basically this seems simple cryptography and here each of the latter is 2 step ahead so
  I.E. A becomes C
  
  so
  well i think this is the level where coding begames
  
  i used  ``.maketrans`` to string to change latters
  and what i get is
  >i hope you didnt translate it by hand. thats what computers are for. doing itin by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
  
  so yeaa i guess i was right and now we have the ``map`` in url changin it we get ``ocr``
  
  Thus we get following url
  [http://www.pythonchallenge.com/pc/def/ocr.html](url)

    Level 2:
    hmm so hint reads :
    
    >recognize the characters. maybe they are in the book,
    but MAYBE they are in the page source.
    
    and as url suggest this must be ``Optical character recognition``
    
    so in url i found a large cluster string of special charcters 
    title on it reads 
    >find rare characters in the mess below
    
    hmm so this is gonna be tricky ``FUCK`` 
    well first of all i am gonna get this comment from source and get into programm
    yes so 
    this was easyier then i expected it to be.
    all i had to was find the char's that were repeating only once in that 99820 charcters string.
    
    Answer : Equality
    Thus we get following url
    [http://www.pythonchallenge.com/pc/def/equality.html](url)
    
 Level 3:
    there picture of candels and it reads
    >One small latter, surrounded by EXACTLY three big bodyguards on each of its sides
    
    so once agian there is a long strings of Characters in source code
    but thing about this string is that charcter's are small and capital alphabets and as hint suggest 
    it seems we are looking for one small latter surrounded by three capital latters on each side
    
    
       