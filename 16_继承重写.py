class Phone:
    IMEI = None
    producer = '222'
    
    def call_5g(self):
        print('5')


class Phone2022(Phone):
    producer = '111'
    def call_5g(self):
        # 通过super()方法调用父类的方法
        # super().call_5g()
        #父类名.成员方法(self)
        Phone.call_5g(self)
        print('6')

p = Phone2022()
p.call_5g()
print(p.producer)

