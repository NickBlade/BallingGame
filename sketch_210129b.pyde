x = 500
y = 810
h = 1024
w = 840
ballX = 100
ballY = 50
speedY = 0
g = -0.3
speedX = 5
score = 0
difficulty = 1
scaleLarge = 400
gameOver = False

        
def setup():
    size(h, w)


def draw():
    global x, y, h, w, gameOver

    restartgame()
    
    if gameOver == False:
        if keyPressed:
            if(keyCode == RIGHT):
                x += 15
            elif(keyCode == LEFT):
                x -= 15
                
            if scaleLarge == 400 and x>600:
                x = 600
            elif scaleLarge == 200 and x>840:
                x = 840
                
            if (x<30):
                x = 30
                
        background(0) #Background negro
        noCursor() #Eliminar mouse
        rect(x, y, scaleLarge, 10) #Dibujar cuadrado    
        
        ball_move()
         
def restartgame():
    global x, y, h, w, ballX, ballY, speedY, g, speedX, score, difficulty, scaleLarge, gameOver
    
    if keyPressed:
        if gameOver == True:
            if(key == 'r' or key == 'R'):
                x = 500
                y = 810
                h = 1024
                w = 840
                ballX = 100
                ballY = 50
                speedY = 0
                g = -0.3
                speedX = 5
                score = 0
                difficulty = 1
                scaleLarge = 400
                gameOver = False
            
            
def gameover():
    global gameOver
    
    textSize(82)
    text("GAME OVER", 250, 350)
    text("Score: "+str(score), 330, 450)
    gameOver = True


def ball_move():
    global ballX, ballY, speedY, speedX, g, score, difficulty, scaleLarge
    
    textSize(32)
    text("Score: "+str(score), 10, 30); 
    text("Difficulty: "+str(difficulty), 10, 80)

    fill(255)
    ellipse(ballX, ballY, 50, 50)
    
    speedY += g
    
    ballY -= speedY
    ballX += speedX

    rd = random(1, 2)
     
    if score == 5:
        difficulty = 2
         
    if ballX + 25 > width or ballX < 0: #Si toca la pared
        speedX = -speedX #que la gravedad se retenga y rebote
    if ballY + 25 > y:
        if ballX > x and ballX + 25 < x + scaleLarge: #Si toca la barra, que rebote
            speedY = -speedY
            score += 1
        elif ballY + 10 > height: #Si cae abajo           
            gameover()
            
    difficulty_func()
         
def difficulty_func():
    global difficulty, scaleLarge, speed, g
    
    if(difficulty == 2):
        scaleLarge = 200
        g = -0.6
        
        


    
        
