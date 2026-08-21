import turtle


tela = turtle.Screen()
tela.setup(width=600, height=600)
tela.title('Minha janela')
tela.bgcolor("pink")

#-------bola---------------------------

bola = turtle.Turtle()
bola.shape('circle')
bola.color('purple')
bola.speed(0)
bola.dy = -2
#-------------movimento-------------------------
gravidade = 0.5

while True:
    bola.dy -= gravidade
    bola.sety(bola.ycor() + bola.dy)

    #check for a bounce
    if bola.ycor() < -300:
        bola.dy *= -1









tela.mainloop()

