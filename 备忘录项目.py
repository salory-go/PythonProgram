# 用来调用函数time.sleep()使程序运行地不要太快
import  time
# 这下面的所有变量名都可以自行修改
# 定义一个事务类，属性有内容，重要性、紧急性
class thing:
    def __init__(self,content,imp,necess):
        self.content = content
        self.imp = imp
        self.necess = necess

# 定义一个待办类（可以理解为待办程序本身）
class daiban:
    # 属性有用户名和密码
    def __init__(self,userName,password):
        self.userName = userName
        # 这个__password就是私有属性（前面有两个下划线）
        self.__password = password
        # 定义一个列表来存储事务对象（因为有16件事务）
        # 因为技术原因（我很菜），所以使用列表来装对象，但是列表的内存不能为空，不然后面加入事务的时候会报错
        # 所以在就直接规定了列表的大小（4x4），并初始化了16个对象thing（“0”，0,0），初始化的本质就是for循环
        self.things =  [[thing('0',0,0) for col in range(4)] for row in range(4)]

    # 定义的私有方法
    def __setPassword(self,newPassword):
        self.__password = newPassword
    # 因为不能直接调用私有属性（比如self.userName），所以需要一个方法来间接调用，以及一个方法来更改属性
    # use用来判断调用密码的用处
    def passwordUse(self,use,password = None):
        if use == "get":
            return self.__password
        elif use == "set":
            self.__setPassword(password)

    # 加入事务方法
    def addT(self,content,imp,necess):
        # 如果此位置没有事务（0,0,0）就直接添加
        t = thing(content,imp,necess)
        if self.things[imp][necess].content=='0':
            self.things[imp][necess] = t
            # return直接就结束方法
            return
        # 否则判断是否替代此事务
        else:
            while True:
                choice = input("此位置已有一个待办，确定要替换掉它吗？(Y or N)")
                if choice in "Y" or "y":
                    self.things[imp][necess] = t
                    return
                elif choice in "N" or "n":
                    return
                else:
                    print("invalid input!")
    # 结束事务（将列表things的对应元素归0（0,0,0,））
    def finishT(self):
        name = input("Please input the thing's name:")
        for i in Daiban.things:
            for j in i:
                if name in j.content:
                    j.content = '0'
                    j.imp = 0
                    j.necess = 0
                    print("have finished")
                    return
        print("There is no thing as input")
    # 按照重要度优先紧急度次要的算法打印适合的处理事务的顺序
    # 比如有（0,1）（0,2）（2,0）三种事务，先打印（0,1）（0,2），在打印（2,0）
    def printList(self):
        # 定义一个bollen数据，判断是事务列表里是否有事务
        flag = True
        List =[]
        # 判断是否存在这个事务，存在即添加到列表，后续打印（如果不进行此操作直接打印事务列表的话就会有一堆0）
        for i in self.things:
            for j in i:
                if (j.content!='0'):
                    flag = False
                    List.append(j)
        if flag:
            print("There is no thing")
        else:
            print("We suggest that you can do things as this order")
            j=1
            # 循环打印事务
            for i in List:
                print(str(j)+"."+i.content)
                j+=1
            time.sleep(4)
    # 这是一个打印自己的函数
    # 如果这样调用repr("asd")
    # 则打印asd，所以我们需要设计一个打印自己的函数
    # 就打印用户名、密码和目前添加的事务（按照设定好的算法排序）
    # 此方法在后面未涉及
    def __repr__(self):
        user = self.userName+","+self.__password+"\n"
        a = ""
        for i in self.things:
            for j in i:
                if (j.content!='0'):
                    a+=j.content+"\n"
        return user+a
    def saveData(self):
        with open("daiban.txt",'w') as file:
            # 把用户名和密码单独提出来放在写入文件第一行
            username = self.userName
            password = str(self.__password)
            file.write(username+','+ password+'\n')
            # 将事务写入文件
            for i in self.things:
                for j in i:
                    file.write(str(j.content)+','+str(j.imp)+','+str(j.necess)+'\n')
print("loading......")

with open("daiban.txt", 'r') as f:
    # 读入一行数据，不要末尾的换行符（‘\n’）
    line = f.readline().rstrip('\n')
    user = line.split(',')

    # 把待办类对象实例化
    # 下面这个try语句是用来防止你的文件daiban.txt为空
    try:
        Daiban = daiban(user[0], user[1])
    except:
        # 如果文件为空就初始化实例，默认用户名为鸡腿，密码为123
        Daiban = daiban('jitui',123)
        Daiban.saveData()
    for i in range(16):
        # 把所有的事务对象实例化
        line = f.readline()
        t = line.split(',')
        Daiban.addT(t[0], int(t[1]), int(t[2]))


while True:
    # 调用函数打印用户名
    print("*" * 20 + "Welcome    " +Daiban.userName+ "*" * 20 + '\n\n')
    choice = input("Please input the password:")
    # 调用函数检测密码输入是否正确
    if choice in Daiban.passwordUse("get"):
        print("correct password!")
        break
    else:
        print("password wrongs")


while True:
    time.sleep(2)
    print('*'*45)
    print("{:^45}".format("1.add thing"))
    print("{:^45}".format("2.finish thing"))
    print("{:^45}".format("3.print things"))
    print("{:^45}".format("4.edit username"))
    print("{:^45}".format("5.edit password"))
    print("{:^45}".format("6.save data and exit"))
    print("{:^45}".format("7.help"))
    choice = input("\nplease input the number:")
    if choice=='1':
        print('*'* 45)
        print("input exit to exit")
        name = input("please input the thing's name")
        while name!="exit":
            imp = eval(input("please input the thing's importance class:"))
            necess = eval(input("please input the thing's emergency class:"))
            # 等级都只有0-3
            if imp > 3 or imp<0 or necess >3 or necess <0:
                print("the importance/emergency class is range from 0 to 3")
                continue
            Daiban.addT(name, imp, necess)
            name = input("please input the thing's name")
        print("success")
    elif choice=='2':
        print('*'* 45)
        Daiban.finishT()
    elif choice=='3':
        print('*'* 45)
        Daiban.printList()
    elif choice == '4':
        print('*' * 45)
        name = input("Please input new name:")
        Daiban.userName = name
    elif choice == '5':
        print('*' * 45)
        password = input("Please input new password:")
        # 这里是调用函数passwordUse来间接调用__setPassword函数
        Daiban.passwordUse("set",password)
    elif choice=='6':
        print('*'* 45)
        Daiban.saveData()
        print('*' * 20 + "see you" + '*' * 20)
        break
    elif choice == '7':
        print('*'* 45)
        print("""
            程序在不同的阶段可能会有几秒的停留时间，不是程序出错或者结束
            内置的daiban.txt文件不可以删除，否则程序无法运行
            用户可以通过菜单输入1进入事务添加功能，每个用户的事务不超过16个
            事务的基本属性有名字，重要等级，紧急等级。等级由0——3.等级越小优先级越高。
            可以修改密码和用户名
            """)