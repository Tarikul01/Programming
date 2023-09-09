class HashMap:
    def __init__(self):
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX
    def add(self,key,val):
        h=self.get_hash(key)
        self.arr[h]=val
    def get(self,key):
        h=self.get_hash(key)
        return self.arr[h]
    def __setitem__(self, key, val):
        h=self.get_hash(key)
        self.arr[h]=val
    def __getitem__(self, item):
        h=self.get_hash(item)
        return self.arr[h]
    def __delitem__(self, key):
        h=self.get_hash(key)
        self.arr[h]=None


if __name__=="__main__":
    hm=HashMap()
    hm.add("march 9","saturday")
    hm["march 8"]="friday"
    print(hm.get("march 9"))
    print(hm["march 8"])