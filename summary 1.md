# 百度飞桨领航团零基础Python速成营 课程总结1


	[课程链接](https://aistudio.baidu.com/aistudio/course/introduce/7073)：https://aistudio.baidu.com/aistudio/course/introduce/7073

	[飞桨官网](https://www.paddlepaddle.org.cn/)：https://www.paddlepaddle.org.cn/	![paddlepaddle]https://paddlepaddle-org-cn.cdn.bcebos.com/paddle-site-front/favicon-128.png

	[推荐学习网站](https://www.runoob.com/python3/python3-tutorial.html)：https://www.runoob.com/python3/python3-tutorial.html

****
## 目录
* [计算机基础](#计算机基础)
* [Python基础](#Python基础)
* [作业一：Python编程基础](#作业一：Python编程基础)

# 课节1：Python计算基础及环境搭配搭建

## 计算机基础

 - 编程语言：（Programming Language），是用来定义计算机程序的形式语言。
        Python就是一种广泛使用的解释型、高级和通用的编程语言。 
 - 计算机的基本组成：控制器，运算器，存储器，输入设备，输出设备。
 
        存储器分为两类：
        - 内存：（Random Access Memory，缩写：RAM；也叫主存）是与 CPU直接交换数据的内部存储器。它可以随时读写，而且速度很快，通常作为操作系统或其他正在运行中的程序的临时资料存储介质。但具有断电易失性。
        
        - 外存：（Non-Volatile Memory，缩写：NVM；也叫非易失性存储器）是指当电流关掉后，所存储的资料不会消失的电脑存储器。非易失性存储器中，依存储器内的资料是否能在使用电脑时随时改写为标准，可分为二大类产品，即ROM和Flash memory（即闪存）。
 - 计算机系统： 硬件：CPU、存储器、键盘鼠标、显示器。 

		软件：
        - 操作系统：（英语：Operating System，缩写：OS）是一组主管并控制计算机	操作、运用和运行硬件、软件资源和提供公共服务来组织用户交互的相互关	联的系统软件程序，同时也是计算机系统的内核与基石。）
        - 应用程序：（英语：Application program）或应用软件（Application 	software），简称应用（app），是电脑软件的主要分类之一，是指为针对用户的某种特殊应用目的所撰写的计算机程序。
 - 进制 
  
        - 二进制：二进制（binary）在数学和数字电路中指以2为基数的记数系统，以2为基数代表系统是二进位制的。 
        - 二进制与十进制的转换。

 ## Python基础
 

 - **标识符**是由字符（A~Z 和 a~z）、下划线和数字组成，但第一个字符不能是数字。 标识符不能和 Python 中的保留字相同。 Python中的标识符中，不能包含空格、@、% 以及 $ 等特殊字符。 在 Python 中，标识符中的字母是严格区分大小写的。
 &nbsp;

- <center>表1. Python 运算符优先级和结合性一览表</center>

	| 运算符说明| Python运算符| 优先级 | 结合性 |优先级顺序|
	|:-----------:| :-------------:|:-------------:| :-------------: | :-------------: |
	| 小括号|	( )	|19	|无 |高
	|索引运算符|	x[i] 或 x[i1: i2 [:i3]]	|18	|左|&uarr;
	|属性访问	|x.attribute	|17|	左|`| `
	|乘方	|**	|16|	右|`| `
	|按位取反|	~	|15|	右|`| `
	|符号运算符	|+（正号）、-（负号）|	14	|右|`| `
	|乘除|	*、/、//、%|	13|	左|`| `
	|加减|	+、-	|12	|左|`| `
	|位移|	>>、<<	|11	|左|`| `
	|按位与|	&	|10	|右|`| `
	|按位异或|	^	|9	|左|`| `
	|按位或| `| ` |8|	    左|`| `
	|比较运算符|	==、!=、>、>=、<、<= 	|7	|左|`| `
	|is 运算符	|is、is not	|6|	左|`| `
	|in 运算符|	in、not in	|5	|左|`| `
	|逻辑非	|not	|4	|右|`| `
	|逻辑与	|and	|3	|左|`| `
	|逻辑或	|or	|2	|左|`| `
	|逗号运算符|	exp1, exp2	|1	|左|低

&nbsp;

 - **Python数据类型**：数字（Number）、字符串（String）、列表（List）、元组（Tuple）、集合（Set）、字典（Dictionary）

 	- 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）。 

	 - 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
	 &nbsp;
	  
	**1. 数字**
	
	整型、浮点型、布尔型、复数
	/&emsp;除法，得到一个浮点数
	// &ensp;除法，得到一个整数，向下取整
	%&ensp;取余
	**&ensp;乘方
	- 混合计算时，Python会把整型转换成为浮点数。
	- round()函数计算浮点数，round(x [, n])。
	- 复数complex(a,b)表示，复数的实部a和虚部b都是浮点型。
	&nbsp;
	
	**2. 字符串**
	- Python中的字符串用单引号 ' 或双引号 " 括起来。
	- 索引值以0为开始值，-1为从末尾的开始位置。
	- 加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，与之结合的数字为复制的次数。
	- 反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个r，表示原始字符串。
	&nbsp;
	
	**3. 列表**
	- 列表是写在方括号[ ]之间、用逗号分隔开的元素列表。
	- 索引值以0为开始值，-1从末尾的开始位置。
	- 加号 + 是列表连接运算符，星号 * 是重复操作。
	- append()函数用于在列表末尾添加新的对象。list.append(obj)
	- pop()函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。list.pop([index=-1])
	&nbsp;
	
	**4. 元组**
	- 元组与列表类似，不同之处在于元组的元素不能修改。元组写在小括号()里，元素之间用逗号隔开。
	- 元组中的元素类型也可以不相同
	&nbsp;
	
	**5. 集合**
	- 集合是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
	- 基本功能是进行成员关系测试和删除重复元素。
	- 可以使用大括号{ }或者set()函数创建集合，注意：创建一个空集合必须用set()而不是{ }，因为{ }是用来创建一个空字典。
	&nbsp;
	
	**6. 字典**
	- 字典是Python中另一个非常有用的内置数据类型。
	-  字典是一种映射类型，字典用{ }标识，它是一个无序的键(key):值(value)的集合。
	- 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
	- 键(key)必须使用不可变类型。
	
&nbsp;

- <center>表2. 数据类型转换</center>

	|函数	|  描述   |
	|--|:--|
	| int(x [,base])| 将x转换为一个整数| 
	| float(x)| 将x转换到一个浮点数| 
	| complex(real [,imag])| 创建一个复数| 
	| str(x)| 将对象 x 转换为字符串| 
	| repr(x)| 将对象 x 转换为表达式字符串| 
	| eval(str)| 用来计算在字符串中的有效Python表达式,并返回一个对象| 
	| tuple(s)| 将序列 s 转换为一个元组| 
	| list(s)| 将序列 s 转换为一个列表| 
	| set(s)| 转换为可变集合| 
	| dict(d)| 创建一个字典。d 必须是一个 (key, value)元组序列| 
	| frozenset(s)| 转换为不可变集合| 
	| chr(x)| 将一个整数转换为一个字符| 
	| ord(x)| 将一个字符转换为它的整数值| 
	| hex(x)| 将一个整数转换为一个十六进制字符串| 
	| oct(x)| 将一个整数转换为一个八进制字符串| 

- 流程控制：
1. **条件判断语句**：
	
	**If语句**
	```python
	if condition_1: 
		statement_block_1 
	elif condition_2: 
		statement_block_2 
	else: 
		statement_block_3
     ```
2. **循环语句**

	**while语句**
	```python
	while 判断条件(condition)：
	    执行语句(statements)……
	```
	
	**for语句**
	
	for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
	
	```python
	for <variable> in <sequence>: 
		<statements> 
	else: 
		<statements>
	```

	range()函数创建一个整数列表，一般用在 for 循环中。range(start, stop[, step])
	结合range()和len()函数遍历一个序列的索引：
	
	```python
	>>>a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ'] 
	>>> for i in range(len(a)): ... print(i, a[i])
	使用range()函数来创建一个列表：
	>>>list(range(5)) 
	[0, 1, 2, 3, 4]
	```

3. **break,continue,pass语句**

	break 语句跳出 for 和 while 的循环体。
	continue 语句跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
	pass是空语句，是为了保持程序结构的完整性。不做任何事情，用作占位语句

&nbsp;

## 作业一：Python编程基础
按要求补全下列代码：
1. 输入两个整数，并打印出它们的和
	
	```python
	a = input('请输入第一个整数: ')
	b = input('请输入第二个整数: ')
	print('\n')
	
	# 分别把 a、b 转换成整数
	a = int(a)
	b = int(b)
	
	# 计算 a、b 的和，赋值给变量c
	c = a+b
	
	# 打印c
	print('第一个整数:')
	print(a)
	print('第二个整数:')
	print(b)
	print('整数和结果c是:')
	print(c)
	```
	输出：
	```
	请输入第一个整数: 
	请输入第二个整数: 
	
	第一个整数:
	123
	第二个整数:
	321
	整数和结果c是:
	444
	```

2. 输入两个整数，如果两个整数之和小于100，则输出 '小于100'，否则输出 '不小于100'。

	```python
	a = input('请输入第一个整数: ')
	b = input('请输入第二个整数: ')
	print('\n')
	# 分别把 a、b 转换成整数
	a = int(a)
	b = int(b)
	
	# 计算 a、b 的和，赋值给变量c
	c = a+b
	
	# 判断c是否小于100，按要求输出
	
	print('第一个整数')
	print(a)
	print('第二个整数:')
	print(b)
	if c < 100:
	    print('小于100')
	else:
	    print('不小于100')
	```
	输出：
	```
	请输入第一个整数: 
	请输入第二个整数: 
	
	第一个整数
	123
	第二个整数:
	321
	不小于100
	```

3. 输入两组姓名和年龄，然后存入一个字典，并输出。

	```python
	name1 = input('请输入第一个姓名: ')
	age1= input('请输入第一个年龄: ')
	name2 = input('请输入第二个姓名: ')
	age2 = input('请输入第二个年龄: ')
	
	# 分别把age1和age2转成整数
	age1 = int(age1)
	age2 = int(age2)
	
	# 构造字典dict_name
	
	dict = {'name':dict_name, 'age':dict_age}
	dict_name = {'name1': name1, 'name2': name2}
	dict_age = {'age1': age1, 'age2': age2}
	# 打印字典
	print(dict)
	```
	输出：
	```
	请输入第一个姓名: 
	请输入第一个年龄: 
	请输入第二个姓名: 
	请输入第二个年龄: {'name': {'name1': 'q', 'name2': 'w'}, 'age': {'age1': 12, 'age2': 21}}
	```

4. 依次输入10组整数，然后求和，并输出
	
	```python
	sum_num = 0
	for i in range(10):
	    # 用input输入数字并转化为整数
	    num=input()
	    num=int(num)
	    print(num)
	   
	    # sum_num 对输入的数字进行累加
	    sum_num=sum_num+num
	print(sum_num)
	```
	输出：
	```
	1
	2
	3
	4
	5
	6
	7
	8
	9
	10
	55
	```
	
	:sweat_smile:
