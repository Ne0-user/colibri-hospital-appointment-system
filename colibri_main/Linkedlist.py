class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    
    def set_data(self,data):
        self.__data=data

    def get_data(self):
        return self.__data
    
    def set_next(self,node):
        self.__next=node
    
    def get_next(self):
        return self.__next        

class LinkedList:
    def __init__(self,data=None):
        self.__head=None
        
        if data:
            try:
                for d in data:
                    self.add(d)
            except TypeError:
                self.add(data)
    
    def add(self,data):
        new_node=Node(data)
        
        if not self.__head:
            self.__head=new_node
            return
        
        current=self.__head
        while current.get_next():
            current=current.get_next()
        
        current.set_next(new_node)
        
    def invertir(self):
        current=self.__head
        prev=None
        
        while current is not None:
            next_node=current.get_next()
            current.set_next(prev)
            prev=current
            current=next_node
        
        self.__head=prev
    
    def copy(self):
        if not self.__head:
            print("None")
            return
        current=self.__head
        lista=[]
        
        while current:
            lista.append(current.get_data())
            current=current.get_next()
         
        new_linkedlist=LinkedList(lista)
            
        return new_linkedlist
    
    def devolver_nodo(self,n):
        if n <= 0 or n > self.size():
            return None
    
        self.invertir()
        current =self.__head
        
        for i in range(n-1):
            current=current.get_next()
        
        nodo_encontrado=current
        
        self.invertir()
        return nodo_encontrado
    
    def merge(self,linklist2):
        
        if not self.__head:
            self.__head=linklist2.__head
            return
        
        current=self.__head
        
        while current.get_next():
            current=current.get_next()
        
        current.set_next(linklist2.__head)
        
    
    def empty(self):
        if not self.__head:
            return True
        return False
        
    def size(self):
        current=self.__head
        tamano=0
        while current:
            tamano+=1
            current=current.get_next()
        
        return tamano
    
    def sort(self,reverse=False):
        if not self.__head or not self.__head.get_next():
            return
        
        lista=[]
        current=self.__head
        
        while current:
            lista.append(current.get_data())
            current=current.get_next()
        
        self.__quick_sort(lista,0,len(lista)-1)
        self.__head=None
        
        newlinklist=LinkedList(lista)
        self.__head=newlinklist.__head
        
        if reverse:
            self.invertir()
        
        return
        
    def __particion(self,lista,pivote,izq,der):
        i=izq-1
        
        for j in range(izq,der):
            
            if lista[j]<lista[pivote]:
                i+=1
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
        i+=1
        aux=lista[i]
        lista[i]=lista[pivote]
        lista[pivote]=aux
        return i
    
    def __quick_sort(self,lista,izq,der):
            
        if izq>=der:
            return
            
        piv=der
        p=self.__particion(lista, piv, izq, der)
        self.__quick_sort(lista, izq, p-1)
        self.__quick_sort(lista, p+1, der)    
    
    def eliminar_rep(self):
        if not self.__head:
            return
            
        current=self.__head
        vistos=[]
        prev=None
        
        while current:
            if current.get_data() in vistos:
                prev.set_next(current.get_next())
            
            else:
                vistos.append(current.get_data())
                prev=current
            
            current=current.get_next()
        
    def print_list(self):
        current=self.__head
        
        while current:
            print(current.get_data(),end="-->")
            current=current.get_next()
            
        print("None")

lista = LinkedList()
lista.add(55)
lista.add(19)
lista.add(21)
lista.add(20)
lista.add(5)
lista.add(11)
lista.add(22)
lista.invertir()
lista.print_list()
lista.copy()
linkedlist2=LinkedList([3,4,5,6])
lista.merge(linkedlist2)
lista.print_list()
lista.eliminar_rep()
lista.print_list()
print(lista.devolver_nodo(2).get_data())
lista.sort()
lista.print_list()