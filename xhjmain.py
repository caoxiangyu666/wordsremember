#
import sys
import time
import datetime
import random
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_xhj(object):

    #次函数的功能为查看错题本
    def checkwrong(self):
        #界面设置
        Dialog6 = self.Dialog6
        Dialog6.setWindowTitle("错题本")
        layout6 = QtWidgets.QGridLayout(Dialog6)
        layout6.setSpacing(10)
        Dialog6.setGeometry(500, 300, 800, 500)

        #从错题文件中读取数据
        file = open("wrongs.txt", 'r')
        lines = file.readlines()

        cnt=0
        #表格布局和内容设置
        tablewidget = QtWidgets.QTableWidget(10, 4)
        tablewidget.setHorizontalHeaderLabels(['编号', '单词', '词性', '释义'])
        tablewidget.setColumnWidth(0, 40)
        tablewidget.setColumnWidth(1, 200)
        tablewidget.setColumnWidth(2, 200)
        tablewidget.setColumnWidth(3, 350)
        for line in lines:
            line = line.strip('\n')
            data = line.split(' ')
            words = data[1]
            words_real = data[2]
            words_mean = data[3]
            cnt = cnt + 1

            newItem = QtWidgets.QTableWidgetItem(str(cnt))
            tablewidget.setItem(cnt - 1, 0, newItem)
            newItem = QtWidgets.QTableWidgetItem(data[1])
            tablewidget.setItem(cnt - 1, 1, newItem)
            newItem = QtWidgets.QTableWidgetItem(data[2])
            tablewidget.setItem(cnt - 1, 2, newItem)
            newItem = QtWidgets.QTableWidgetItem(data[3])
            tablewidget.setItem(cnt - 1, 3, newItem)
        layout6.addWidget(tablewidget, 0, 0, 10, 10)
        Dialog6.setLayout(layout6)
        #界面展示
        Dialog6.show()


    #此函数的功能为重做题目，也就是把做题界面的输入框置空
    def redo(self):
        self.question1line.setText('')
        self.question2line.setText('')
        self.question3line.setText('')
        self.question4line.setText('')
        self.question5line.setText('')
        self.question6line.setText('')
        self.question7line.setText('')
        self.question8line.setText('')
        self.question9line.setText('')
        self.question10line.setText('')
        reply = QtWidgets.QMessageBox.about(self.Dialog, '重置答案','重置成功！再次测试吧~')

    #次函数的功能为检查答题正确性并计算，给出数据，并将错题存入错题本
    def checkans(self):
        if self.choice == QtWidgets.QMessageBox.Yes:  # 2
            userans = []
            wrongcount = 0
            wrongproblems = []
            wrongnum = []
            userans.append(self.question1line.text().strip(' '))
            userans.append(self.question2line.text().strip(' '))
            userans.append(self.question3line.text().strip(' '))
            userans.append(self.question4line.text().strip(' '))
            userans.append(self.question5line.text().strip(' '))
            userans.append(self.question6line.text().strip(' '))
            userans.append(self.question7line.text().strip(' '))
            userans.append(self.question8line.text().strip(' '))
            userans.append(self.question9line.text().strip(' '))
            userans.append(self.question10line.text().strip(' '))
            for i in range(10):
                if userans[i] == self.results[i]:
                    pass
                else:
                    wrongcount = wrongcount + 1
                    wrongproblems.append(str(i + 1) + '. ' + self.problems[i])
                    wrongnum.append(i + 1)

            lastscore = 10 - wrongcount
            lastscore = 10 * lastscore
            if lastscore < 100:
                fd = open('wrongs.txt', 'w+')
                for wrongproblem in wrongproblems:


                    fd.write('%s\n' % (wrongproblem.strip('\n')))
                fd.close()
                reply = QtWidgets.QMessageBox.about(self.Dialog, '成绩',
                                                    '您做错了 %d 题，得分为 %d 分，错题已保存至错题本' % (wrongcount, lastscore))
            else:
                reply = QtWidgets.QMessageBox.about(self.Dialog, '成绩', 'TQL TQL TQL')

        else:  # 4
            userans=[]
            wrongcount = 0
            wrongproblems= []
            wrongnum =[]
            userans.append(self.question1line.text().strip(' '))
            userans.append(self.question2line.text().strip(' '))
            userans.append(self.question3line.text().strip(' '))
            userans.append(self.question4line.text().strip(' '))
            userans.append(self.question5line.text().strip(' '))
            userans.append(self.question6line.text().strip(' '))
            userans.append(self.question7line.text().strip(' '))
            userans.append(self.question8line.text().strip(' '))
            userans.append(self.question9line.text().strip(' '))
            userans.append(self.question10line.text().strip(' '))
            for i in range(10):
                if userans[i] ==self.results[i]:
                    pass
                else:
                    wrongcount=wrongcount+1
                    wrongproblems.append(str(i+1)+'. '+self.problems[i])
                    wrongnum.append(i+1)

            lastscore = 10 - wrongcount
            lastscore= 10*lastscore
            if lastscore < 100:
                fd = open('wrongs.txt','w+')
                for wrongproblem in wrongproblems:
                    fd.write('%s\n'%(wrongproblem.strip('\n')))
                fd.close()
                reply = QtWidgets.QMessageBox.about(self.Dialog, '成绩', '您做错了 %d 题，得分为 %d 分，错题已保存至错题本'%(wrongcount,lastscore))
            else:
                reply = QtWidgets.QMessageBox.about(self.Dialog, '成绩', 'TQL TQL TQL')





    #这是做题功能的主界面
    def spellword(self,choice):
        count=0
        file= open('wordlist.txt','r', encoding='UTF-8')
        self.lines = file.readlines()
        rand =[]
        self.problems=[]
        asks=[]
        self.results=[]
        self.wrongselect=[]
        #self.rightans=[]
        #self.rightans2=[]
        self.choice=choice

        #从题库随机抽取题目
        for i in range(10):

            ran=random.randint(1,len(self.lines))

            if ran not in rand:

                rand.append(ran)
            else:
                rand.append(random.randint(1,len(self.lines)))



        #如果选择了选择题
        if choice == QtWidgets.QMessageBox.Yes:  # 2
            for ran in rand:
                self.problems.append(self.lines[ran - 1])
            for i in range(10):
                ask = self.problems[i].strip('\n')
                ass = ask.split(' ')

                randwrong = []
                for k in range(3):
                    randa1 = random.randint(1,len(self.lines))
                    while ass[0] in self.lines[randa1-1]:
                        randa1 = random.randint(1,len(self.lines))
                    wr = self.lines[randa1-1]
                    wr1= wr.strip('\n')
                    wr2 = wr1.split(' ')

                    randwrong.append(wr2[1]+' '+wr2[2])
                other = ''
                randtrue = random.randint(1,4)
                if randtrue ==1:
                    final = '%d.%s   '%(i+1,ass[0])+'A.'+ass[1]+ass[2]+' '+ 'B.'+randwrong[0]+' '+ 'C.'+randwrong[1]+' '+ 'D.'+randwrong[2]
                    asks.append(final)
                    self.results.append('A')
                if randtrue == 3:
                    final = '%d.%s   '%(i+1,ass[0])+'A.' + randwrong[1] + ' ' + 'B.' + randwrong[0] + ' ' + 'C.' + ass[1] + ass[2] + ' ' + 'D.' + randwrong[2]
                    asks.append(final)
                    self.results.append('C')
                if randtrue == 2:
                    final = '%d.%s   '%(i+1,ass[0])+'A.' + randwrong[0] + ' ' + 'B.' + ass[1] + ass[2] + ' ' + 'C.' + randwrong[
                        1] + ' ' + 'D.' + randwrong[2]
                    asks.append(final)
                    self.results.append('B')
                if randtrue ==4:
                    final = '%d.%s   '%(i+1,ass[0])+'A.'+randwrong[2]+' '+ 'B.'+randwrong[0]+' '+ 'C.'+randwrong[1]+' '+ 'D.'+ass[1]+ass[2]
                    asks.append(final)
                    self.results.append('D')

        #如果选择了拼写题
        else:  # 4
            for ran in rand:
                self.problems.append(self.lines[ran - 1])

            for i in range(10):
                ask = self.problems[i].strip('\n')
                ass = ask.split(' ')
                asks.append(ass[1]+'  ' +ass[2])
                self.results.append(ass[0])





        #做题界面设置
        Dialog4=self.Dialog4
        if choice == QtWidgets.QMessageBox.Yes:  # 2
            Dialog4.setWindowTitle("选择题")
        else:
            Dialog4.setWindowTitle("拼写题")
        layout4 = QtWidgets.QGridLayout(Dialog4)
        layout4.setSpacing(15)
        Dialog4.setGeometry(200, 200, 800, 800)

        redolable = QtWidgets.QPushButton("重做")
        checkresultlable = QtWidgets.QPushButton("提交答案")
        checkwrongs = QtWidgets.QPushButton("查看错题")

        redolable.clicked.connect(self.redo)
        checkresultlable.clicked.connect(self.checkans)
        checkwrongs.clicked.connect(self.checkwrong)


        self.question1line = QtWidgets.QLineEdit("请填写答案")
        self.question2line = QtWidgets.QLineEdit("请填写答案")
        self.question3line = QtWidgets.QLineEdit("请填写答案")
        self.question4line = QtWidgets.QLineEdit("请填写答案")
        self.question5line = QtWidgets.QLineEdit("请填写答案")
        self.question6line = QtWidgets.QLineEdit("请填写答案")
        self.question7line = QtWidgets.QLineEdit("请填写答案")
        self.question8line = QtWidgets.QLineEdit("请填写答案")
        self.question9line = QtWidgets.QLineEdit("请填写答案")
        self.question10line = QtWidgets.QLineEdit("请填写答案")


        if choice == QtWidgets.QMessageBox.Yes:  # 2

            question1lable = QtWidgets.QLabel(asks[0])
            question2lable = QtWidgets.QLabel(asks[1])
            question3lable = QtWidgets.QLabel(asks[2])
            question4lable = QtWidgets.QLabel(asks[3])
            question5lable = QtWidgets.QLabel(asks[4])
            question6lable = QtWidgets.QLabel(asks[5])
            question7lable = QtWidgets.QLabel(asks[6])
            question8lable = QtWidgets.QLabel(asks[7])
            question9lable = QtWidgets.QLabel(asks[8])
            question10lable = QtWidgets.QLabel(asks[9])
        else:  # 4
            question1lable = QtWidgets.QLabel(asks[0])
            question2lable = QtWidgets.QLabel(asks[1])
            question3lable = QtWidgets.QLabel(asks[2])
            question4lable = QtWidgets.QLabel(asks[3])
            question5lable = QtWidgets.QLabel(asks[4])
            question6lable = QtWidgets.QLabel(asks[5])
            question7lable = QtWidgets.QLabel(asks[6])
            question8lable = QtWidgets.QLabel(asks[7])
            question9lable = QtWidgets.QLabel(asks[8])
            question10lable = QtWidgets.QLabel(asks[9])
        #界面布局设置
        layout4.addWidget(redolable,1,1,1,3)
        layout4.addWidget(checkresultlable,1,5,1,3)
        layout4.addWidget(checkwrongs,1,9,1,3)
        layout4.addWidget(question1lable,2,1,1,9)
        layout4.addWidget(self.question1line,2,13,1,3)
        layout4.addWidget(question2lable, 3, 1, 1, 9)
        layout4.addWidget(self.question2line, 3, 13, 1, 3)
        layout4.addWidget(question3lable, 4, 1, 1, 9)
        layout4.addWidget(self.question3line, 4, 13, 1, 3)
        layout4.addWidget(question4lable, 5, 1, 1, 9)
        layout4.addWidget(self.question4line, 5, 13, 1, 3)
        layout4.addWidget(question5lable, 6, 1, 1, 9)
        layout4.addWidget(self.question5line, 6, 13, 1, 3)
        layout4.addWidget(question6lable, 7, 1, 1, 9)
        layout4.addWidget(self.question6line, 7, 13, 1, 3)
        layout4.addWidget(question7lable, 8, 1, 1, 9)
        layout4.addWidget(self.question7line, 8, 13, 1, 3)
        layout4.addWidget(question8lable, 9, 1, 1, 9)
        layout4.addWidget(self.question8line, 9, 13, 1, 3)
        layout4.addWidget(question9lable, 10, 1, 1, 9)
        layout4.addWidget(self.question9line, 10, 13, 1, 3)
        layout4.addWidget(question10lable, 11, 1, 1, 9)
        layout4.addWidget(self.question10line, 11, 13, 1, 3)
        #展示界面
        Dialog4.setLayout(layout4)
        Dialog4.show()












    #此函数为点击开始测试后的题型选择框
    def bgtest(self):

        choice = QtWidgets.QMessageBox.question(self.Dialog4, '开始做题', '想做选择题吗，想做选择题就按yes，想做拼写就按no',
                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)  # 1

        if choice == QtWidgets.QMessageBox.Yes:  # 2
            self.spellword(choice)
        elif choice == QtWidgets.QMessageBox.No:  # 4

            self.spellword(choice)




    #此函数为单词本编辑的增加记录功能
    def addword(self):
        file= open('wordlist.txt','r', encoding='UTF-8')
        lines =file.readlines()
        file.close()
        words=[]
        for line in lines:
            line=line.strip('\n')
            words.append(line)
        newwords= self.addline.text()
        new = newwords.split(' ')
        if len(new)!=3:
            reply = QtWidgets.QMessageBox.about(self.Dialog,'警告','数据格式错误')
        else:
            words.append(newwords)
            print(len(words))
            fn=open('wordlist.txt','w+', encoding='UTF-8')
            for word in words:
                fn.write('%s\n'%word)

            fn.close()
            reply = QtWidgets.QMessageBox.about(self.Dialog, '成功', '数据增加成功~')



    #次函数的功能为单词本编辑的删除记录功能
    def deleteword(self):
        count=0
        file= open('wordlist.txt','r', encoding='UTF-8')
        lines = file.readlines()
        words = []
        deleteline=self.deleteline.text()
        print(deleteline)
        print(type(deleteline))
        deleteline=int(deleteline)
        for line in lines:
            line=line.strip('\n')
            words.append(line)
        words.pop(deleteline-1)
        fn = open('wordlist.txt', 'w+', encoding='UTF-8')
        for word in words:
            fn.write('%s\n' % word)
        reply = QtWidgets.QMessageBox.about(self.Dialog, '成功', '数据删除成功~')

    # 次函数的功能为单词本编辑的保存修改功能
    def saveword(self):
        rows=self.row
        words=[]
        for row in range(rows):
            str1 = self.tablewidget.item(row,1).text()
            str2 = self.tablewidget.item(row, 2).text()
            str3 = self.tablewidget.item(row, 3).text()
            str = str1+' '+str2+' '+str3
            words.append(str)
        fn = open('wordlist.txt', 'w+', encoding='UTF-8')
        for word in words:
            fn.write('%s\n' % word)
        reply = QtWidgets.QMessageBox.about(self.Dialog, '成功', '保存数据成功~')




    #单词本编辑的主界面
    def wordlists(self):
        #界面设置
        self.Dialog3.setWindowTitle("词汇表")
        self.layout3 = QtWidgets.QGridLayout(self.Dialog3)
        self.layout3.setSpacing(10)
        self.Dialog3.setGeometry(600, 200, 800, 800)

        self.addlable = QtWidgets.QPushButton("增加记录")
        self.deletelable = QtWidgets.QPushButton("删除记录")
        self.savelable = QtWidgets.QPushButton("保存修改")

        self.addlable.clicked.connect(self.addword)
        self.deletelable.clicked.connect(self.deleteword)
        self.savelable.clicked.connect(self.saveword)

        self.addline = QtWidgets.QLineEdit("Ex:dog n 狗,犬")
        self.deleteline = QtWidgets.QLineEdit("Ex:5(输入的数字即为想要删除的行号)")
        #读取单词表
        file= open("wordlist.txt",'r', encoding='UTF-8')
        lines = file.readlines()
        self.row = len(lines)
        cnt=0
        self.tablewidget = QtWidgets.QTableWidget(self.row,4)
        self.tablewidget.setHorizontalHeaderLabels(['编号','单词','词性','释义'])
        self.tablewidget.setColumnWidth(0,40)
        self.tablewidget.setColumnWidth(1, 200)
        self.tablewidget.setColumnWidth(2, 200)
        self.tablewidget.setColumnWidth(3, 350)
        #数据填入
        for line in lines:
            line = line.strip('\n')
            data = line.split(' ')
            words = data[0]
            words_real = data[1]
            words_mean = data[2]
            cnt = cnt+1

            newItem=QtWidgets.QTableWidgetItem(str(cnt))
            self.tablewidget.setItem(cnt-1,0,newItem)
            newItem = QtWidgets.QTableWidgetItem(data[0])
            self.tablewidget.setItem(cnt - 1, 1, newItem)
            newItem = QtWidgets.QTableWidgetItem(data[1])
            self.tablewidget.setItem(cnt - 1, 2, newItem)
            newItem = QtWidgets.QTableWidgetItem(data[2])
            self.tablewidget.setItem(cnt - 1, 3, newItem)
        #界面布局
        self.layout3.addWidget(self.addlable,1,0,1,1)
        self.layout3.addWidget(self.addline,1,1,1,1)
        self.layout3.addWidget(self.deletelable,2,0,1,1)
        self.layout3.addWidget(self.deleteline,2,1,1,1)
        self.layout3.addWidget(self.savelable,3,0,1,1)
        self.layout3.addWidget(self.tablewidget,4,0,5,10)
        #界面展示
        self.Dialog3.setLayout(self.layout3)
        self.Dialog3.show()











    #此函数为欢迎界面的签到功能实现
    def signon(self):
        #查看今天的日期，防止重复签到
        today = datetime.date.today()
        time = str(today.year)+'-'+str(today.month)+'-'+str(today.day)
        usrfile_r = open('users.txt', 'r')

        userlines_r = usrfile_r.readlines()
        user_inf_new = []
        for lines in userlines_r:
            user_info = lines.strip('\n')
            user_inf = user_info.split(' ')
            if self.login_username == user_inf[0]:
                last_signon = str(user_inf[4])
                signon_count = int(user_inf[5])
                if last_signon==time:
                    reply = QtWidgets.QMessageBox.about(self.Dialog,'签到失败','您今天已经签到过啦~您已经签到了 %s 次了:)'%user_inf[5])
                    user_inf_new.append(user_info)
                else:
                    user_inf[4]=time
                    user_inf[5]=signon_count+1
                    inf = user_inf[0]+' '+user_inf[1]+' '+user_inf[2]+' '+user_inf[3]+' '+str(user_inf[4])+' '+str(user_inf[5])+' '+str(user_inf[6])+' '+str(user_inf[7])
                    user_inf_new.append(inf)
                    reply = QtWidgets.QMessageBox.about(self.Dialog, '签到成功', '签到成功啦~您已经签到了 %s 次了:)' %str(user_inf[5]))
            else:
                user_inf_new.append(user_info)
        print(user_inf_new)
        usrfile_w = open('users.txt', 'w+')
        for infos in user_inf_new:
            usrfile_w.write('%s\n'%infos)




    #欢迎界面
    def setupUi2(self,registusername):

        self.Dialog2.setWindowTitle("欢迎您~"+registusername)
        layout = QtWidgets.QGridLayout(self.Dialog2)
        layout.setSpacing(10)
        self.Dialog2.setGeometry(200, 100, 800, 800)
        #三个功能按钮
        self.signonbtn  = QtWidgets.QPushButton('打卡签到')
        self.testbtn = QtWidgets.QPushButton('开始测试')
        self.wordslist = QtWidgets.QPushButton('单词本编辑')
        #3界面布局
        layout.addWidget(self.signonbtn, 1, 0,2,1)
        layout.addWidget(self.testbtn, 4, 0,2,1)
        layout.addWidget(self.wordslist, 7, 0,2,1)
        self.signonbtn.clicked.connect(self.signon)
        self.wordslist.clicked.connect(self.wordlists)
        self.testbtn.clicked.connect(self.bgtest)
        #界面展示
        self.Dialog2.setLayout(layout)
        self.Dialog2.show()

    #此函数为登录界面的登录功能实现
    def login(self):
        count = 0
        userfile = open('users.txt', 'r')
        registusername = self.nameLineEdit.text()
        registpassword = self.sexLineEdit.text()
        registphone = self.phoneLineEdit.text()
        registmail = self.mailEdit.text()
        userslines = userfile.readlines()
        userfile.close()
        for user_info in userslines:
            user_info=user_info.strip('\n')
            user_inf = user_info.split(' ')
            username = user_inf[0]
            password = user_inf[1]

            if registusername==username and registpassword==password :
                count=count+1
                self.login_username = username
                reply = QtWidgets.QMessageBox.about(self.Dialog,'nb','登录成功~')
                break
        if count==0:

            reply = QtWidgets.QMessageBox.about(self.Dialog, '您输的啥？', '登录失败~')
        else:
            self.Dialog.close()
            self.setupUi2(registusername)

    #此函数为登录界面的注册功能实现
    def registe(self):
        count = 0
        userfile = open('users.txt','r')
        registusername = self.nameLineEdit.text()
        registpassword = self.sexLineEdit.text()
        registphone = self.phoneLineEdit.text()
        registmail = self.mailEdit.text()
        userslines = userfile.readlines()
        userfile.close()
        for user_info in userslines:
            user_info=user_info.strip('\n')
            user_inf = user_info.split(' ')
            username = user_inf[0]
            password = user_inf[1]
            phone = user_inf[2]
            mail = user_inf[3]
            if registusername==username or registpassword==password or registphone==phone or registmail==mail:
                count=count+1
                reply = QtWidgets.QMessageBox.about(self.Dialog,'警告','你号没了~')
                break
        if count==0:
            regist_userfile = open('users.txt','a')
            write_info = registusername+' '+registpassword+' '+registphone+' '+registmail+' '+'0'+' '+'0'+' '+'0'+' '+'0'
            regist_userfile.write('%s\n'%write_info)
            regist_userfile.close()
            reply = QtWidgets.QMessageBox.about(self.Dialog,'Congratulations','你号有了~')






    #登录界面
    def setupUi(self,Dialog,Dialog2,Dialog3,Dialog4,Dialog5,Dialog6):
        self.Dialog=Dialog
        self.Dialog2=Dialog2
        self.Dialog3= Dialog3
        self.Dialog4=Dialog4
        self.Dialog5=Dialog5
        self.Dialog6=Dialog6
        self.Dialog.setWindowTitle("Remember Words")
        layout = QtWidgets.QGridLayout(self.Dialog)
        self.Dialog.setGeometry(600, 200, 400, 400)

        #四个框
        nameLabel = QtWidgets.QLabel("用户名")
        self.nameLineEdit = QtWidgets.QLineEdit("")
        sexLabel = QtWidgets.QLabel("密码")
        self.sexLineEdit = QtWidgets.QLineEdit("")
        emitLabel = QtWidgets.QLabel("手机号")
        self.phoneLineEdit = QtWidgets.QLineEdit("")
        timeLabel = QtWidgets.QLabel("邮箱")
        self.mailEdit = QtWidgets.QLineEdit("")
        # layout.setSpacing(10)
        #四个输入框
        layout.addWidget(nameLabel, 1, 0)
        layout.addWidget(self.nameLineEdit, 1, 1)
        layout.addWidget(sexLabel, 2, 0)
        layout.addWidget(self.sexLineEdit, 2, 1)
        layout.addWidget(emitLabel, 3, 0)
        layout.addWidget(self.phoneLineEdit, 3, 1)
        layout.addWidget(timeLabel, 4, 0)
        layout.addWidget(self.mailEdit, 4, 1)
        layout.setColumnStretch(1, 20)
        #两个功能按钮
        self.save_Btn = QtWidgets.QPushButton('登录')
        self.cancle_Btn = QtWidgets.QPushButton('注册')
        self.cancle_Btn.clicked.connect(self.registe)
        self.save_Btn.clicked.connect(self.login)
        layout.addWidget(self.save_Btn,5,2)
        layout.addWidget(self.cancle_Btn,5,3)
        #界面展示
        self.Dialog.setLayout(layout)
        self.Dialog.show()









if __name__ == "__main__":
    import sys
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    Dialog2= QtWidgets.QDialog()
    Dialog3= QtWidgets.QTableWidget()
    Dialog4 = QtWidgets.QDialog()
    Dialog5 = QtWidgets.QDialog()
    Dialog6 = QtWidgets.QDialog()
    ui = Ui_xhj()
    #主程序运行
    ui.setupUi(Dialog,Dialog2,Dialog3,Dialog4,Dialog5,Dialog6)

    sys.exit(app.exec_())