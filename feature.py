import os, json
import pandas as pd
import csv
import emoji

def find_file(basedir, filename):
    for dirname, dirs, files in os.walk(basedir):
        if filename in files:
            yield os.path.join(dirname, filename)
def find_folder(basedir, foldername):
    for dirname, dirs, files in os.walk(basedir):
        if foldername in dirs:
            yield dirname

def char_is_emoji(character):
	return character in emoji.UNICODE_EMOJI

def text_has_emoji(text):
	for character in text:
		if character in emoji.UNICODE_EMOJI:
			return 1

	return 0


csv_out = open('tweets_out.csv', mode='w')
writer = csv.writer(csv_out) 
fields = ['id','event', 'text', 'favorite_count', 'retweet_count', 'created_at','followers_count', 'friends_count', 'account_creation','verified'] #field names
writer.writerow(fields)
path_to_json = 'pheme-rumour-scheme-dataset/threads/en/charliehebdo'
for found in find_file(path_to_json, 'tweet.json'):
    data_json = open(found, mode='r').read()
    data = json.loads(data_json)
    writer.writerow([data.get('id'),
                     'charliehebdo',
                     data.get('text').encode('utf-8'), #unicode escape to fix emoji issue
                     data.get('favorite_count'),
                     data.get('retweet_count'),
		     data.get('created_at'),
		     data['user'].get('followers_count'),
		     data['user'].get('friends_count'),
		     data['user'].get('created_at'),
		     data['user'].get('verified')
		     ])	
		  
path_to_json = 'pheme-rumour-scheme-dataset/threads/en/ebola-essien'
for found in find_file(path_to_json, 'tweet.json'):
    data_json = open(found, mode='r').read()
    data = json.loads(data_json)
    writer.writerow([data.get('id'),
                     'ebola-essien',
                     data.get('text').encode('utf-8'), #unicode escape to fix emoji issue
                     data.get('favorite_count'),
                     data.get('retweet_count'),
		     data.get('created_at'),
		     data['user'].get('followers_count'),
		     data['user'].get('friends_count'),
		     data['user'].get('created_at'),
		     data['user'].get('verified')
		     ])	
		     	
path_to_json = 'pheme-rumour-scheme-dataset/threads/en/ferguson'
for found in find_file(path_to_json, 'tweet.json'):
    data_json = open(found, mode='r').read()
    data = json.loads(data_json)
    writer.writerow([data.get('id'),
                     'ferguson',
                     data.get('text').encode('utf-8'), #unicode escape to fix emoji issue
                     data.get('favorite_count'),
                     data.get('retweet_count'),
		     data.get('created_at'),
		     data['user'].get('followers_count'),
		     data['user'].get('friends_count'),
		     data['user'].get('created_at'),
		     data['user'].get('verified')
		     ])	
path_to_json = 'pheme-rumour-scheme-dataset/threads/en/germanwings-crash'
for found in find_file(path_to_json, 'tweet.json'):
    data_json = open(found, mode='r').read()
    data = json.loads(data_json)
    writer.writerow([data.get('id'),
                     'germanwings-crash',
                     data.get('text').encode('utf-8'), #unicode escape to fix emoji issue
                     data.get('favorite_count'),
                     data.get('retweet_count'),
		     data.get('created_at'),
		     data['user'].get('followers_count'),
		     data['user'].get('friends_count'),
		     data['user'].get('created_at'),
		     data['user'].get('verified')
		     ])
		     
path_to_json = '/home/csprj-08/Phemeproject/pheme-rumour-scheme-dataset/threads/en/ottawashooting'
for found in find_file(path_to_json, 'tweet.json'):
    data_json = open(found, mode='r').read()
    data = json.loads(data_json)
    writer.writerow([data.get('id'),
                     'ottawashooting',
                     data.get('text').encode('utf-8'), #unicode escape to fix emoji issue
                     data.get('favorite_count'),
                     data.get('retweet_count'),
		     data.get('created_at'),
		     data['user'].get('followers_count'),
		     data['user'].get('friends_count'),
		     data['user'].get('created_at'),
		     data['user'].get('verified')
		     ])	
		     

path_to_json = 'pheme-rumour-scheme-dataset/threads/en/prince-toronto'
for found in find_file(path_to_json, 'tweet.json'):
    data_json = open(found, mode='r').read()
    data = json.loads(data_json)
    writer.writerow([data.get('id'),
                     'prince-toronto',
                     data.get('text').encode('utf-8'), #unicode escape to fix emoji issue
                     data.get('favorite_count'),
                     data.get('retweet_count'),
		     data.get('created_at'),
		     data['user'].get('followers_count'),
		     data['user'].get('friends_count'),
		     data['user'].get('created_at'),
		     data['user'].get('verified')
		     ])
		     
path_to_json = 'pheme-rumour-scheme-dataset/threads/en/putinmissing'
for found in find_file(path_to_json, 'tweet.json'):
    data_json = open(found, mode='r').read()
    data = json.loads(data_json)
    writer.writerow([data.get('id'),
                     'putinmissing',
                     data.get('text').encode('utf-8'), #unicode escape to fix emoji issue
                     data.get('favorite_count'),
                     data.get('retweet_count'),
		     data.get('created_at'),
		     data['user'].get('followers_count'),
		     data['user'].get('friends_count'),
		     data['user'].get('created_at'),
		     data['user'].get('verified')
		     ])	
		     
path_to_json = 'pheme-rumour-scheme-dataset/threads/en/sydneysiege'
for found in find_file(path_to_json, 'tweet.json'):
    data_json = open(found, mode='r').read()
    data = json.loads(data_json)
    writer.writerow([data.get('id'),
                     'sydneysiege',
                     data.get('text').encode('utf-8'), #unicode escape to fix emoji issue
                     data.get('favorite_count'),
                     data.get('retweet_count'),
		     data.get('created_at'),
		     data['user'].get('followers_count'),
		     data['user'].get('friends_count'),
		     data['user'].get('created_at'),
		     data['user'].get('verified')
		     ])				     		     			     		     		     
csv_out.close()
csv_out1 = open('annotation.csv', mode='w')
writer = csv.writer(csv_out1) 
fields = ['id', 'is_rumour', 'misinformation'] #field names
writer.writerow(fields)
path_to_json = 'pheme-rumour-scheme-dataset/threads/en'
for found in find_file(path_to_json, 'annotation.json'):
    data_json = open(found, mode='r').read()
    head, tail = os.path.split(os.path.split(found)[0])
    data = json.loads(data_json)
    writer.writerow([tail,
                     data.get('is_rumour'),
                     data.get('misinformation')
		     ])	
csv_out1.close()

csv_out2 = open('reactions.csv', mode='w')
writer = csv.writer(csv_out2) 
fields = ['id', 'in_reply_to_status_id', 'created_at', 'text'] #field names
writer.writerow(fields)
path_to_json = 'pheme-rumour-scheme-dataset/threads/en'
for found in find_folder(path_to_json, 'reactions'):
    seek = os.path.join(found,'reactions')
    cwd = os.getcwd()
    seek1 = os.path.join(cwd,seek)
    os.chdir(seek1)
    for json_file in os.listdir(seek1):
    	if json_file.endswith('.json'):
    		data_json = open(json_file, mode='r').read()
    		data = json.loads(data_json)
    		writer.writerow([data.get('id'),
                     	data.get('in_reply_to_status_id'),
                     	data.get('created_at'),
                     	data.get('text').encode('utf-8')
		     	])
    os.chdir(cwd)
csv_out2.close()
csv_out3 = open('support.csv', mode='w')
writer = csv.writer(csv_out3) 
fields = ['threadid','tweetid','event', 'support', 'evidentiality', 'certainty', 'responsetype-vs-source','responsetype-vs-previous'] #field names
writer.writerow(fields)
data_support = open('pheme-rumour-scheme-dataset/annotations/en-scheme-annotations.json', mode='r').read()
dat = json.loads(data_support)
for line in dat:
	writer.writerow([line.get('threadid'),
		line.get('tweetid'),
		line.get('event'), 	
        	line.get('support'),
        	line.get('evidentiality'),
        	line.get('certainty'),
        	line.get('responsetype-vs-source'),
        	line.get('responsetype-vs-previous')
			     ])	


csv_out3.close()
Final = open('final.csv',mode='w')
writer = csv.writer(Final)
fields = ['tweetid', 'negationratio','event']
writer.writerow(fields)
File1 = open('tweets_out.csv', mode='r')
reader1 = csv.DictReader(File1)
for r1 in reader1:
	count=0
      	
	File2 = open('support.csv', mode='r')
	reader2 = csv.DictReader(File2)
	neg_count=0	
      	
	for r2 in reader2:
		tweet_id = r1['id']
			
		if tweet_id == r2['threadid']:
			count = count+1
			#print r1['event'],r2['event']	
			if r2['threadid'] == r2['tweetid']:
				
				if r2['support'] != 'supporting':
					neg_count =neg_count+1
				
			else:
				
				if r2['responsetype-vs-source'] != 'comment' and r2['responsetype-vs-source'] != 'agreed':
					neg_count +=1
							
					
			
	#print r1['id'],count,neg_count				
	negationratio = float(neg_count)/float(count)
	#print negationratio
	writer.writerow([r1['id'], negationratio,r1['event']])
      		
Final.close() 
Final = open('neg_ratio.csv',mode='w')
writer = csv.writer(Final)
fields = ['tweetid','event', 'negationratio','misinformation']
writer.writerow(fields)
File1 = open('annotation.csv', mode='r')
reader1 = csv.DictReader(File1)
for r1 in reader1:
	count=0
      	
	File2 = open('final.csv', mode='r')
	reader2 = csv.DictReader(File2)
	neg_count=0	
      	
	for r2 in reader2:
		tweet_id = r1['id']
			
		if tweet_id == r2['tweetid']:
			writer.writerow([r1['id'], r2['event'], r2['negationratio'], r1['misinformation']])
		
	
	
Final.close()
Final = open('tentativity.csv',mode='w')
writer = csv.writer(Final)
fields = ['tweetid', 'tentativity','misinformation']
writer.writerow(fields)
File = open('annotation.csv', mode='r')
reader = csv.DictReader(File)
no=0
for r in reader:
		File1 = open('support.csv', mode='r')
		reader1 = csv.DictReader(File1)
		for r1 in reader1:
			if r['id'] == r1['tweetid']:
				no=no+1 
				if r1['tweetid'] == r1['threadid']:
			
					if r1['certainty'] == 'certain':
						tentativity=0
					elif r1['certainty'] == 'somewhat-certain':
						tentativity =0.5
					else:
						tentativity =1
		
		
		
		writer.writerow([r['id'], tentativity, r['misinformation']])
		
	
	
Final.close()	

Final = open('role.csv',mode='w')
writer = csv.writer(Final)
fields = ['tweetid', 'role','misinformation']
writer.writerow(fields)
File = open('annotation.csv', mode='r')
reader = csv.DictReader(File)
no=0
for r in reader:
	File1 = open('tweets_out.csv', mode='r')
	reader1 = csv.DictReader(File1)
	for r1 in reader1:
		if r['id'] == r1['id']:
			no=no+1 
			role = float(r1['followers_count'])/float(r1['friends_count'])
		
	
	writer.writerow([r['id'], role, r['misinformation']])
	
	

Final.close()
Final = open('influence.csv',mode='w')
writer = csv.writer(Final)
fields = ['tweetid', 'influence','misinformation']
writer.writerow(fields)
File = open('annotation.csv', mode='r')
reader = csv.DictReader(File)
max_foll=1
for r in reader:
	
	File1 = open('tweets_out.csv', mode='r')
        
	reader1 = csv.DictReader(File1)
        
        for r1 in reader1:
        	
        	if r['id'] == r1['id']:
        		
            		if float(r1['followers_count']) >= max_foll:
				
	        		max_foll = r1['followers_count']
				max_foll = float(max_foll)



								
File = open('annotation.csv', mode='r')
reader = csv.DictReader(File)
no=0
for r in reader:
	File1 = open('tweets_out.csv', mode='r')
	reader1 = csv.DictReader(File1)
	for r1 in reader1:
		if r['id'] == r1['id']:
			no=no+1 
			influence = float(r1['followers_count'])/float(max_foll)
		
	
	writer.writerow([r['id'], influence, r['misinformation']])
	
	

Final.close()		
Final = open('credibility.csv',mode='w')
writer = csv.writer(Final)
fields = ['tweetid', 'credibility','misinformation']
writer.writerow(fields)
File = open('annotation.csv', mode='r')
reader = csv.DictReader(File)
no=0
for r in reader:
	File1 = open('tweets_out.csv', mode='r')
	reader1 = csv.DictReader(File1)
	for r1 in reader1:
		if r['id'] == r1['id']:
			no=no+1 
			if r1['verified'] == 'True':
				credibility=1
			else:
				credibility=0
		
	
	writer.writerow([r['id'], credibility, r['misinformation']])
	
	

Final.close()	
insight_dict={"think","thought","know","Unconfirmed", "consider","assume","determine","expect","feel","guess","imagine","suppose","suspect","doubt","disbelieve","says","said","shouted","confused","assumed","expected","felt","guessed","supposed","suspects","doubted","Maybe","maybe","say","suspects"}
Final = open('insight.csv',mode='w')
writer = csv.writer(Final)
fields = ['tweetid', 'insight_score','misinformation']
writer.writerow(fields)
File = open('annotation.csv', mode='r')
reader = csv.DictReader(File)
no=0
for r in reader:
	File1 = open('tweets_out.csv', mode='r')
	reader1 = csv.DictReader(File1)
	for r1 in reader1:
		if r['id'] == r1['id']:
			no=no+1 
			text=str(r1['text'])
			length=len(text.split())
			insight=0
			for item in insight_dict:
	
				if item in text:
					insight=insight+1
		

		
			insight_score=float(insight)/float(length)
			writer.writerow([r1['id'], insight_score, r['misinformation']])


Final.close()
abbr_dictionary={"B4","b4","B/C","b/c","BAE","bae","BFF","bff","BRB","brb","BTW","btw","DAE","dae","F2F","f2f","FOMO","FTFY","fomo","ftfy","FTW","ftw","FYI","Gr8","GTG","gtg","HBD","hbd","HMB","hmb","HTH","hth","IDC","IDK","ILY","IMO","IRL","JK","Irl","jk","L8","LMK","LOL","l8","lmk","lol","OMG","omg","OMW","omw","ROFL","rofl","RT","Thx","Txt","w/","WBU","bday"}
vulgar_dictionary={"arse","arsehole","ass","asshole","badass","bastard","beaver","bitch","bollock","boner","bogger","bullshit","bum","cock","crap","creampie","cunt","dick","dickhead","dyke","fag","faggot","fart","fatass","fuck","fucking","fucked","greek","holyshit","jack ass","jerk ass","kick ass","kick-ass","kike","kikes","Nigga","Nigger","piss","shit","STFU","trap","trap","shitty","suck","twat","wank","tit"}
Final = open('maturity.csv',mode='w')
writer = csv.writer(Final)
fields = ['tweetid','smiley','abbr_score','vulgarity','word_complexity','avg_word_complexity','sentence_complexity','maturity']
writer.writerow(fields)

File1 = open('tweets_out.csv', mode='r')
reader1 = csv.DictReader(File1)
max_length=0
max_complexity=0
for r1 in reader1:
	length=len(r1['text'].split())
	#print length
	chr_length=len(r1['text'])
	#print chr_length
	word_complexity = float(chr_length)/float(length)
	#print r1['id'],chr_length,length,word_complexity
	if word_complexity>max_complexity:
		max_complexity=word_complexity
		#print max_complexity


	if length>max_length:
		max_length=length
		#print max_length
	
File2 = open('tweets_out.csv', mode='r')
reader2 = csv.DictReader(File2)		
for r2 in reader2:
	
	text=r2['text'].decode('utf-8')
	length=len(r2['text'].split())
	abbr=0
	for item in abbr_dictionary:
		
		if item in r2['text'].split():
			#print r1['id'],r1['text'],item
			abbr=abbr+1

	
	abbr_score=float(abbr)/float(length)
	vulg=0
	for item in vulgar_dictionary:
		
		if item in r2['text'].split():
			#print r1['id'],r1['text'],item,length
			vulg=vulg+1


	vulgarity=float(vulg)/float(length)
	char_length=len(r2['text'])
	word_complexity=float(char_length)/float(length)
	#print r2['id'],char_length,length,word_complexity
	avg_word_complexity=word_complexity/max_complexity
	sentence_complexity=float(length)/float(max_length)
	maturity = (text_has_emoji(text) + abbr_score + vulgarity + avg_word_complexity + sentence_complexity)/5
	writer.writerow([r2['id'],text_has_emoji(text),abbr_score,vulgarity,word_complexity,avg_word_complexity,sentence_complexity,maturity])

Final.close()
Final = open('controversiality.csv',mode='w')
writer = csv.writer(Final)
fields = ['tweetid', 'controversiality']
writer.writerow(fields)
File1 = open('tweets_out.csv', mode='r')
reader1 = csv.DictReader(File1)
for r1 in reader1:
	count=0
      	
      	File2 = open('support.csv', mode='r')
	
	reader2 = csv.DictReader(File2)
	neg_count=0	
      	for r2 in reader2:
		tweet_id = r1['id']
			
		if tweet_id == r2['threadid']:
			count = count+1
				
			if r2['threadid'] == r2['tweetid']:
				
				if r2['support'] != 'supporting':
					neg_count =neg_count+1
				
			else:
				
				if r2['responsetype-vs-source'] != 'comment' and r2['responsetype-vs-source'] != 'agreed':
					neg_count +=1
							
					
			
	p=count-neg_count
	n=neg_count
	a1=float(p+1)/float(n+1)
	a2=float(n+1)/float(p+1)
	a=min(a1,a2)
	controversiality=count**a
	writer.writerow([r1['id'], controversiality])
      		
Final.close() 

Final = open('engagement.csv',mode='w')
writer = csv.writer(Final)
fields = ['tweetid', 'engagement']
writer.writerow(fields)
File1 = open('tweets_out.csv', mode='r')
reader1 = csv.DictReader(File1)
for r1 in reader1:
	account_age=r1['account_creation'].split()
	tweet_year=r1['created_at'].split()
	age=int(tweet_year[5])-int(account_age[5])
	if tweet_year[5] == account_age[5]:
	
	      if tweet_year[1] == account_age[1]:
	       
	                age = age+0.02
	       
	      else:
	       
	                age = age+0.2
	       
	
	
	activity=float(r1['followers_count'])+float(r1['friends_count'])
	engagement=activity/float(age)
	writer.writerow([r1['id'],engagement])
		
Final.close()
veracity_final = open('veracity_final.csv',mode='w')
writer = csv.writer(veracity_final)
fields = ['id','neg_ratio','tentativity','maturity','insight','controversiality','role','influence','credibility','engagement','misinformation']
writer.writerow(fields)
f1 = open('neg_ratio.csv',mode='r')
reader1 = csv.DictReader(f1)
for r1 in reader1:
	f2 = open('tentativity.csv',mode='r')
	reader2 = csv.DictReader(f2)
	for r2 in reader2:
		if r1['tweetid'] == r2['tweetid']:
			f3 = open('maturity.csv',mode='r')
			reader3 = csv.DictReader(f3)
			for r3 in reader3:
				if r1['tweetid'] == r3['tweetid']:
					f4 = open('insight.csv',mode='r')
					reader4 = csv.DictReader(f4)
					for r4 in reader4:
						if r1['tweetid'] == r4['tweetid']:
							f5 = open('controversiality.csv',mode='r')
							reader5 = csv.DictReader(f5)
							for r5 in reader5:
								if r1['tweetid'] == r5['tweetid']:
									f6 = open('role.csv',mode='r')
									reader6 = csv.DictReader(f6)
									for r6 in reader6:
										if r1['tweetid'] == r6['tweetid']:
											f7 = open('influence.csv',mode='r')
											reader7 = csv.DictReader(f7)
											for r7 in reader7:
												if r1['tweetid'] == r7['tweetid']:
													f8 = open('credibility.csv',mode='r')
													reader8 = csv.DictReader(f8)
													for r8 in reader8:
														if r1['tweetid'] == r8['tweetid']:
															f9 = open('engagement.csv',mode='r')
															reader9 = csv.DictReader(f9)
															for r9 in reader9:
																if r1['tweetid'] == r9['tweetid']:
																	writer.writerow([r1['tweetid'],r1['negationratio'],r2['tentativity'],r3['maturity'],r4['insight_score'],r5['controversiality'],r6['role'],r7['influence'],r8['credibility'],r9['engagement'],r1['misinformation']])
																
															
														
													
												
											
										
									
								
							
						
					
				
			
		
	


																	














veracity_final.close()


