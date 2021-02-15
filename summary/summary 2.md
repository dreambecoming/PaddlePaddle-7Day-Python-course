# 百度飞桨领航团零基础Python速成营 课程总结2
![paddlepaddle](https://paddlepaddle-org-cn.cdn.bcebos.com/paddle-site-front/favicon-128.png  "百度logo")

[课程链接](https://aistudio.baidu.com/aistudio/course/introduce/7073) `：https://aistudio.baidu.com/aistudio/course/introduce/7073`  
[飞桨官网](https://www.paddlepaddle.org.cn/)`：https://www.paddlepaddle.org.cn/`   
[推荐学习网站](https://www.runoob.com/python3/python3-tutorial.html)`：https://www.runoob.com/python3/python3-tutorial.html`

****
## 目录
* [进阶](#进阶)
* [作业二：Python编程基础（二）](#作业二Python编程基础二)

# 课节2：Python编程基础
## 进阶
**1.字符串** 
- 常用函数：
	- 索引：字符串[start: end: step]，默认从左到右，左闭右开
	- 拆分：
			split()函数：对字符串进行切片，参数str默认所有空字符，num默认-1,分隔num+1个子字符串。
			str.split(str="", num=string.count(str)).
	- 替换：
			replace()函数：对子字符串进行替换，替换不超过max次。replace不会改变原字符串的内容。
			str.replace(old, new[, max])
	- 计数：
			count()函数：统计字符串里某个字符出现的次数。str.count(sub,start=0,end=len(string))
	- 查找：
		- find()函数：判断字符串中是否包含子字符串，包含子字符串返回开始的索引值，否则返回-1。
							str.find(str, start=0, end=len(string))
		- index()函数：与find()函数一样，只不过如果str不在string中会报一个异常。
					str.index(str,start=0, end=len(string))
	- 判断：
		- startswith()函数：判断字符串是否是以指定前缀开头，是则返回True，否则返回False。
				str.startswith(prefix[, start[, end]])
		- endswith()函数：判断字符串是否以指定后缀结尾，是则返回True，否则返回False。
				str.endswith(suffix[, start[, end]])
	- 变形：
		- upper()、lower()函数：大小写字母转化。
		- capitalize()函数：将字符串的第一个字母变成大写,其他字母变小写。
		- strip()函数：移除字符串头尾指定的字符（默认为空格）或字符序列。str.strip([chars]
- 格式化输出：
	- %-formatting语句：
		- <center>表1. Python字符串格式化符号一览表</center>
		
			 |  	       符号	  |     描 述       | 
			 |:-----------------: | :----------------:|
		     |     			%c	                |格式化字符及其ASCII码|
		     |				%s					 |格式化字符串|
		     |				%d					 |格式化整数|
		     |				%u					 |格式化无符号整型|
		     |				%o					 |格式化无符号八进制数|
		     |				%x					 |格式化无符号十六进制数|
		     |				%X				 |格式化无符号十六进制数（大写）|
		     |				%f	 				 |格式化浮点数字，可指定小数点后的精度|
	         |				%e					 |用科学计数法格式化浮点数|
	      	 |				%E				 |作用同%e，用科学计数法格式化浮点数|
		     |				%g					 |%f和%e的简写|
		     |				%G				 |%f 和 %E 的简写|
	         |				%p					 |用十六进制数格式化变量的地址|
	&nbsp;

	- 格式化函数format()，通过 {} 和 : 来代替以前的 % 。
	- 格式化字符串f-string，以f或F修饰符引领的字符串（f'xxx'或F'xxx'），以大括号{}标明被替换的字段，实际上是运行时运算求值的表达式。
	
	&nbsp;
	
**2.列表**
- 常用函数：
	- append()函数用于在列表末尾添加新的对象。list.append(obj)
	- insert()函数用于将指定对象插入列表的指定位置。list.insert(index, obj)
	- extend() 函数用于在列表末尾一次性追加另一个序列中的多个值list.extend(seq)
	- pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
		list.pop([index=-1])
	- remove() 函数用于移除列表中某个值的第一个匹配项。list.remove(obj)
	
	&nbsp;
	
- 列表生成式（List Comprehensions）
	```python
	list_1 = [1,2,3,4,5]
		
	#求偶数项 
	even=[n for n in list_1 if n%2==0]
	print('偶数项：',even)
	#求奇数项 
	odd=[n for n in list_1 if n%2==1]
	print('奇数项：',odd)
	```

	```
	偶数项： [2, 4]
	奇数项： [1, 3, 5]
	```
	
- **生成器（generator）**

	```python
	#例1
	def factor(max_num):
	    # 这是一个函数  用于输出所有小于max_num的质数
	    factor_list = []
	    n = 2
	    while n<max_num:
	        find = False
	        for f in factor_list:
	            # 先看看列表里面有没有能整除它的
	            if n % f == 0:
	                find = True
	                break
	        if not find:
	            factor_list.append(n)
	            yield n
	            
	        n+=1
	```
	
	```python
	# 输入参数max_num，输出生成器
	max_num = 10
	g = factor(max_num)
	print(g)
	
	# 输出生成器对象所有元素
	for n in g:
	    print(n)
	```
	输出：
	```
	<generator object factor at 0x7fd494568ad0>
	2
	3
	5
	7
	```

	```python
	# next() 返回生成器的下一个项目
		max_num = 10
		h = factor(max_num)
		for i in range(max_num):
		    print(next(h))
	```
	输出
	```
			2
			3
			5
			7
			---------------------------------------------------------------------------StopIteration          Traceback (most recent call last)
			<ipython-input-11-5d0bf69b3548> in <module>
			      3 h = factor(max_num)
			      4 for i in range(max_num):
		    ----> 5     print(next(h))
			StopIteration: 
	```
		
	```python
	# 例2 斐波那契数列
	def feb(max_num):
	    n_1 = 1
	    n_2 = 1
	    n = 0
	    while n<max_num:
	        if n == 0 or n == 1:
	            yield 1
	            n += 1
	        else:
	            yield n_1 + n_2
	            new_n_2 = n_1 
	            n_1 = n_1 + n_2
	            n_2 = new_n_2
	            n += 1
	```
	```python
	max_num=5
	j = feb(max_num)
	for n in j:
	    print(n)
	```
	输出：
	```
	1
	1
	2
	3
	5
	```
	- yield 的作用就是把一个函数变成一个 generator。 执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行。
	- StopIteration 异常用于标识迭代的完成

## 作业二：Python编程基础（二）
按要求完成下列代码：
1. 选取列表的第2到第5项，并打印（从0开始计数，即取出c d e f）

	```python
	words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
	
	# 选取第2-5项，并打印
	# 索引左闭右开
	print(words[2:6])
	```
	输出：
	```
	['c', 'd', 'e', 'f']
	```
2. 使用列表生成式的方法，根据 list1 生成 list2

	```python
	list1 = [1, 2, 3, 4, 5, 6, 7, 8]
	
	# 列表推导式生成list2
	list2 = [n*100 for n in list1]
	
	print(list2)
	```
	输出：
	```
	[100, 200, 300, 400, 500, 600, 700, 800]
	```

3. 把下列字符串按下划线('_')划分成若干个片段
	string1 = 'this_is_a_sample'
	生成按'_'划分的字符串列表，即下列内容
	['this', 'is', 'a', 'sample']
	
	```python
	string1 = 'this_is_a_sample'
	
	# 按'_'划分string1
	string1.split('_')
	```
	输出：
	```
	['this', 'is', 'a', 'sample']
	```

