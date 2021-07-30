data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))


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