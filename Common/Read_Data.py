import yaml
import os


class Read_Data:
    def __init__(self, file_name):
        """
         使用pytest运行在项目的根目录下运行，即App_Project目录
         期望路径为：项目所在目录/App_Project/Data/file_name
        """
        self.file_path = os.getcwd() + os.sep + "Data" + os.sep + file_name

    def return_data(self):
        with open(self.file_path, 'r') as f:
            # 读取文件内容
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data