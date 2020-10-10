import pickle as pk

filename = "authkey.pkl"


class Readwrite:
    def read(self):
        load_list = []
        open_file = open(filename, "rb")
        try:
            load_list = pk.load(open_file)
        except EOFError:
            load_list = []

        open_file.close()
        return load_list

    def write(self, load_list):
        open_file = open(filename, "wb")
        pk.dump(load_list, open_file)
        open_file.close()