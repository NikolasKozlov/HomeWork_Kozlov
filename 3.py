import collections

text = input('enter words\n')
str = text.split()
counter = collections.Counter(str)
common = counter.most_common()
long = max(str, key=len)
print(common, long)
