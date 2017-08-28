import pandas as pd
fields = ['imdb_profile', 'twitter_profile']
df = pd.read_csv('E:/userlist.csv', skipinitialspace=True, usecols=fields)
usr=[]
twpro=df.twitter_profile.str[20:len(df.twitter_profile)]
profile=twpro.tolist()
for i in profile:
    if '?' in i:
        u=i.split('?')
        usr.append(u[0])
        
    elif '/' in i:
        u=i.split('/')
        usr.append(u[0])
        
    else:
        usr.append(i)  
        
csvdataframe=pd.DataFrame(usr,columns=['twitter user'])
csvdataframe.to_csv("E:/usr.csv",index=False)




