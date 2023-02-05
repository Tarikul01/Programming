class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def print_tree(self):
        print(self.data)
        for child in self.children:
            child.print_tree()


def build_product_tree():
    root=TreeNode("Electronics")
    laptop=TreeNode("Laptop")
    root.add_child(laptop)
    laptop.add_child(TreeNode("MAC"))

    Light=TreeNode("Light")
    Light.add_child(TreeNode("LED"))
    Light.add_child(TreeNode("Color Light"))
    root.add_child(Light)


    return root



if __name__=='__main__':
    root=build_product_tree()
    root.print_tree()
    pass