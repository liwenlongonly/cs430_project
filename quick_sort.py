#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import random
from median_finding import median_finding_randomized 
import sys
sys.setrecursionlimit(10000000)
class quick_sort:

	def main(self,n,type_="random"):
		self.n=n
		self.type_=type_
		self.quicksort(self.n,0,len(n)-1)
		return self.n	

	def partition(self,n,p,r):
		# random 代表使用随机数来进行快速排序
		# median 代表使用中值来进行快速排序
		# 不传   代表使用数组最后一个值的正常快速排序
		
		if str(self.type_)=="random":
			random_x=random.randint(p,r-1)
			temp=n[random_x]
			n[random_x]=n[r]
			n[r]=temp
		if str(self.type_)=="median":
			
			n[r]=median_finding_randomized(n,p,r,int((r-p)/2+1))
		
		x=n[r]
		i=p-1
		for j in range(p,r):
 
			if n[j]<=x:
				i+=1
				temp=n[i]
				n[i]=n[j]
				n[j]=temp

		temp=n[i+1]
		n[i+1]=n[r]
		n[r]=temp
		return i+1

	def quicksort(self,n,p,r):
		if p<r:
			q=self.partition(n,p,r)
			self.quicksort(n,p,q-1)
			self.quicksort(n,q+1,r)
	


if __name__ == '__main__':

	num=5000
	n=[]
	for x in range(0,num):
		n.append(random.randint(0,x))

	obj_=quick_sort()
	#a=time.time()
	obj_.main(n,'median')#带中值快排
	#b=time.time()
	obj_.main(n,'random')#带随机数快排
	#c=time.time()
	obj_.main(n,'')#直接快排
	# d=time.time()
	# print(b-a)
	# print(c-b)
	# print(d-c)	