# 百度飞桨领航团零基础Python速成营 课程总结1
![paddlepaddle](https://paddlepaddle-org-cn.cdn.bcebos.com/paddle-site-front/favicon-128.png  "百度logo")

[课程链接](https://aistudio.baidu.com/aistudio/course/introduce/7073) `：https://aistudio.baidu.com/aistudio/course/introduce/7073`  
[飞桨官网](https://www.paddlepaddle.org.cn/)`：https://www.paddlepaddle.org.cn/`   
[推荐学习网站](https://www.runoob.com/python3/python3-tutorial.html)`：https://www.runoob.com/python3/python3-tutorial.html`

****
## 目录
* [函数（Function）](#函数（Function）)
* [模块（Module）](#模块（Module）)
* [作业三：Python函数基础（大作业）](#作业三：Python函数基础（大作业）)


# 课节3: Python函数基础


## 函数（Function）
- 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
- 函数能提高应用的模块性，和代码的重复利用率。
- 定义函数
	```python
	def functionname( parameters ): 
		"函数_文档字符串" 
		function_suite 
		return [expression]
	```
- 参数传递：
	- 必选参数：必选参数须以正确的顺序传入函数、数量必须和声明时的一样。
	- 默认参数：默认参数的值如果没有传入，则被认为是默认值。
	- 可变参数：加了星号（*）的变量名会存放所有未命名的变量参数。可变参数在函数调用时自动组装为一个tuple。
	- 关键字参数：关键字参数在函数内部自动组装为一个dict。
		```python
		def score_info(name, **kw):
		    if '语文成绩' in kw:
		        print(name, '的语文成绩', kw['语文成绩'])
		    if '数学成绩' in kw:
		        print(name, '的数学成绩', kw['数学成绩'])
		        
		
		def person_info(name, age, **kw):
		    print('姓名：', name, ' 年龄',age)
		    score_info(name, **kw)    
		
		score_cfg = {'语文成绩':65, '数学成绩':60}
		person_info('张三', 18, **score_cfg)
		```
	- 命名关键字参数：限制关键字参数的名字。和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。 命名关键字参数必须传入参数名，可以有缺省值，可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔 符*。
	- 参数定义的顺序必须是：必选参数 --> 默认参数 --> 可变参数 --> 命名关键字参数 --> 关键字参数
- 命名空间（Namespace）:
	命名空间是从名称到对象的映射，大部分的命名空间都是通过 Python 字典来实现的。命名空间提供了在项目中避免名字冲突的一种方法。各个命名空间是独立的，没有任何关系的，所以一个命名空间中不能有重名，但不同的命名空间是可以重名而没有任何影响。
	- 内置命名空间（Built-in names）： 用于存放Python 的内置函数的空间，比如，print，input等不需要定义即可使用的函数就处在内置命名空间。
	- 全局命名空间（Global names）：模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
	- 局部命名空间（Local names）：函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。在函数内定义的局部变量，在函数执行结束后就会失效，即无法在函数外直接调用函数内定义的变量。
	- 命名空间查找顺序： 局部命名空间→全局命名空间→内置命名空间。
	- 命名空间的生命周期：取决于对象的作用域，如果对象执行完成，则该命名空间的生命周期就结束。
- 作用域（Scope）：
作用域就是一个 Python 程序可以直接访问命名空间的正文区域。在一个 python 程序中，直接访问一个变量，会从内到外依次访问所有的作用域直到找到，否则会报未定义的错误。
	- Local：在程序的最内层，包含局部变量，比如，一个函数的内部。
	- Enclosing：包含了非局部(non-local)也非全局(non-global)的变量。比如，两个嵌套函数，函数（或类）A里面又包含了函数B，那么对于B中的名称来说 A中的作用域就为no-nlocal。
	- Global：当前脚本的最外层，比如，当前模块的全局变量。
	- Built-in： 包含了内建的变量/关键字等，比如，int。全局变量和局部变量。定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
	- 作用域查找顺序： L –> E –> G –> B。
- 匿名函数：lambda [arg1 [,arg2,.....argn]]:expression
- 高阶函数：一个函数可以作为参数传给另外一个函数，或者一个函数的返回值为另外一个函数（若返回值为该函数本身，则为递归）。
	- map() 函数会根据提供的函数对指定序列做映射。第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
	map(function, iterable, ...)。
	Python 2.x 返回列表。Python 3.x 返回迭代器。
	- reduce() 函数会对参数序列中元素进行累积。函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
	reduce(function, iterable[, initializer])
		- 注意：Python3.x reduce() 已经被移到 functools 模块里，如果我们要使用，需要引入 functools 模块来调用 reduce() 函数：from functools import reduce
	- sorted() 函数对所有可迭代的对象进行排序操作。sorted(iterable, cmp=None, key=None, reverse=False)
	- 偏函数：将所要承载的函数作为partial()函数的第一个参数，原函数的各个参数依次作为partial()函数后续的参数，除非使用关键字参数。from functools import partial

	- 装饰器（Decorators）：修改其他函数的功能的函数。装饰器最大的优势是用于解决重复性的操作，其主要使用的场景有如下几个：
		- 计算函数运行时间
		- 给函数打日志
		- 类型检查
		```python
			# 装饰器输入一个函数，输出一个函数
		def print_working(func):
		    def wrapper():
		        print(f'{func.__name__} is working...')
		        func()
		    return wrapper
		
		def worker1():
		    print('我是一个勤劳的工作者！')
		def worker2():
		    print('我是一个勤劳的工作者！')
		def worker3():
		    print('我是一个勤劳的工作者！')
		
		worker1 = print_working(worker1)
		worker1()
		worker2= print_working(worker2)
		worker2()
		worker3= print_working(worker2)
		worker3()
		```
		
		```python
		@print_working
		def worker1():
		    print('我是一个勤劳的工作者！')
		
		@print_working
		def worker2():
		    print('我是一个勤劳的工作者！')
		
		@print_working
		def worker3():
		    print('我是一个勤劳的工作者！')
		worker1()
		worker2()
		worker3()
		```
	- 闭包（Closure）：一个函数定义中引用了函数外定义的变量，并且该函数可以在其定义环境外被执行。这样的一个函数我们称之为闭包。
		```python
		# 一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。
		
		def count():
		    fs = []
		    for i in range(1, 4):
		        def f():
		            # print(id(i))
		            return i*i
		        fs.append(f)
		    return fs
		
		f1, f2, f3 = count()
		print(f1())
		print(f2())
		print(f3())
		```

		输出：
		```
		9
		9
		9
		```

		
		```python
		def count():
		    def f(j):
		        def g():
		            # print(id(j))
		            return j*j
		        return g
		    fs = []
		    for i in range(1, 4):
		        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
		    return fs
		
		f1, f2, f3 = count()
		print(f1())
		print(f2())
		print(f3())
		```

		输出：
		```
		1
		4
		9
		```		
		- 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
		
## 模块（Module）
- import 语句：import module1[, module2[,... moduleN]]。调用模块中函数：模块名.函数名。
- from…import语句：from modname import name1[, name2[, ... nameN]]。
	- 一个模块只会被导入一次，不管你执行了多少次import。
- 安装/卸载：
	- pip install / uninstall
	- conda install / uninstall

&nbsp;

## 作业三：Python函数基础（大作业）
作业内容:

- 统计英语6级试题中所有单词的词频，并返回一个如下样式的字典
	{'and':100,'abandon':5}
- 英语6级试题的文件路径./artical.txt
- Tip: 读取文件的方法

	```python
	def get_artical(artical_path):
	    with open(artical_path) as fr:
	        data = fr.read()
	    return data
	
	get_artical('./artical.txt')
	```

处理要求:
- (a) '\n'是换行符 需要删除
- (b) 标点符号需要处理	['.', ',', '!', '?', ';', '\'', '\"', '/', '-', '(', ')']
- (c) 阿拉伯数字需要处理	['1','2','3','4','5','6','7','8','9','0'] 
- (d) 注意大小写 一些单词由于在句首，首字母大写了。需要把所有的单词转成小写	'String'.lower()
- (e) 高分项
通过自己查找资料学习正则表达式，并在代码中使用(re模块)
可参考资料：https://docs.python.org/3.7/library/re.html


```python
# 请根据处理要求下面区域完成代码的编写。
def get_artical(artical_path):
    with open(artical_path) as fr:
        data = fr.read()
    return data

# get_artical()为自定义函数，可用于读取指定位置的试题内容。
str_artical=get_artical('./artical.txt')
```

```python
import string
# 去除数字
from string import digits
str_digits = str_artical.translate(str.maketrans('', '', digits))

# 去除符号
from string import punctuation
str_punctuation = str_digits.translate(str.maketrans('', '', punctuation))

# 去除选项中ABCD字母（题目没要求，个人添加）
#str_question = str_punctuation.translate(str.maketrans('', '', 'ABCD'))

# 小写
str_lower=str_question.lower()

# 去除空字符，切片
str_spilt=str_lower.split()

# 打印词频列表
num_words = {}
for str_spilt in str_spilt:
     num_words[str_spilt] = num_words.get(str_spilt, 0) + 1
print(num_words)
```

```python
# 输出词频txt文本文件（题目没要求）
s = str(num_words)
f = open('dict.txt','w')
f.writelines(s)
f.close()
```

```python
# 词频查询（题目没要求）
str_spilt=str_lower.split()
word=input('输入要查询的单词的次数')
print(str_spilt.count(word))
```
