# Create Employee class to have employee details
#     empid int
#     name str
#     designation str
#     salary int  --> make it private (hidden)
#     project_ids_assigned (set)
#     skills list of str
#     company name : 
#          shared in all employees

class employee:
    
    company_name = "EMV"
    def __init__(self,empid :int,name :str, desg : str, __sal :int, project_ids :set, skill :str):
        self.empid = empid
        self.name = name
        self.desg = desg
        self.__sal = __sal
        self.project_ids = project_ids
        self.skill = skill

    def print_info(self):
        print(self.empid,self.name,self.desg,self.__sal,self.project_ids,self.skill,self.company_name,sep=", ")
        print(type(1),type("ravi"),type("captain"),type(84929),type({4,1}),type("driving"))
e = employee(1,"ravi","captain",84929,{4,1},"driving")

e.print_info()




