import json
import random
from pymongo import MongoClient
client = MongoClient('localhost',27017)
collection = client['driver']['test']

class DriverTest():
    def __init__(self,num):
        self.num = num
        self.client = MongoClient('localhost',27017)
        self.collection = client['driver']['test']
        self.test = list(collection.find())

    def ready_test(self):
        print('你可以通过以下程序来练习科目一驾考题目\n'
              '本次考试一共{}道题，答对一道加一分，答错不扣分\n'
              '如果你想中途退出请按c键'.format(self.num))
        start = input('如果你准备好开始答题请按Y键：')
        return start

    def start_test(self):
        answer_dict = {'16':'1','32':'2','64':'3','128':'4'}
        index = 1
        score = 0
        while index != self.num:
            print('第{}题：'.format(index))
            #随机出题
            exercises = random.choice(self.test)
            #打印图片
            if exercises['page_url'] != '':
                print(exercises['page_url'])
            #打印问题
            print(exercises['question'])
            #打印选项
            for key,value in exercises['option'].items():
                print(key+':'+value)
            #用户选项
            user_choice = input('请输入选项前面的序号，按回车键结束：')
            #题目选项
            allow_choice = [i for i in exercises['option']]
            #合法选项
            allow_choice.append('c')
            #判断输入
            while user_choice not in allow_choice:
                choice = input('输入有误，请输入选项前面的序号，按回车键结束:')
            if user_choice == answer_dict[str(exercises['answer'])]:
                print('回答正确')
                score += 1
                index += 1
            elif user_choice == 'c':
                break
            else:
                print('回答错误，正确答案为{}'.format(answer_dict[str(exercises['answer'])]))
                index += 1
        print('本次一共回答{}道题\n回答正确{}道\n总分为{}分'.format(index-1,score,score))

if __name__ == '__main__':
    driver = DriverTest(100)
    if driver.ready_test() in ['y','Y']:
        driver.start_test()







