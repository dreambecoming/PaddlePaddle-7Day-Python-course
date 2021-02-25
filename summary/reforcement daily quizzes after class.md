# Python编程巩固

## 目录
* [第一天](#第一天)
    * [问题1](#问题1)
    * [问题2](#问题2)
    * [问题3](#问题3)
    * [问题4](#问题4)
    * [问题5](#问题5)
* [第二天](#第二天)
    * [问题1](#问题1-1)
    * [问题2](#问题2-1)
    * [问题3](#问题3-1)
    * [问题4](#问题4-1)
    * [问题5](#问题5-1)
 * [第三天](#第三天)
    * [问题1](#问题1-2)
    * [问题2](#问题2-2)
    * [问题3](#问题3-2)
    * [问题4](#问题4-2)
    * [问题5](#问题5-2)
    
## 第一天
***
### 问题1
编写一个程序，查找所有此类数字，这些数字可以被7整除，但不能是5的倍数，介于2000和3200之间（均包括在内）。所获得的数字应以逗号分隔的顺序打印在一行上。
***
自己尝试：
```python
#提示：考虑使用range（#begin，#end）方法
num=[];
for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        num.append(i)
print(num)
```
**参考答案**：
```python
#提示：考虑使用range（#begin，#end）方法
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))
```
总结：

* range() 函数前闭后开，[begin,end)，题目中应该是 range(2000,3201)
* 考虑 & 和 and 运算符的优先级
    ```python
    i= 2009
    print('i%7:',i%7)
    print('i%5:',i%5)
    
    print('i%7==0',i%7==0)
    print('i%5!=0',i%5!=0)
    
    #注意运算符先后顺序
    print('\n注意运算符先后顺序：\n')
    print('& 运算符',i%7==0 & i%5!=0)
    print('& 运算符加括号', (i%7==0) & (i%5!=0) )
    print('and 运算符',i%7==0 and i%5!=0)
    ```
    输出：
    ```python
    i%7: 0
    i%5: 4
    i%7==0 True
    i%5!=0 True
    
    注意运算符先后顺序：
    
    & 运算符 False
    & 运算符加括号 True
    and 运算符 True
    ```
* 列表打印在一行的功能十分特殊。
    * 列表元素输出：
     
    1. for循环输出。输出是竖向排列的，而我们往往需要水平输出。
        ```
        for i in [1,2,3]:
        print(i)
        ```
    2. for循环+分隔符输出。实现水平输出
        ```
        for i in [1,2,3]:
        print(i,end=',')
        ```
    3. join字符串形式输出。既实现了水平输出，又能在末尾不留分隔符，代码也比较精简。join其实是对列表进行了合并再输出。  
         ```print(" ".join(str(i) for i in [1,2,3]))```
         
***
### 问题2
编写一个程序，可以计算给定数字的阶乘。结果应以逗号分隔的顺序打印在一行上。

输入：8

输出：40320
***
自己尝试：
```python
#提示：如果将输入数据提供给问题，则应假定它是控制台输入
i=(input('输入所需计算阶乘的数字：\n'))
n=1
if eval(i)>0 and type(eval(i))==int:
    i=int(i)
    for i in range(1,i+1):
        n=n*i
    print(n)

else:
     print('请输入一个正整数')    
```
改进版：
```python
def fac():
    j=int(input('计算次数：'))
    list=[]

    while j>0:       
        i=(input('输入所需计算阶乘的数字：'))
        n=1
        if eval(i)>0 and type(eval(i))==int:
            i=int(i)
            for i in range(1,i+1):
                n=n*i
            print('阶乘是：%d'%n)      
        else:
            print('请输入一个正整数')
            n=None
        list.append(str(n))
        j=j-1
        print('总运算结果：'+','.join(str(n) for n in list))
fac()
```
输出：
```python
计算次数：3
输入所需计算阶乘的数字：-2
请输入一个正整数
总运算结果：None
输入所需计算阶乘的数字：4.5
请输入一个正整数
总运算结果：None,None
输入所需计算阶乘的数字：9
阶乘是：362880
总运算结果：None,None,362880
```
**参考答案**：
```python
#提示：如果将输入数据提供给问题，则应假定它是控制台输入
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))
```
总结：

* 网上找到了四种方法实现阶乘运算：

    第一种：普通的for循环
    ```python
    a = int(input('please inputer a integer:'))
    num = 1
    if a < 0:
        print('负数没有阶乘！')
    elif a == 0:
        print('0的阶乘为1！')
    else :
        for i in range(1,a + 1):
            num *= i
        print(num)
    ```
    第二种：reduce()函数
    ```python
    #从functools中调用reduce()函数
    from functools import reduce
    
    #使用lambda，匿名函数，迭代
    num = reduce(lambda x,y:x*y,range(1,7))
    print(num)
    ```
    第三种：factorial()函数
    ```python
    import math
    value = math.factorial(6)
    print(value)
    ```
    第四种：递归调用
    ```python
    def num(n):
        if n == 0:
            return 1
        else:
            return n * num(n - 1)
    
    print(num(6))
    ```
* python3 input()函数将输入都转为字符串str类型。先开始使用 int(input()) 会导致如果输入的浮点数float，例如8.5，相当于int('8.5')，会报错：ValueError: invalid literal for int() with base 10: '8.5'
    * 判断整数或者浮点数：
        1. 使用isinstance(i,float/int)判断：
        2. type(eval(s))==int/float判断
        3. 使用isdight()函数判断

***
### 问题3
使用给定的整数n，编写一个程序生成包含（i，i * i）的字典，该字典是介于1和n之间的整数（都包括在内），最后程序打印字典。

输入：8

输出：{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
***
自己尝试：
```python
#提示：如果将输入数据提供给问题，则应假定它是控制台输入。考虑使用dict（）
dic = {}
n=(input('输入正整数：'))
if eval(n)>0 and type(eval(n))==int:
    i=int(n)
    for i in range(1,i+1):
        dic.update({i:i*i})
    print(dic)      
else:
    print('请输入一个正整数')
    n=None
```
**参考答案**：
```python
#提示：如果将输入数据提供给问题，则应假定它是控制台输入。考虑使用dict（）
n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)
```
***
### 问题4
编写一个程序，该程序从控制台接受一个逗号分隔的数字序列，并生成一个包含每个数字的列表和元组。

输入：34,67,55,33,12,98

输出：['34', '67', '55', '33', '12', '98']('34', '67', '55', '33', '12', '98')
***
自己尝试：
```python
#提示：如果将输入数据提供给问题，则应假定它是控制台输入。tuple（）方法可以将列表转换为元组
n=(input('逗号分隔的数字序列：'))
print(n.split(','),tuple(n.split(',')))
```
**参考答案**：
```python
#提示：如果将输入数据提供给问题，则应假定它是控制台输入。tuple（）方法可以将列表转换为元组
values=input()
l=values.split(",")
t=tuple(l)
print(l)
print(t)
```
总结：

* 字符串 列表
    * 字符串转列表 str.split(" ")
    * 列表转字符串 (" ".join(l))
* 列表 元组
    * 列表转元组 tuple(列表)
    * 元组转列表 list(元组)

***
### 问题5
定义一个至少具有两个方法的类：

getString：从控制台输入中获取字符串

printString：以大写形式打印该字符串

需要编写简单的测试功能来测试类方法
***
参照答案写出：
```python
#提示：使用init方法构造一些​​参数
class Q5:
    def __init__(self):
        self.s=''
        
    def getString(self):
        self.s=input('请输入字符串：')
    
    def printString(self):
        print(self.s.upper())

q=Q5()
q.getString()
q.printString()
```
总结：

* class Studen(object),class 后接类名，**类名大写字母开头**，object为类的继承，没有合适的继承类用object类，这是所有类最终会继承的类
* 类的实例化：bart = student()

## 第二天
***
### 问题1
编写一个程序：接受连续的输入，当最终的输入为空时，程序终止运行，并将输入中的所有字符都大写之后打印。

输入：

Hello world Practice

Hello world Practice

输出：

HELLO WORLD PRACTICE

HELLO WORLD PRACTICE
***
自己尝试：
```python
#提示：控制台输入
lis=[]
while True:
    str=(input('请输入字符串，输入为空时程序结束运行'))
    print('字符串大写后：',str.upper())
    lis.append(str)
    if len(str) ==0:
        break
print('以逗号为间隔符输出总字符串：'+(','.join(lis)))
```
**参考答案**：
```python
#参考答案 输入3次：aaaaa；bbbbb；空
lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print(sentence)
```

***
### 问题2
编写一个程序：查找所有介于1000和3000之间的数字（包括1000和3000），以使该数字的每个数字均为偶数。所获得的数字应以逗号分隔的顺序打印在一行上。
***
自己尝试：
```python
#提示：包含1000和3000需要注意
#提示：包含1000和3000需要注意
lis=[]
for i in range(1000,3001):
    if i%2==0 and int(i/10)%2==0 and int(i/100)%2==0 and int(i/1000)%2==0:
        lis.append(str(i))

print('以逗号为间隔符输出：'+(','.join(lis)))
```
**参考答案**：
```python
#参考答案
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))
```

***
### 问题3
编写一个程序：接收字符串，并返回字符串中字母以及数字的数量。

举例：

输入：

hello world！123

输出：

字母：10

数字：3
***
自己尝试：
```python
#控制台输入
str=input('请输入字符串：')

num, char = 0, 0
for i in str:
    if i.isdigit():
        num = num + 1  
    elif i.isalpha():    
        char = char + 1
print('字母总数%d；数字总数%d'%(num,char))
```
**参考答案**：
```python
s = input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])
```
***
### 问题4
编写一个程序：输入一个数字列表,返回列表中平方为奇数的项。输入输出用,间隔。

举例:

输入：1,2,3,4,5,6,7,8,9

输出：1,3,5,7,9
***
自己尝试：
```python
#控制台输入
lis=[]
lis1=[]
str=input('请输入字符串数字列表，以逗号为间隔')
lis=str.split(",")

for i in lis:
    if eval(i)*eval(i) %2==1:
        lis1.append(i)
print('以逗号为间隔符输出：'+(','.join(lis1)))
```
**参考答案**：
```python
#参考答案
values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print(",".join(numbers))
```

***
### 问题5
定义一个可以接受两个字符串作为输入的函数，并在控制台中打印最大长度的字符串。如果两个字符串的长度相同，则该函数应逐行打印所有字符串。
***
自己尝试：
```python
#使用len（）函数获取字符串的长度
def strcon():
    str1=input('请输入字符串1')
    str2=input('请输入字符串2')
    if len(str1)>len(str2):
        print('字符串1：',str1)
    elif len(str1)<len(str2):
        print('字符串2：',str2)
    else:
        print('字符串1：',str1)
        print('字符串2：',str2)

strcon()
```
**参考答案**：
```python
def printValue(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1>len2:
        print(s1)
    elif len2>len1:
        print(s2)
    else:
        print(s1)
        print(s2)
        
printValue("one","three")
```
## 第三天
***
### 问题1
定义一个函数，该函数可以生成一个列表，其中值是介于1到20之间的数字的平方（包含1、20）。该函数需要打印列表中前5个元素以外的所有值。
***
自己尝试：
```python
#提示：使用**运算符可获取数字的幂。使用range（）进行循环。使用list.append（）将值添加到列表中。使用[n1：n2]分割列表
def q1():
    lis=[]
    for i in range(1,21):
        n=i**2
        lis.append(n)
    print(lis[5:])

q1()
```
**参考答案**：
```python
def printTuple():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(tuple(li))
		
printTuple()
```

***
### 问题2
编写程序：生成并打印一个元组，元组中的元素值为在给定元组（1,2,3,4,5,6,7,8,9,10）中其值为偶数的元素。
***
自己尝试：
```python
#提示：使用“ for”迭代元组使用tuple（）从列表中生成一个元组。
tup1=(1,2,3,4,5,6,7,8,9,10)
lis1=[]
for i in tup1:
    if i%2==0:
        lis1.append(i)
print(tuple(lis1))
```
**参考答案**：
```python
#参考答案
tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
	if i%2==0:
		li.append(i)

tp2=tuple(li)
print(tp2)
```

***
### 问题3
编写一个程序：该程序可以使用map（）创建一个列表，该列表的元素为1到20之间的数字平方（包含1、20）
***


**参考答案**：
```python
squaredNumbers = list(map(lambda x: x**2, range(1,21)))
print(squaredNumbers)
```
总结：

* map() 函数会根据提供的函数对指定序列做映射。  
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。  map(function, iterable, ...)

    答案中 range(1,21) 还是相当于一个序列。

* 匿名函数 lambda [arg1 [,arg2,.....argn]]:expression

注意区别：
```python
li = [lambda i:i**2 for i in range(1,21)]
print(type(li))      #<class 'list'>
print(type(li[0]))   #<class 'function'>
for i in li:
    print(i()) 
```
输出：
```python
<class 'list'>
<class 'function'>
400
400
400
400
400
400
400
400
400
400
400
400
400
400
400
400
400
400
400
400
```
```
解析：
li = [lambda :x for x in range(1,21)]
变成函数：
li = []
for x in range(10):
　　def fun():  #lambda中没有定义参数
　　　　return x
　　li.append(fun) #当函数还没有运行的时候，x已经为20了
```
***
### 问题4
定义一个名为Circle的类，该类以半径作为参数。Circle类具有一种可以计算面积的方法。
***

**参考答案**：
```python
#参考答案
values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print(",".join(numbers))
```

***
### 问题5
定义一个名为Shape的类及其子类Square。Square类具有一个init函数，该函数以长度作为参数。这两个类都有一个Area函数（计算面积公式：长乘以宽）。该函数可以打印Shape的面积默认为0。。
***
自己尝试：
```python
#要覆盖超类中的方法，我们可以在超类中定义一个具有相同名称的方法。
class Shape:
    def __init__(self,length=0,width=0):
        self.length=length
        self.width=width
       
    def Area(self):
        self.area=self.length*self.width
        return  self.area

class Square(Shape):
    def __init__(self,length=0,width=0):
        self.length=length
        self.width=width

s=Square(2.5,3.7)
s.Area()
```
**参考答案**：
```python
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print(aSquare.area())
```
总结：

* 使子类调用超类`__init__`方法：
```
class Subclass(Superclass):
    def __init__(self):
        Superclass.__init__(self) 
```
```
class Subclass(Superclass):
    def __init__(self):
        super(Subclass, self).__init__()
```
