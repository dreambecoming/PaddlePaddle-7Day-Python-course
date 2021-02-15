# 百度飞桨领航团零基础Python速成营 课程总结4
![paddlepaddle](https://paddlepaddle-org-cn.cdn.bcebos.com/paddle-site-front/favicon-128.png  "百度logo")

[课程链接](https://aistudio.baidu.com/aistudio/course/introduce/7073) `：https://aistudio.baidu.com/aistudio/course/introduce/7073`  
[飞桨官网](https://www.paddlepaddle.org.cn/)`：https://www.paddlepaddle.org.cn/`   
[推荐学习网站](https://www.runoob.com/python3/python3-tutorial.html)`：https://www.runoob.com/python3/python3-tutorial.html`

****
## 目录
* [问题1：选取体育选手最好的三次成绩](#问题1选取体育选手最好的三次成绩)
  * 1.读取文件
  * 2.数据格式标准化
  * 3.排序去重
  * 4.简便方法

* [问题2：附带选手信息的最好的三次成绩](#问题2附带选手信息的最好的三次成绩)
  * 1.单一选手
  * 2.所有选手
  * 3.改进方法

* [引入类](#引入类)
  * 类
  * 类属性
  * 类方法
  * 类的私有属性和方法
* [作业四：Python面向对象(上)](#作业四Python面向对象上)
  * 第一题
  * 第二题
  * 第三题
  * 第四题
  * 第五题

# 课节4: Python面向对象(上)

## 问题1：选取体育选手最好的三次成绩
### 1. 读取文件
```python
# 读取文件内容，按逗号进行切分
def get_coach_data(filename):
    with open(filename) as f:
        line = f.readline()
    return line.strip().split(',')

# 输出读取文件的结果
times = get_coach_data('mywork/james.txt')
print('读取文件james.txt后的结果：\n')
print(times)
```
输出：
```
读取文件james.txt后的结果：

['2-34', '3:21', '2', '34', '2.45', '3.01', '2:01', '2:01', '3:10', '2-22']
```

get_coach_data函数的说明：

- filename为文件路径

- f表示文件对象

- f.realine()表示读取文件的一行

- line.strip().split(',')为链式函数写法意思是，先对这一行的数据进行strip()，就是去掉改行头尾空格和换行符。然后对strip()的结果进行split(',')，对结果以逗号的进行切分形成一个数组。

### 2. 数据格式标准化
```python
# 数据格式标准化
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins,secs) = time_string.split(splitter)
    return (mins+'.'+secs)
```

```python
# 输出数据格式标准化后的时间
james_times = get_coach_data('mywork/james.txt')
clean_james = []
for each_t in james_times:
    clean_james.append(sanitize(each_t))
print('输出james.txt标准化后的结果\n')
print(clean_james)
```
输出：
```
输出james.txt标准化后的结果

['2.34', '3.21', '2', '34', '2.45', '3.01', '2.01', '2.01', '3.10', '2.22']
```
sanitize函数的说明：

- time_string为时间数组

- splitter是根据原数据的格式来确实分钟和秒的分隔符

- (mins,secs) = time_string.split(splitter)以splitter分隔符切分每个时间数据到两个变量中mins,secs

- return (mins+'.'+secs)将分钟和秒以字符串点进行连接

### 3. 排序去重

```python
# 排序
sorted_james=sorted(clean_james)

# 去掉重复
unique_james = []
for each_t in sorted_james:
    if each_t not in unique_james:
        unique_james.append(each_t)

print('输出排序并去重后的结果，并取前3个数据\n')
print(unique_james[0:3])
```
输出：
```
输出排序并去重后的结果，并取前3个数据

['2', '2.01', '2.22']
```

### 4. 简便方法

```python
# python，一句话搞定数据标准化，排序和去重
james_times = get_coach_data('mywork/james.txt')
print('一句话搞定数据标准化、排序、去重\n')
print(sorted(set([sanitize(t) for t in james_times]))[0:3])
```

输出：
```
一句话搞定数据标准化、排序、去重

['2', '2.01', '2.22']
```

## 问题2：附带选手信息的最好的三次成绩
### 1. 单一选手
```python
# 读取新的数据文件，输出附带选手信息的最好的三次成绩
james_new = get_coach_data('mywork/james_new.txt')
(james_name,james_dob) = james_new.pop(0),james_new.pop(0)
james_top3 = sorted(set([sanitize(t) for t in james_new]))[0:3]
print('姓名：%s,生日：%s,最快的3次成绩：%s' %(james_name,james_dob,james_top3))
```

输出：
```
姓名：james,生日：2006-11-11,最快的3次成绩：['2.01', '2.22', '2.34']
```
### 2. 所有选手
```python
# 读取所有选手信息
james_new = get_coach_data('mywork/james_new.txt')
mikey_new = get_coach_data('mywork/mikey_new.txt')
julie_new = get_coach_data('mywork/julie_new.txt')
sarah_new = get_coach_data('mywork/sarah_new.txt')

# 输出输出附带选手信息的最好的三次成绩
(james_name,james_dob) = james_new.pop(0),james_new.pop(0)
james_top3 = sorted(set([sanitize(t) for t in james_new]))[0:3]

print('姓名：%s,生日：%s,最快的3次成绩：%s' %(james_name,james_dob,james_top3))

(mikey_name,mikey_dob) = mikey_new.pop(0),mikey_new.pop(0)
mikey_top3 = sorted(set([sanitize(t) for t in mikey_new]))[0:3]

print('姓名：%s,生日：%s,最快的3次成绩：%s' %(mikey_name,mikey_dob,mikey_top3))

(julie_name,julie_dob) = julie_new.pop(0),julie_new.pop(0)
julie_top3 = sorted(set([sanitize(t) for t in julie_new]))[0:3]

print('姓名：%s,生日：%s,最快的3次成绩：%s' %(julie_name,julie_dob,julie_top3))


(sarah_name,sarah_dob) = sarah_new.pop(0),sarah_new.pop(0)
sarah_top3 = sorted(set([sanitize(t) for t in sarah_new]))[0:3]

print('姓名：%s,生日：%s,最快的3次成绩：%s' %(sarah_name,sarah_dob,sarah_top3))
```
输出：
```
姓名：james,生日：2006-11-11,最快的3次成绩：['2.01', '2.22', '2.34']
姓名：mikey,生日：2003-9-10,最快的3次成绩：['2.22', '2.38', '2.49']
姓名：julie,生日：2006-5-9,最快的3次成绩：['2.11', '2.23', '2.59']
姓名：sarah,生日：2004-3-8,最快的3次成绩：['2.18', '2.25', '2.39']
```
### 3. 改进方法
使用字典来减少变量个数和代码量
```python
# 使用字典
james_new = get_coach_data('mywork/james_new.txt')

james_data={}

james_data['Name'] = james_new.pop(0)
james_data['Dob'] = james_new.pop(0)
james_data['top3'] = sorted(set([sanitize(t) for t in james_new]))[0:3]

print('姓名：%s,生日：%s,最快的3次成绩：%s' %(james_data['Name'],james_data['Dob'],james_data['top3']))
```
输出：
```
姓名：james,生日：2006-11-11,最快的3次成绩：['2.01', '2.22', '2.34']
```
## 引入类
### 类
- 定义类：
&nbsp;
class Athlete:

	- 第一部分：class定义类的关键字，Athlete符合python标识符命名规则，：表示类内容的开始
	def init(self,a_name,a_dob=None,a_times=[]):

	- 第二部分：def定义函数的关键字，init 方法是一个特殊方法会在实例化对象时自动调用，我们会在这个方法中对数据进行赋值。self作为类中函数的第一个参数，方便该方法调用该类的其他属性和方法。

	- 第三部分：自定义的属性和方法
	
&nbsp;

- 使用类 
	- 1.创建对象：对象名 = 类名(参数)

	- 2.使用.调用类的方法和属性：

		- 对象.属性名

		- 对象.方法名()
&nbsp;

-  使用类的优点：
	- 降低复杂性，提高可维护性。
	- 类可以将数据与函数绑定在一起，使代码模块化。
	- 调用数据和函数，使用对象名.的方式，使代码更加优雅。
&nbsp;

- 代码通常称为类的方法，数据通常称为类的属性，实例化的对象称为实例。


```python
# 定义类
class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return sorted(set([sanitize(t) for t in self.times]))[0:3]
        
    def sanitize(self,time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return (time_string)
        (mins,secs) = time_string.split(splitter)
        return (mins+'.'+secs)
```

```python
# 从文件中读取数据
def get_coach_data(filename):
    with open(filename) as f:
        line = f.readline()
    return line.strip().split(',')
    
james_new = get_coach_data('mywork/james_new.txt')
james_name = james_new.pop(0)
james_dob = james_new.pop(0)
james_times = james_new

# 创建Athlete对象
james = Athlete(james_name,james_dob,james_times)
print('姓名：%s,生日：%s,最快的3次成绩：%s' %(james.name,james.dob,james.top3()))
```
输出：
```
姓名：james,生日：2006-11-11,最快的3次成绩：['2.01', '2.22', '2.34']
```
### 类属性
- 所有对象共享的数据。
- 定义：在 init 之上，或者说在类的范围内与方法同等级别，书写变量名=值。
- 调用：类名.类属性

```python
class Athlete:

    #运动员集训了，要买东西的同学要把地址改一下
    address = '中国足球协会训练基地xx街xx号'

    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return sorted(set([self.sanitize(t) for t in self.times]))[0:3]
        
    def sanitize(self,time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return (time_string)
        (mins,secs) = time_string.split(splitter)
        return (mins+'.'+secs)
```

```python
julie_new = get_coach_data('mywork/julie_new.txt')
julie_name = julie_new.pop(0)
julie_dob = julie_new.pop(0)
julie_times = julie_new

james_new = get_coach_data('mywork/james_new.txt')
james_name = james_new.pop(0)
james_dob = james_new.pop(0)
james_times = james_new

julie = Athlete(julie_name,julie_dob,julie_times)
james = Athlete(james_name,james_dob,james_times)

#address地址共享
print(julie.address)
print(james.address)
print(Athlete.address)
```
输出：
```
中国足球协会训练基地xx街xx号
中国足球协会训练基地xx街xx号
中国足球协会训练基地xx街xx号
```

### 类方法
- 所有对象共享的方法
- 定义：方法定义时，使用@classmethod标记

- 调用：
	- 类名.类方法

	- 对象.类方法

```python
class Athlete:

    #运动员集训了，要买东西的同学要把地址改一下
    address = '中国足球协会训练基地xx街xx号'

    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return sorted(set([self.sanitize(t) for t in self.times]))[0:3]
        
    def sanitize(self,time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return (time_string)
        (mins,secs) = time_string.split(splitter)
        return (mins+'.'+secs)
    @classmethod
    def changeAddress(self):
        self.address = '中国田径训练基地xx街xx号'
```

```python
# 集训队换地方了
Athlete.changeAddress()
print(julie.address)
print(james.address)
print(Athlete.address)
```
输出：
```
中国足球协会训练基地xx街xx号
中国足球协会训练基地xx街xx号
中国田径训练基地xx街xx号
```
### 类的私有属性和方法


- 定义：在属性和方法名前加 __ 两个下划线。

- 调用：只能通过类中的方法来调用私有属性和方法。
```python
class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
    	# 私有name   
        self.__name = a_name
        self.dob = a_dob
        self.times = a_times
       
    def sayName(self):
        print(self.__name)
        
    def top3(self):
        return sorted(set([self.__sanitize(t) for t in self.times]))[0:3]
    
    # 私有sanitize()    
    def __sanitize(self,time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return (time_string)
        (mins,secs) = time_string.split(splitter)
        return (mins+'.'+secs)
```

```python
james = Athlete(james_name,james_dob,james_times)
# 分别去掉注释，进行测试
# print(james._name)
# james.__sanitize()
print('姓名：%s,生日：%s,最快的3次成绩：%s' %(james.name,james.dob,james.top3()))
```
分别输出：
```
AttributeError: 'Athlete' object has no attribute '_name'	以及：
AttributeError: 'Athlete' object has no attribute '__sanitize'
```
## 作业四：Python面向对象(上)
（注：此次作业代码皆取自课件，参考课件即可完成。）

作业内容:

### 第一题
'james,2006-11-11,2-34,3:21,2.34,2.45,3.01,2:01,2:01,3:10,2-22'

存储以上的数据，如何定义运动员类，补全代码（4分）

```python
class Athlete:  

    def __init__(self,a_name,a_dob=None,a_times=[]):  
    
		#代码1,通过传参的方式初始化name,dob,times三个属性值
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        #代码2,对times属性进行sanitize（统一化），去重和从小到大的排序操作，最后取最短的3个时间，并将结果返回
      return sorted(set([self.sanitize(t) for t in self.times]))[0:3]
        
    def sanitize(self,time_string):
      if '-' in time_string:            
        splitter = '-'        
      elif ':' in time_string:
        splitter = ':'        
      else:
         return (time_string)        
      (mins,secs) = time_string.split(splitter)        
      return (mins+'.'+secs)
```
### 第二题
数据所在文件的路径为'work/james_new.txt'，通过get_coach_data函数读取数据使用该数据初始化运动员对象，打印运动员对象的属性信息，补全代码。（4分）

```python
def get_coach_data(filename): 
    with open(filename) as f: 
        line = f.readline() 
    return line.strip().split(',')

james_new = get_coach_data('work/james_new.txt')
james_name = james_new.pop(0) 
james_dob = james_new.pop(0) 
james_times = james_new

#代码1，创建Athlete类的对象，将2个变量james_dob，james_times传递个构造方法，赋值给james
james = Athlete(james_name,james_dob,james_times)

#代码2，使用对象名.属性的方式，调用dob属性和top3方法
print('姓名：%s,生日：%s,最快的3次成绩：%s' %(james.name,james.dob,james.top3()))
```
输出：
```
姓名：james,生日：2006-11-11,最快的3次成绩：['2.01', '2.22', '2.34']
```
### 第三题
定义类属性address并赋值，定义类方法changeAddress改变address的值，补全代码。（4分）

```python
class Athlete:
    
    #代码1，定义address类属性变量，并进行赋值，值为'中国足球协会训练基地xx街xx号'
    address = '中国足球协会训练基地xx街xx号'

    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return sorted(set([self.sanitize(t) for t in self.times]))[0:3]
        
    def sanitize(self,time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return (time_string)
        (mins,secs) = time_string.split(splitter)
        return (mins+'.'+secs)
    #代码2，使用装饰器classmethod
    @classmethod
    #代码3，定义changeAddress函数，在函数内部对address类属性赋值为'中国田径训练基地xx街xx号'
    def changeAddress(self):
        self.address = '中国田径训练基地xx街xx号'
```
本题没要求验证，但可以使用下列代码进行验证：

```python
Athlete.changeAddress()
james = Athlete(james_name,james_dob,james_times)
print(james.address)
print(Athlete.address)
```

输出：
```
中国田径训练基地xx街xx号
中国田径训练基地xx街xx号
```
### 第四题
将第3题中的实例变量name改为私有的属性，将sanitize改为私有方法，补全代码。（4分）

```python
class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        #代码1，更改name为私有的属性，通过a_name对该属性赋值
        self.__name = a_name
        self.dob = a_dob
        self.times = a_times
       
    def sayName(self):
        #代码2，打印__name私有属性
        print(self.__name)
        
    def top3(self):
        #代码3，更改sanitize函数的定义为私有的方法，有一个参数，参数名为time_string
        return sorted(set([self.__sanitize(t) for t in self.times]))[0:3]

    def __sanitize(self,time_string):    
    #代码4
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return (time_string)
        (mins,secs) = time_string.split(splitter)
        return (mins+'.'+secs)
```
本题没要求验证，但可以使用下列代码进行验证：
```python
# 分别运行进行验证
james = Athlete(james_name,james_dob,james_times)
# print(james._name)
# james.__sanitize()
```
分别输出：
```
AttributeError: 'Athlete' object has no attribute '_name' 以及：
AttributeError: 'Athlete' object has no attribute '__sanitize'
```
### 第五题
数据内容为 'james,2006-11-11,2-34,3:21,2.34,2.45,3.01,2:01,2:01,3:10,2-22'
请以分钟.秒的形式（例如，'2.22'）打印'2-34'后面的所有时间，输出的结果为['2.34', '3.21', '2.34', '2.45', '3.01', '2.01', '2.01', '3.10', '2.22']的列表, 补全代码。（4分）

```python
data = 'james,2006-11-11,2-34,3:21,2.34,2.45,3.01,2:01,2:01,3:10,2-22'

def sanitize(time_string):
	#代码1
#判断每个时间的格式，例如2-34，如果包含'-'就赋值给splitter，如果包含'：'就赋值给splitter    
#如果不满足以上两种情况，则直接返回。对time_string以splitter切分形成(mins,secs)这种格式    
    if '-' in time_string:
            splitter = '-'
    elif ':' in time_string:
            splitter = ':'
    else:
        return (time_string)
    (mins,secs) = time_string.split(splitter)    
    return (mins+'.'+secs)
    
#代码2,对变量data以','进行切分，赋值给james

james = data.split(',')
name = james.pop(0)
dob = james.pop(0)
#代码3，使用列表推导的方式，对每个时间进行标准化，将最后的结果赋值给times
times = [sanitize(t) for t in james]
print(times)
```
输出：
```
['2.34', '3.21', '2.34', '2.45', '3.01', '2.01', '2.01', '3.10', '2.22']
```
