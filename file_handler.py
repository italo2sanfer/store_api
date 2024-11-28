class FileHandler:

    url_pattern = "/home/dev/Workspace/store_api/"

    def __init__(self,object):
        self.object = object

    def get_line_add(self):
        list = []
        for chave, valor in self.object.__dict__.items():
            list.append(f'{chave}={valor}')
        return ";".join(list)+"\n"

    def get_by_line(self):
        print ("... Mounting line.")
        line_mount = self.get_line_add()
        print ("... Looking for existing line in file.")
        file = open(self.file, "r")
        line_finded = ""
        while len(line := file.readline()):
            if line==line_mount:
                print ("... Line found.")
                line_finded=line_mount
                break
        file.close()
        line_exists = (line_finded!="")
        return line_exists
    
    def add_in_file(self):
        if not self.get_by_line():
            print ("... adding line.")
            file = open(self.file, "a")
            file.write(self.get_line_add())
            file.close()    


class ProductFH(FileHandler):

    def __init__(self, object):
        super().__init__(object)
        self.file = self.url_pattern+"products.txt"