import sys,os,yaml
class data_opt:
    def __init__(self,filename):
        self.filepath = os.getcwd() + os.sep + "data" + os.sep + filename
    def read_yaml(self):
        with open(self.filepath,'r') as f:
            return yaml.load(f)
    def write_yaml(self,data):
        with open(self.filepath,'w') as f:
            return yaml.dump(data,f)
def get_data():
    datalist = []
    data = data_opt("data.yaml").read_yaml().get('Logindata')
    for i in data:
        for o in i.keys():
            datalist.append((o,i.get(o).get('uid'),i.get(o).get('pwd'),i.get(o).get('except_result')))
    return datalist



