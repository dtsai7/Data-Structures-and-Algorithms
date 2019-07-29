class binarytree:
    def __init__(self, root):
        self.key = root
        self.leftchild = None
        self.rightchild = None

    def insertleft(self, newnode):
        if self.leftchild == None:
            self.leftchild = binarytree(newnode)
        else: 
            t = binarytree(newnode)
            t.leftchild, self.leftchild = self.leftchild, t
            # insert a node and push the existing child down one level in the tree

    def insertright(self, newnode):
        if self.rightchild == None:
            self.rightchild = binarytree(newnode)
        else:
            t = binarytree(newnode)
            t.rightchild, self.rightchild = self.rightchild, t

    def getleftchild(self):
        return self.leftchild

    def getrightchild(self):
        return self.rightchild

    def setrootval(self, val):
        self.key = val

    def getrootval(self):
        return self.key


t = binarytree('a')
t.insertleft('b')
t.insertright('c')
t.getrightchild().setrootval('hello')






