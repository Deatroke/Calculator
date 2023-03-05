from tkinter import *
import tkinter as tk

class tela():
    def __init__(self):
        self.tela=tk.Tk()
        self.tela.title("Calculadora Tk")
        self.tela.resizable(width=False, height=False)

        self.Res=""
        self.Valores=0
        self.WIDTH=10
        self.HEIGHT=3
        self.FONTE="Arial 14 bold"


        #atualiza o display da tela
        def atualizar(auxBt):
            self.Res+=auxBt
            print(self.Res)
            self.auxResultado.set(self.Res)



        def calcular(self):
            Digitos=[]
            Oper=[]
            for i in self.Res:
                if i.isdigit():
                    Digitos.append(i)
                else:
                    Oper.append(i)
                    Digitos.append("*")
            print(Oper)
            print(Digitos)
            NumStr="".join(Digitos)
            NumStr=NumStr.split("*")
            print(NumStr)




            #operações
            if Oper[0]=="+":
                ResTotal=int(NumStr[0])+int(NumStr[1])



            if Oper[0]=="-":
                ResTotal=int(NumStr[0])-int(NumStr[1])



            if Oper[0]=="X":
                ResTotal=int(NumStr[0])*int(NumStr[1])



            if Oper[0]=="%":
                ResTotal=int(NumStr[0])/int(NumStr[1])



            self.auxResultado.set(str(ResTotal))
            self.Res=[]


        


        #label resultado - DISPLAY DA CALCULADORA
        self.auxResultado=tk.StringVar()
        self.auxResultado.set("")
        self.lbResultado=tk.Label(self.tela, textvariable=self.auxResultado, font=self.FONTE)
        self.lbResultado.grid(row=0, columnspan=5)

        #Botão 0
        self.auxBt0=tk.StringVar()
        self.auxBt0.set(0)
        self.bt0=tk.Button(self.tela, textvariable=self.auxBt0, width=self.WIDTH, height=self.HEIGHT, font=self.FONTE, command=lambda : atualizar(self.auxBt0.get()))
        self.bt0.grid(row=4, column=2, padx=2, pady=2)


        #Botão 1
        self.auxBt1=tk.StringVar()
        self.auxBt1.set(1)
        self.bt1=tk.Button(self.tela, textvariable=self.auxBt1, width=self.WIDTH, height=self.HEIGHT, font=self.FONTE, command=lambda : atualizar(self.auxBt1.get()))
        self.bt1.grid(row=1, column=1, padx=2, pady=2)


        #Botão 2
        self.auxBt2=tk.StringVar()
        self.auxBt2.set(2)
        self.bt2=tk.Button(self.tela, textvariable=self.auxBt2, width=self.WIDTH, height=self.HEIGHT, font=self.FONTE, command=lambda : atualizar(self.auxBt2.get()))
        self.bt2.grid(row=1, column=2, padx=2, pady=2)


        #Botão 3
        self.auxBt3=tk.StringVar()
        self.auxBt3.set(3)
        self.bt3=tk.Button(self.tela, textvariable=self.auxBt3, width=self.WIDTH, height=self.HEIGHT, font=self.FONTE, command=lambda : atualizar(self.auxBt3.get()))
        self.bt3.grid(row=1, column=3, padx=2, pady=2)


        #Botão 4
        self.auxBt4=tk.StringVar()
        self.auxBt4.set(4)
        self.bt4=tk.Button(self.tela, textvariable=self.auxBt4, width=self.WIDTH, height=self.HEIGHT, font=self.FONTE, command=lambda : atualizar(self.auxBt4.get()))
        self.bt4.grid(row=2, column=1, padx=2, pady=2)
        

        #Botão 5
        self.auxBt5=tk.StringVar()
        self.auxBt5.set(5)
        self.bt5=tk.Button(self.tela, textvariable=self.auxBt5, width=self.WIDTH, height=self.HEIGHT, font=self.FONTE, command=lambda : atualizar(self.auxBt5.get()))
        self.bt5.grid(row=2, column=2, padx=2, pady=2)

        
        #Botão 6
        self.auxBt6=tk.StringVar()
        self.auxBt6.set(6)
        self.bt6=tk.Button(self.tela, textvariable=self.auxBt6, width=self.WIDTH, height=self.HEIGHT, font=self.FONTE, command=lambda : atualizar(self.auxBt6.get()))
        self.bt6.grid(row=2, column=3, padx=2, pady=2)


        #Botão 7
        self.auxBt7=tk.StringVar()
        self.auxBt7.set(7)
        self.bt7=tk.Button(self.tela, textvariable=self.auxBt7, width=self.WIDTH, height=self.HEIGHT, font=self.FONTE, command=lambda : atualizar(self.auxBt7.get()))
        self.bt7.grid(row=3, column=1, padx=2, pady=2)


        #Botão 8
        self.auxBt8=tk.StringVar()
        self.auxBt8.set(8)
        self.bt8=tk.Button(self.tela, textvariable=self.auxBt8, width=self.WIDTH, height=self.HEIGHT, font=self.FONTE, command=lambda : atualizar(self.auxBt8.get()))
        self.bt8.grid(row=3, column=2, padx=2, pady=2)


        #Botão 9
        self.auxBt9=tk.StringVar()
        self.auxBt9.set(9)
        self.bt9=tk.Button(self.tela, textvariable=self.auxBt9, width=self.WIDTH, height=self.HEIGHT, font=self.FONTE, command=lambda : atualizar(self.auxBt9.get()))
        self.bt9.grid(row=3, column=3, padx=2, pady=2)


        #Botão -
        self.auxBt11=tk.StringVar()
        self.auxBt11.set("-")
        self.bt11=tk.Button(self.tela, textvariable=self.auxBt11, width=self.WIDTH, height=self.HEIGHT, bg= "light blue", font=self.FONTE, command=lambda : atualizar(self.auxBt11.get()))
        self.bt11.grid(row=2, column=4, padx=2, pady=2)


        #Botão +
        self.auxBt12=tk.StringVar()
        self.auxBt12.set("+")
        self.bt12=tk.Button(self.tela, textvariable=self.auxBt12, width=self.WIDTH, height=self.HEIGHT, bg= "light blue", font=self.FONTE, command=lambda : atualizar(self.auxBt12.get()))
        self.bt12.grid(row=1, column=4, padx=2, pady=2)


        #Botão *
        self.auxBt13=tk.StringVar()
        self.auxBt13.set("X")
        self.bt13=tk.Button(self.tela, textvariable=self.auxBt13, width=self.WIDTH, height=self.HEIGHT, bg= "light blue",font=self.FONTE, command=lambda : atualizar(self.auxBt13.get()))
        self.bt13.grid(row=3, column=4, padx=2, pady=2)


        #Botão /
        self.auxBt14=tk.StringVar()
        self.auxBt14.set("%")
        self.bt14=tk.Button(self.tela, textvariable=self.auxBt14, width=self.WIDTH, height=self.HEIGHT, bg= "light blue",font=self.FONTE, command=lambda : atualizar(self.auxBt14.get()))
        self.bt14.grid(row=4, column=4, padx=2, pady=2)


        #Botão =
        self.auxBt15=tk.StringVar()
        self.auxBt15.set("=")
        self.bt15=tk.Button(self.tela, textvariable=self.auxBt15, width=self.WIDTH, height=self.HEIGHT, bg= "#FED8B1", font=self.FONTE, command=lambda : calcular(self))
        self.bt15.grid(row=4, column=3, padx=2, pady=2)


        self.tela.mainloop()


tela()