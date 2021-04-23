#-*- coding:utf-8 -*-

class Pilha():
    def constrói():
        a = [3, -55, '1kdsa', 'ort94', 4, -492, 332]
        
        i = 6
        while(i>=0):
            print(a[i])
            i = i - 1
            
        print("")
        a.append("5fkl59")
        print("Empilhando")
        print("")
        
        i = 7
        while(i>=0):
            print(a[i])
            i = i - 1
        
        print("")
        a.append(10)
        print("Empilhando")
        print("")
        
        i = 8
        while(i>=0):
            print(a[i])
            i = i - 1
            
        print("")
        a.pop()
        print("Desempilhando")
        print("")     
        
        i = 7
        while(i>=0):
            print(a[i])
            i = i - 1
        
        print("")
        a.pop()
        print("Desempilhando")
        print("")   
        
        i = 6
        while(i>=0):
            print(a[i])
            i = i - 1
        
        print("")
        a.pop()
        print("Desempilhando")
        print("")   
        
        i = 5
        while(i>=0):
            print(a[i])
            i = i - 1
        

        

p = Pilha
p.constrói()
input()