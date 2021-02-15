# 百度飞桨领航团零基础Python速成营 课程总结5
![paddlepaddle](https://paddlepaddle-org-cn.cdn.bcebos.com/paddle-site-front/favicon-128.png  "百度logo")

[课程链接](https://aistudio.baidu.com/aistudio/course/introduce/7073) `：https://aistudio.baidu.com/aistudio/course/introduce/7073`  
[飞桨官网](https://www.paddlepaddle.org.cn/)`：https://www.paddlepaddle.org.cn/`   
[推荐学习网站](https://www.runoob.com/python3/python3-tutorial.html)`：https://www.runoob.com/python3/python3-tutorial.html`

****
## 目录
* [继承](#继承)
* [方法重写](#方法重写)
* [多态](#多态)
* [多继承](#多继承)
* [模块化](#模块化)
* [作业五：Python面向对象(下)](#作业五Python面向对象下)
  * 第一题
  * 第二题
  * 第三题
  * 第四题
  
# 课节5：Python面向对象(下)

## 继承
- 定义：
&nbsp;
class 子类名(父类名)：

	- 情况1，如果子类有新增的属性，那么需要在子类__init方法中，调用父类的__init__

	- 情况2，如果子类没有新增的属性,子类不需要写__init__方法

- 使用：对象名 = 子类名(参数)
- 继承的好处：代码重用，升级功能（重写），新增功能（新的方法）
```python
# 读取文件
def get_coach_data(filename):
    with open(filename) as f:
        line = f.readline()
    return line.strip().split(',')
```

```python
#定义类
class Athlete:
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
#定义橄榄球员类
class Rugby(Athlete):
    def __init__(self,a_name,a_bod,a_squat,a_times):
        #调用父类__init__
        Athlete.__init__(self,a_name,a_bod,a_times)
        #深蹲次数
        self.squat = a_squat
    # 继承后下面两个函数就在Rugby类中，只是看不到而已
    # def top3(self):
    #     return sorted(set([self.sanitize(t) for t in self.times]))[0:3]
    # def sanitize(self,time_string):
    #     if '-' in time_string:
    #         splitter = '-'
    #     elif ':' in time_string:
    #         splitter = ':'
    #     else:
    #         return (time_string)
    #     (mins,secs) = time_string.split(splitter)
    #     return (mins+'.'+secs)
```

```python
loren = get_coach_data('mywork/loren.txt')
rugby = Rugby(loren.pop(0),loren.pop(0),loren.pop(0),loren)
print('姓名：%s,生日：%s,深蹲：%s个,最块的3次成绩：%s' %(rugby.name,rugby.dob,rugby.squat,rugby.top3()))
```
输出：
```
姓名：2011-11-3,生日：270,深蹲：3.59个,最块的3次成绩：['3.11', '3.23', '4.10']
```

## 方法重写
- 子类方法与父类方法完全相同，子类若重写了父类的方法，则子类对象调用方法时就是调用的自己类中重新的方法。
```python
# 例1 选取最慢3次
class Rugby(Athlete):
    def __init__(self,a_name,a_bod,a_squat,a_times):

        Athlete.__init__(self,a_name,a_bod,a_times)

        self.squat = a_squat
    def top3(self):
        return sorted([self.sanitize(t) for t in self.times])[-3:]
```

```python
loren = get_coach_data('mywork/loren.txt')
rugby = Rugby(loren.pop(0),loren.pop(0),loren.pop(0),loren)
print('姓名：%s,生日：%s,深蹲：%s个,最慢的3次成绩：%s' %(rugby.name,rugby.dob,rugby.squat,rugby.top3()))
```
输出：
```
姓名：2011-11-3,生日：270,深蹲：3.59个,最慢的3次成绩：['4.11', '4.21', '4.21']
```


```python
# 例2 其他运动员选取
class OtherAthlete(Athlete):
    def __init__(self,a_name,a_bod,a_squat,a_times):

        Athlete.__init__(self,a_name,a_bod,a_times)

        self.squat = a_squat
    def top3(self):
        return sorted([self.sanitize(t) for t in self.times])[0:3]
```

```python
mark = get_coach_data('mywork/mark.txt')
mark = OtherAthlete(mark.pop(0),mark.pop(0),mark.pop(0),mark)
print('姓名：%s,生日：%s,深蹲：%s个,最快的3次成绩：%s' %(mark.name,mark.dob,mark.squat,mark.top3()))
```
输出：
```
姓名：mark,生日：2010-2-4,深蹲：300个,最快的3次成绩：['3.11', '3.11', '3.23']
```

## 多态
- 多态性：一个事物多种形态
- 优点：减少重复代码，分离经常改变的代码与不经常改变的代码，使得代码可维护性提高。

方法重写：
```python
# 更多球员选取
mark1 = get_coach_data('mywork/mark.txt')
mark2 = get_coach_data('mywork/mark1.txt')
mark3 = get_coach_data('mywork/mark2.txt')


mark1 = OtherAthlete(mark1.pop(0),mark1.pop(0),mark1.pop(0),mark1)
mark2 = OtherAthlete(mark2.pop(0),mark2.pop(0),mark2.pop(0),mark2)
mark3 = OtherAthlete(mark3.pop(0),mark3.pop(0),mark3.pop(0),mark3)

print('姓名：%s,生日：%s,深蹲：%s个,最快的3次成绩：%s' %(mark1.name,mark1.dob,mark1.squat,mark1.top3()))
print('姓名：%s,生日：%s,深蹲：%s个,最快的3次成绩：%s' %(mark2.name,mark2.dob,mark2.squat,mark2.top3()))
print('姓名：%s,生日：%s,深蹲：%s个,最快的3次成绩：%s' %(mark3.name,mark3.dob,mark3.squat,mark3.top3()))
```
输出：
```
姓名：mark,生日：2010-2-4,深蹲：300个,最快的3次成绩：['3.11', '3.11', '3.23']
姓名：mark,生日：2010-2-4,深蹲：111个,最快的3次成绩：['3.11', '3.11', '3.23']
姓名：mark,生日：2010-2-4,深蹲：222个,最快的3次成绩：['3.11', '3.11', '3.23']
```

```python
loren = get_coach_data('mywork/loren.txt')
mark = get_coach_data('mywork/mark.txt')

loren = Rugby(loren.pop(0),loren.pop(0),loren.pop(0),loren)
mark = OtherAthlete(mark.pop(0),mark.pop(0),mark.pop(0),mark)

print(loren.name)
print(loren.dob)
print(loren.squat)
print(loren.top3())

print(mark.name)
print(mark.dob)
print(mark.squat)
print(mark.top3())
```
输出：
```
2011-11-3
270
3.59
['4.11', '4.21', '4.21']
mark
2010-2-4
300
['3.11', '3.11', '3.23']
```
使用多态：
```python
# 更多球员选取
loren = get_coach_data('mywork/loren.txt')
mark = get_coach_data('mywork/mark.txt')

loren = Rugby(loren.pop(0),loren.pop(0),loren.pop(0),loren)
mark = OtherAthlete(mark.pop(0),mark.pop(0),mark.pop(0),mark)

def print_rugby(athlete):

    print(athlete.name)
    print(athlete.dob)
    print(athlete.squat)
    print(athlete.top3())

print_rugby(loren)
print_rugby(mark)
```
输出：
```
2011-11-3
270
3.59
['4.11', '4.21', '4.21']
mark
2010-2-4
300
['3.11', '3.11', '3.23']
```

```python
#优化创建对象的代码

def obj_factory(name,filename):
    with open(filename) as f:
        line = f.readline()
    templ = line.strip().split(',')
    if name == 'r':
        return Rugby(templ.pop(0),templ.pop(0),templ.pop(0),templ)
    elif name == 'oa':
        return OtherAthlete(templ.pop(0),templ.pop(0),templ.pop(0),templ)

oa = obj_factory('oa','mywork/mark.txt')
print(oa.name)
```
```
输出：
mark
```
## 多继承

```python
class Father(): 
    def __init__(self):
        self.color = 'black'
    def talk(self):
        print("---爸爸的表达能力---")

class Mather():
    def __init__(self):
        self.height = 170
    def smart(self):
        print("---妈妈聪明的头脑---")

class Child(Father,Mather):
    def __init__(self):
        Father.__init__(self)
        Mather.__init__(self)

child1 = Child()
child1.talk()
child1.smart()
print(child1.color)
print(child1.height)
```
```
输出：
---爸爸的表达能力---
---妈妈聪明的头脑---
black
170
```

## 模块化
未完待续。。。







## 作业五：Python面向对象(下)
（注：此次作业代码皆取自课件，参考课件即可完成。）

作业内容:

### 第一题
定义Rugby为Athlete的子类，并增加子类自己的属性squat。（5分）
```python  
def get_coach_data(filename):
    with open(filename) as f:
        line = f.readline()
    return line.strip().split(',')
    
class Athlete:
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

#代码1，定义Rugby类继承Athlete
class Rugby(Athlete):
    def __init__(self,a_name,a_bod,a_squat,a_times):      
        #代码2，调用父类的构造方法，传递的参数为a_dob、a_times
        Athlete.__init__(self,a_name,a_bod,a_times)        
        #代码3，将a_squat赋值给类属性squat
        self.squat = a_squat
```
### 第二题
定义OtherAthlete类为Athlete类的子类，重写top3方法（允许重复的时间）。（5分）
```python
#代码1，定义OtherAthlete类继承Athlete
class OtherAthlete(Athlete):
    def __init__(self,a_name,a_bod,a_squat,a_times):
        Athlete.__init__(self,a_name,a_bod,a_times)

        self.squat = a_squat


    #代码2，定义无参数top3函数，对self.times属性应用统一化和排序功能
    def top3(self):
        return sorted([self.sanitize(t) for t in self.times])[0:3]
```
### 第三题
定义print_rugby函数，以多态的方式调用子类属性和方法。（5分）
```python
def get_coach_data(filename):
    with open(filename) as f:
        line = f.readline()
    return line.strip().split(',')
    
loren = get_coach_data('mywork/loren.txt')
mark = get_coach_data('mywork/mark.txt')

loren = Rugby(loren.pop(0),loren.pop(0),loren.pop(0),loren)
mark = OtherAthlete(mark.pop(0),mark.pop(0),mark.pop(0),mark)


def print_rugby(athlete):
    print(athlete.name)
    #代码1，打印athlete的属性dob、squat和top3方法的返回值
    print(athlete.dob)
    print(athlete.squat)
    print(athlete.top3())
    
#代码2，调用print_rugby函数，参数为loren
print_rugby(loren)
#代码3，调用print_rugby函数，参数为mark
print_rugby(mark)
```
输出：
```
loren
2011-11-3
270
['3.11', '3.23', '3.59']
mark
2010-2-4
300
['3.11', '3.11', '3.23']
```
### 第四题
有两个父类，一个Father，一个Mother，定义Child类共同继承这两个父类，子类调用父类的属性和方法 。（5分）
```python
class Father(): 
    def __init__(self):
        self.color = 'black'
    def talk(self):
        print("---爸爸的表达能力---")

class Mother():
    def __init__(self):
        self.height = 170
    def smart(self):
        print("---妈妈聪明的头脑---")

#代码1，定义Child类继承Father和Mother
class Child(Father,Mother):
    def __init__(self):
        #代码2，调用Mother类的的__init__方法
        Father.__init__(self)
        Mother.__init__(self)
#代码3，创建Child类的对象child,调用无参数的构造方法
child1 = Child()

#代码4，通过child调用父类的smart方法
child1.smart()

#代码5，通过child打印父类的color属性
print(child1.color)
```
输出：
```
---妈妈聪明的头脑---
black
```
