from typing import Tuple

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print(data[0])            

print('read process compile total count is', len(data), 'data' )

sum_len = 0
for d in data:
     sum_len = sum_len + len(d)
print('Avarge length of rreview is', sum_len / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)

print('total', len(new), 'data length < 100')        
print('----------')
print(new[0])
print(new[1])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('Total have', len(good), 'review')      
print(good[0])  

# word count

wc = {} #word count dictionary
for d in data:
    words = d.split() #default is space
    for word in words:
        if word in wc:
            wc[word] += 1
        else:    
            wc[word] = 1 # add new key in wc{}

for word in wc:
    if wc[word] > 100000:
        print(word, wc[word])

print(len(wc))
print(wc['Ben'])
    
while True:
    word = input('What do you want to search: ')   
    if word == 'q':
        break 
    if word in wc:
        print(word, 'display how many times in', wc[word])
    else:
        print('There is not exit')    
print('Thanks for your using, Bye!')