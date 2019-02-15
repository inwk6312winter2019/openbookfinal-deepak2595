mybook=open("book1.txt","r")
def unique_words(mybook):
#	mybook = open('Book1.txt',"r")
	li=[]
#	i=0
	for line in mybook:
		line=line.strip()
		line=line.split()
		if word not in li:
			li.append(word)
			
        #                
	#	else:
			li(word)+=1
#	                i=i+1
	       # i=i+1
        print(li)
unique_words(mybook)

#unique_words

def count_the_article(mybook):
#	mynote = open('book2.txt')
        count=0
	for line in mybook:
		line =line.split()
		for word in line:
			count+=1
        print(count)
count_the _article(mybook)

#countwords 	

def sorted_words(mybook):
  output=[]
  list2=[]
  for line in mybook:
    line=line.strip()
    line=line.split()
    for word in line:
      if word not in output:
        output.append(word)
  print(sorted(output[::-1], key = len))
sorted_words(mybook)
    
#sortedwords
def character_word_count(mybook)
    mydict={}
    for line in mybook:
      line=line.strip()
      line=line.split()
      for word in line:
        if word not in mydict:
		mydict[word]=1
        else:
	        mydict[word]+=1
	print(mydict)

chracter_word_count(mybook)
#counting chracters

def starts_with_vow(mybook)
    li1=[]
    tup = ("a", "e", "i", "o", "u")
    for line in mybook:
	line=line.strip()
        line=line.split()
          if word[0] in tup:
             li.append(word)
starts_with_vow(mybook)

#vowels word  
 
