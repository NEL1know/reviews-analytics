
# 讀取檔案
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))

print('檔案讀取完了,總共有', len(data), '筆資料')

# 文字記數
wc = {} # word_count 字典
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else :
			wc[word] = 1 #新增新的key進wc字典裡
for word in wc:
	if wc[word]>100000 :
		print(word, ': ', wc[word])

print('字典中有: ', len(wc),'個詞')

while True:
	word = input('請問你想查什麼單詞: ')
	if word == 'q':
		print('感謝使用本查詢功能')
		break
	print (word, '出現過的次數為', wc[word], '次')

# 留言平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均長度為' ,sum_len/len(data))

# 留言長度小於100
hundred = []
for d in data:
	if len(d) < 100:
		hundred.append(d)
print('一共有', len(hundred), '筆留言長度小於100')
print(hundred[0])

# 留言提及good的筆數
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提及good')
print(good[0])