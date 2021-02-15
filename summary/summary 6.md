# 百度飞桨领航团零基础Python速成营 课程总结6
![paddlepaddle](https://paddlepaddle-org-cn.cdn.bcebos.com/paddle-site-front/favicon-128.png  "百度logo")

[课程链接](https://aistudio.baidu.com/aistudio/course/introduce/7073) `：https://aistudio.baidu.com/aistudio/course/introduce/7073`  
[飞桨官网](https://www.paddlepaddle.org.cn/)`：https://www.paddlepaddle.org.cn/`   
[推荐学习网站](https://www.runoob.com/python3/python3-tutorial.html)`：https://www.runoob.com/python3/python3-tutorial.html`

****
## 目录
* [文件处理模型](#文件处理模型)
* [Python基础](#Python基础)
* [作业一：Python编程基础](#作业一Python编程基础)

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

