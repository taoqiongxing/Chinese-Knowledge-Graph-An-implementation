import glob
import os
import re
import pickle as pkl
pages=glob.glob('../ie/info-table/*')

# pattern=re.compile(r'[\u4e00-\u9fa5]+')


class entity:
	def __init__(self):
		self.name=''
		self.attr=dict()
	def set_name(self,name):
		self.name=name
	def add_attr(self,attr,name):
			self.attr[attr]=name
attrs=[]
entities=[]
kgtxt=open('./triples.txt','a+')
result=''
for page in pages:
    
	name=page.replace("\\","/").split('/')[-1][:-4]
	lines=open(page,'r',encoding='utf-8').readlines()
	if len(lines)<1:
		continue
	ent=entity()
	ent.name=name
	for i,line in enumerate(lines):
		arrs=line.split('$$')
		if len(arrs)!=2:
			continue
		attr=arrs[0].replace(' ','')
		value=arrs[1].replace('\n','')
		attrs.append(attr)
		ent.add_attr(attr,value)
		print("name:{}  attr:{}  value:{}".format(name,attr,value))
		try:
			kgtxt.write(name+"$$"+attr+"$$"+value+"\n")
		except Exception:
			print(name+"$$"+attr+"$$"+value+"error")
	entities.append(ent)

kgtxt.close()
pkl.dump(attrs,open('./attrs.bin','wb'))
pkl.dump(entities,open('./entities.bin','wb'))
print('done')