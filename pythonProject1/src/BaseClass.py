import configparser
class BaseClass:

    def getConfig(self, section, key):
        parser = configparser.ConfigParser()
        parser.read('D:\\application.conf')
        a= parser.get(section, key)
        return a


    @staticmethod
    def greet(name, item):
        print(f"Hello {name}, this is your {item}")

    a = 10
    b = 20
    def sum_num(self):
        return self.a+self.b
		
if __name__= "__main__"
	num= BaseClass()
	num.a= 10
	num.b= 12
	s= num.sum_num()
	#print(s)

	#num.greet("Kartik","Pen")
