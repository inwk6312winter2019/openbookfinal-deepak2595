import operator 
b1= open (book1.txt,"r")
b2= open(book2.txt, "r")
b3= open(book3.txt. "r")

def common_words(b):
	for line in b1:
                pydict={}
		line=line.strip()
		line=line.split(",")
		
		if word not in pydict:
			pydict[word]=1
		else:
			pydict[word]+=1
	 x = (sorted (pydict.items(),key=operator.itemgetter(0),reverse)
        for freq,word in x[:20]:
		print(word,freq,sep='\t')
	for char in x[:20]:
		com_dict[char]=com_dict.get(char,0)+1
	print("\n " "mostcommon word in book1")
	print(com_dict)
        for line in b2:
                 py2dict={}
                 line=line.strip()
                 line=line.split(",")
                 if word not in  py2dict:
                         py2dict[word]=1
                 else:
                         py2dict[word]+=1
         y = (sorted (py2dict.items(),key=operator.itemgetter(0),reverse)
        for freq,word in y[:20]:
		print(word,freq,sep='\t')
	for char in y[:20]:
		com_dict[char]=com_dict.get(char,0)+1
	print("\n" "most common words in book2")
	print(com_dict)
        for line in b2:
                 py3dict={}
                 line=line.strip()
                 line=line.split(",")
                 if word not in  py3dict:
                         py2dict[word]=1
                 else:
                         py2dict[word]+=1
         z = (sorted (py3dict.items(),key=operator.itemgetter(0),reverse)
        for freq,word in z[:20]:
		print(word,freq,sep='\t')
	for char in z[:20]:
		com_dict[char]=com_dict.get(char,0)+1
	print("\n" "mostcommon word in book3")
	print(com_dict) 
        #i=0
        #j=0



common_words(b1)
common_words(b2)
common_words(b3)
