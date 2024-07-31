class Phone:
    IMEI = None
    producer = None
    
    def call_4g(self):
        print('4')

class Phone2022(Phone):
    def call_5g(self):
        print('5')





# 多继承
class NFCReader:
    nfc_type = '5'
    producer = 'HM'

    def read(self):
        print('1')
    
class Control:
    def control(self):
        print('2')

class Myphone(NFCReader,Phone2022,Control):
    pass


p = Myphone()
p.call_4g()
p.control()

# 同名属性/方法 谁在左边，谁优先  =====class Myphone(NFCReader,Phone2022,Control):