import Tkinter as tk
import random
root = tk.Tk ()
number = 0
ft = ('Times')
colors = ('#7FFF00', '#0000FF', '#8B008B',
          '#9ACD32', '#FF0000', '#DB7093',)
balls = []
photo1 = tk.PhotoImage(file="ball.gif")
photo2 = tk.PhotoImage(file="ball2.gif")

#Canvas-----------------------------------------------------------------
Mcanvas = tk.Canvas (root, width = 800, height = 800)
Mcanvas.pack ()

class ball:
    delay = 40
    damp = .90
    def update (self):
        self.x += self.vx
        self.y += self.vy
        self.vx += self.ax
        self.vy += self.ay

        canvasWidth = Mcanvas.winfo_width ()

        canvasHeight = Mcanvas.winfo_height()
        
        if self.y > canvasHeight - self.r:
            self.vy*= -self.damp
            self.y = canvasHeight - self.r
        if self.y < self.r:
            self.vy*= -self.damp
            self.y = self.r
        if self.x > canvasWidth - self.r:
            self.vx*= -self.damp
            self.x = canvasWidth - self.r
        if self.x < self.r:
            self.vx*= -self.damp
            self.x = self.r
            
        Mcanvas.coords(self.oval,
                      self.x - self.r,
                      self.y - self.r,
                      self.x + self.r,
                      self.y + self.r)
        #delete balls.
        if self.stop == False:
            root.after(ball.delay, self.update)
        else:
            Mcanvas.delete(self.oval)
            
    def __init__(self,x,y,vx,vy,ax,ay,r):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.r = r
        self.oval = Mcanvas.create_oval(self.x - self.r,
                                       self.y - self.r,
                                       self.x + self.r,
                                       self.y + self.r,
                                       fill= random.choice(colors),
                                       width = 1)
        self.stop = False
        

#button commands---------------------------------------------------------
def Add():
    myBall = ball (x=300,
                   y=50,
                   vx=10,
                   vy=0,
                   ax=0,
                   ay=1,
                   r=10)
    root.after(ball.delay, myBall.update)
    balls.append(myBall)
def Sub():
    balls[0].stop = True
    del balls[0]
def ran():
    myBall = ball (x=300,
                   y=150,
                   vx=10 + random.uniform(-20,20),
                   vy=0 + random.uniform(-20,20),
                   ax=0,
                   ay=1,
                   r=10)
    root.after(ball.delay, myBall.update)
    balls.append(myBall)

#buttons----------------------------------------------------------------
addButton = tk.Button (root, compound='bottom', image=photo1, text='ADD+1',
                       font=(ft), command=Add,
                       activebackground = 'red', background='#a52a2a')
addButton.place(relx=.3,
                rely=1,
                anchor='sw')
lessButton = tk.Button (root, compound='bottom', image=photo2, text = 'SUB-1',
                        font=(ft), command=Sub,
                        activebackground='red', background='#a52a2a')
lessButton.place(relx=.5,
                rely=1,
                anchor='s')
ranBall = tk.Button (root, compound='bottom' ,image=photo1, text='ADD+R',
                     font=(ft), command=ran,
                     activebackground='red', background='#a52a2a')
ranBall.place(relx=.7,
              rely=1,
              anchor='se')




tk.mainloop()
#ball = canvas.create_oval(10,10,20,20, fill="blue")
