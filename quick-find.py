'''
Project: Sample code for QUICK-FIND
Author: Murali Krishna
'''
import os

class Unionfind:
    id=[]
    node1=None
    node2=None
    def __init__(self,max):
        self.id=[]
        for i in range(0,max):
            self.id.append(i)
    def getNodes(self):
        self.node1 = int(input("Enter first node: "))
        self.node2 = int(input("Enter second node: "))
    def connected(self):
        self.getNodes()
        if (self.id[self.node1] == self.id[self.node2]):
            return True
        else:
            return False
    def union(self):
        if(self.connected()):
            return True
        else:
            temp=self.id[self.node1]
            self.id[self.node1]=self.id[self.node2]
            for i in range(0,len(self.id)):
                if(self.id[i]==temp):
                    self.id[i]=self.id[self.node1]
        print("ID: {0}".format(self.id))
        return True


def main():
    max=int(input("Enter the number of nodes: "))
    uf=Unionfind(max)
    userContinue=True
    while(userContinue):
        selection=int(input("Which operation would you like to perform\n1.Connected\n2.Union: "))
        method={
            1:"connected",
            2:"union"
        }
        returnValue=getattr(uf ,method[selection])()
        print "Connected" if returnValue else "Not connected"
        value=str(raw_input("Wish to continue? [Yes/No]: "))
        userContinue=True if (((value).rstrip(os.linesep).lower()) in ["yes"]) else False

if __name__ == '__main__':
    main()
