class student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        #self.msg=self.name+' got grade '+self.grade
    @property
    def msg(self):
        mg=self.name + ' got grade ' + self.grade
        return(mg)
    @msg.setter
    def msg(self,msg):
        sent=msg.split(" ")
        self.name=sent[0]
        self.grade=sent[-1]

st1=student('gopal','a')
st1.grade='b'
st1.msg='gopal got grade b'
print(st1.msg)