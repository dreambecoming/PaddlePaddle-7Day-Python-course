# 百度飞桨领航团零基础Python速成营 课程总结6
![paddlepaddle](https://paddlepaddle-org-cn.cdn.bcebos.com/paddle-site-front/favicon-128.png  "百度logo")

[课程链接](https://aistudio.baidu.com/aistudio/course/introduce/7073) `：https://aistudio.baidu.com/aistudio/course/introduce/7073`  
[飞桨官网](https://www.paddlepaddle.org.cn/)`：https://www.paddlepaddle.org.cn/`   
[推荐学习网站](https://www.runoob.com/python3/python3-tutorial.html)`：https://www.runoob.com/python3/python3-tutorial.html`

****
## 目录
* [文件处理模型](#文件处理模型)
* [文件常用函数](#文件常用函数)
* [JSON(JavaScript Object Notation)](#JSONJavaScript Object Notation)
* [OS文件/目录](#OS文件目录)
* [作业五：大作业](#作业五大作业)

# 课节6：文件操作及常用模块使用

  * 输入，处理，输出。

    输入：读取4个队员的训练数据，读取4个文件

      ```
      james.txt 2-34,3:21,2,34,2.45,3.01,2:01,2:01,3:10,2-22

      sarah.txt 2:58,2.58,2:39,2-25,2:55,2:54,2.18,2:55,2:55

      julie.txt 2.59,2.11,2:11,2:23,3-10,2-23,3:10,3.21,3-21

     mikey.txt 2:22,3.01,3:01,3.02,3:02,3.02,3:22,2.49,2:38
     ```

    处理：标准化数据，切分数据，top3（最快的3个时间）

    输出：将每个人的信息打印在屏幕上显示

## 文件处理模型
```python
# 读取每行数据
f = open('work/train_data_cor.txt')
for line in f:
    print(line)
f.close()
```
输出：
```
james,2004-5-21,2.34,3:21,2.34,2.45,3.01,2:01,2:01,3:10,2-22

julie,2006-5-9,2.59,2.11,2:11,2:23,3-10,2-23,3:10,3.21,3-21

sarah,2004-3-8,2:58,2.58,2:39,2-25,2-55,2:54,2.18,2:55,2:55

mikey,2003-9-10,2:22,3.01,3:01,3.02,3:02,3.02,3:22,2.49,2:38
```
数据出现问题
```python
f = open('work/train_data_wrg.txt')
for line in f:
    data = line.strip().split(',')

    print('姓名：'+data.pop(0)+'生日：'+data.pop(0)+'时间：'+str(data))
f.close()
```
输出：
```
recent call last)<ipython-input-4-a51a9349f79f> in <module>
      3     data = line.strip().split(',')
      4 
----> 5     print('姓名：'+data.pop(0)+'生日：'+data.pop(0)+'时间：'+str(data))
      6 f.close()
IndexError: pop from empty list
```
解决方法：
1.使用异常
```python
#使用异常
with open('work/train_data_wrg.txt') as f:
    for line in f:
        data = line.strip().split(',')
        try:
            print('姓名：'+data.pop(0)+'生日：'+data.pop(0)+'时间：'+str(data))
        except:
            pass
```
2.代码判断
```python
#代码判断
with open('work/train_data_wrg.txt') as f:
    for line in f:
        data = line.strip().split(',')
        if len(data) != 1:
            print('姓名：'+data.pop(0)+'生日：'+data.pop(0)+'时间：'+str(data))
```

正确输出：
```
姓名：james生日：2004-5-21时间：['2.34', '3:21', '2.34', '2.45', '3.01', '2:01', '2:01', '3:10', '2-22']
姓名：julie生日：2006-5-9时间：['2.59', '2.11', '2:11', '2:23', '3-10', '2-23', '3:10', '3.21', '3-21']
姓名：sarah生日：2004-3-8时间：['2:58', '2.58', '2:39', '2-25', '2-55', '2:54', '2.18', '2:55', '2:55']
姓名：mikey生日：2003-9-10时间：['2:22', '3.01', '3:01', '3.02', '3:02', '3.02', '3:22', '2.49', '2:38']
```


## 文件常用函数
 文件打开关闭：
  * open() 函数：打开文件。file object = open(file_name [, access_mode][, buffering])
  * close() 函数：关闭文件。fileObject.close()  
 
 文件读写
  * read() 函数：用于从文件读取指定的字节数。fileObject.read([size])
   参数size：从文件中读取的字节数，默认为 -1，表示读取整个文件。
  * readline() 函数：用于从文件读取整行，包括 "\n" 字符。fileObject.readline(size)
  * write() 函数：将任何字符串写入一个打开的文件。fileObject.write(string)  
  
 文件定位：
  * seek() 函数：用于移动文件读取指针到指定位置。fileObject.seek(offset[, whence])
    参数offset：开始的偏移量，也就是代表需要移动偏移的字节数。whence：可选，默认值为 0。表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
  * tell() 函数： 返回文件的当前位置，即文件指针当前位置。fileObject.tell()
 
## JSON(JavaScript Object Notation) 
导入 json 库：import json
json()函数：
 * json.dumps	将 Python 对象编码成 JSON 字符串。
 * json.loads	将已编码的 JSON 字符串解码为 Python 对象。
 * json.dump 将数据写入json文件中。
 * json.load 把文件打开，并把字符串变换为数据类型。
 * 不带s的用于操作文件，带s的用于数据类型的转换。 
 
 表1. python 类型 json 类型转化对照表
 | Python      |      JSON      | 
	|:-----------:| :-------------:|
	| dict     	  |   object       |
	|list, tuple  |     array      |
 |str, unicode |     string     |
 |int, long, float  |     number    |
 |  True       |    true        |
 |  False       |    false      |
 |  None       |    null        |
 
 ```python
 # dumps，python字典转json字符串
 import json
class Athlete(json.JSONEncoder):
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


with open('work/train_data_cor.txt') as f:
    data = f.readline().strip().split(',')
    ath = Athlete(data.pop(0),data.pop(0),data)
    print(ath)
    
# dumps数据转化
ath_json = json.dumps(ath.__dict__)
# 字典
print(ath.__dict__)
# json 字符串
print(ath_json)
 ```
 输出：
 ```
 <__main__.Athlete object at 0x7f19d5064dd0>
{'name': 'james', 'dob': '2004-5-21', 'times': ['2.34', '3:21', '2.34', '2.45', '3.01', '2:01', '2:01', '3:10', '2-22']}
{"name": "james", "dob": "2004-5-21", "times": ["2.34", "3:21", "2.34", "2.45", "3.01", "2:01", "2:01", "3:10", "2-22"]}
 ```
 
 ```python
 # dump，保存json到文件
 with open('work/json.txt','w') as f:
    json.dump(ath_json,f)
 ```
  ```python
 # load，读取json文件内容
with open('work/json.txt') as f:
    ath = json.load(f)
    print(ath)
 ```
 输出：
 ```
 {"name": "james", "dob": "2004-5-21", "times": ["2.34", "3:21", "2.34", "2.45", "3.01", "2:01", "2:01", "3:10", "2-22"]}
 ```
 ## OS文件/目录
 * os.getcwd() 函数：用于返回当前工作目录。
 * os.chdir() 函数：用于改变当前工作目录到指定的路径。os.chdir(path)
 * os.mkdir() 函数：用于以数字权限模式创建目录。默认的模式为 0777 (八进制)。os.mkdir(path[, mode])
 * os.listdir(path) 函数：返回path指定的文件夹包含的文件或文件夹的名字的列表。
 * os.system() 函数：将字符串转化成命令在服务器上运行。  
 path模块：from pathlib import Path
 * os.path.abspath(path)	函数：返回绝对路径。
 * os.path.exists(path)		函数：如果路径 path 存在，返回 True；如果路径 path 不存在，返回 False。
 * os.path.isdir(path) 函数：	判断路径是否为目录。

 ```python
 import os
#返回当前工作目录
current_path = os.getcwd()
print('当前路径：'+current_path)
 ```
  输出：
 ```
 当前路径：/home/aistudio
 ```
 
 ```python
#改变当前工作目录
os.chdir('/home/aistudio/work')
#运行mkdir命令
os.system('mkdir today')
 ```
  输出：
 ```
 0
 ```
 
  ```python
from pathlib import Path
#返回当前绝对路径
abs_path = os.path.abspath('')
print('abs_path：'+abs_path)
#路径是否存在
Path(abs_path).exists()
 ```
  输出：
 ```
 abs_path：/home/aistudio/work
True
 ```
 
  ```python
print('当前路径：'+os.getcwd())
listdir = os.listdir()
#返回当前路径下文件和文件夹名
print(listdir)
 ```
  输出：
 ```
 当前路径：/home/aistudio/work
['json.txt', 'train_data_cor.txt', 'athlete.py', 'data.txt', 'train_data_wrg.txt', 'today']
 ```
 
  ```python
#是否为文件夹
os.path.isdir('/home/aistudio/work/today')
 ```
  输出：
 ```
True
 ```
 
 ## 作业五：大作业

作业内容:

### 第一题
数据如下：

stu1.txt 孙同学,2020-5-21,20,'男',77,56,77,76,92,58,-91,84,69,-91
stu2.txt 赵同学,2020-11-3,24,'女',65,68,72,95,-81,71,86,91,57,91
stu3.txt 王同学,2021-8-7,25,'男',87,78,90,-76,88,47,100,65,69,100 
stu4.txt 李同学,2021-8-10,29,'男',92,54,85,71,-91,68,77,68,95,95
以上四个txt文档在work路径下可以找到。

定义Student类，包括name、dob、age、gender和score属性，包括top3方法用来返回学生的最大的3个成绩（可重复）、sanitize方法用来将负的分数变为正的分数，负的分数可能是输入错误。声明stu_list对象组数用于存储所有的学生对象。最后输出所有的学生信息包括姓名、生日、年龄、性别、最高的3个分数。

第一题的输出结果如下，供参考：
！[输出参考结果](https://ai-studio-static-online.cdn.bcebos.com/2a1b5032bcc740b6a681e50497c2b94452f39a624a044ccd9718d2edd1269b06)
### 第二题
数据格式如下：

stu5.txt 特长同学,2020-10-5,20,'男',180,87,98,77,76,92,58,-76,84,69,-47
stu6.txt 特长同学,2020-10-6,20,'女',230,76,48,82,88,92,58,-91,84,69,-68
以上两个txt文档在work路径下可以找到。

定义Spostudent、Artstudent为Student的子类，在子类的属性里面新增了spe为特长分数。Spostudent包括的top3方法返回的是最低的3个得分（可重复），Artstudent包括top3方法返回的是最高的3个得分（可重复），最后使用多态的方式输出2个特长同学的姓名、生日、年龄、性别、分数、特长分。

第二题的输出结果如下，供参考：
！[输出参考结果](https://ai-studio-static-online.cdn.bcebos.com/585b454f8c2f45e1a08dc9a7fc7c017c596974c8ca91449298c2b72f88c99a03)
