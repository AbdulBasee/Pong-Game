from tkinter import *
import random
import pygame
import time

######################################################################
# Author: AbdulBaseer Mahmood
# Username: AbdulBaseer Mahmood
#

#
# Purpose: Interactive Pong Game
######################################################################
# Acknowledgements:
#
# Acknowledgements:
#

####################################################################################





counter = 0

pygame.init()
ROOT = Tk()
HEGHT = 700
WIDTH = 700
ROOT.title('Pong')
canvas = Canvas(ROOT,bg='black', width = WIDTH, height = HEGHT)
velocity = 30

canvas.update()
WINDOW_HEIGHT = canvas.winfo_screenheight() - 68
WINDOWWIDTH = canvas.winfo_screenwidth()
canvas.pack()






class Padding:

    def __init__(self, canvas):
        """

        :param canvas:
        """

        self.canvas = canvas
        self.PAD_HEIGHT = 100
        self.PAD_WIDTH = 100
        self.pad_velocity = 30





        self.left_pad = canvas.create_rectangle(0, 300, 40, 400,fill = 'red')

        self.right_pad = canvas.create_rectangle(660, 300, 700, 400, fill = 'red')


        # self.pad_screen_collision()
        print(canvas.coords(self.right_pad))




    def pad_motion(self,event):
        """

        :param event:
        :return: None
        """
        (rightpx1, rightpy1, rightpx2, rightpy2) = canvas.coords(self.right_pad)
        (leftpx1, leftpy1, leftpx2, leftpy2) = canvas.coords(self.left_pad)

        if event.char == 'o':
            canvas.move(self.right_pad, 0, -self.pad_velocity)
            if rightpy1 <= 0:
                canvas.move(self.right_pad, 0, self.pad_velocity)






        elif event.char == 'l':
            canvas.move(self.right_pad, 0, self.pad_velocity)
            if rightpy2 >= WIDTH:
                canvas.move(self.right_pad, 0, -self.pad_velocity)




            # left pad
        elif event.char == 'w':

            canvas.move(self.left_pad, 0, -self.pad_velocity)
            if leftpy1 <= 0:
                canvas.move(self.left_pad, 0, self.pad_velocity)




        elif event.char == 's':
            canvas.move(self.left_pad, 0, self.pad_velocity)
            if leftpy2 >= WIDTH:
                canvas.move(self.left_pad, 0, -self.pad_velocity)


class Ball(Padding):
        def __init__(self, canvas, color):
            """

            :param canvas:
            :param color:
            """

            super().__init__(canvas)

            self.canvas = canvas

            self.x_distace = 5
            self.y_distace = 5
            # self.rand = random.choice(self.y_distace)
            self.player1_score = 0
            self.player2_socre = 0
            self.height = canvas.winfo_screenheight() - 68
            self.width =  canvas.winfo_screenwidth() - 666

            self.ball_velocity = 20
            self.color = color
            self.ball = canvas.create_oval((WIDTH // 2 -25), (HEGHT // 2 -25), (WIDTH// 2 + 25) , (HEGHT //2 + 25), outline="#f11", fill="#1f1", width=2)
            # canvas.move(self.ball, 315,315)
            self.ball_screen_collision()




        def ball_screen_collision(self):
            """ This function contains the code for ball and screen collision.

            :return: None
            """

            (bx1, by1, bx2, by2) = canvas.coords(self.ball)
            # print(bx1,by1,bx2,by2)

            if bx2 >= HEGHT:
                canvas.delete(self.ball)
                self.ball = canvas.create_oval((WIDTH // 2 - 25), (HEGHT // 2 - 25), (WIDTH // 2 + 25),
                                               (HEGHT // 2 + 25), outline="#f11", fill="#1f1", width=2)
                self.player1_show_score()
            if by2 >= WIDTH:
                self.y_distace = -self.y_distace
            if bx1 <= 0:
                canvas.delete(self.ball)
                self.ball = canvas.create_oval((WIDTH // 2 - 25), (HEGHT // 2 - 25), (WIDTH // 2 + 25),
                                               (HEGHT // 2 + 25), outline="#f11", fill="#1f1", width=2)
                self.player_2_show_score()
            if by1 <= 0:
                self.y_distace = -self.y_distace

            self.ball_pad_collision()






            canvas.move(self.ball,self.x_distace, self.y_distace)
            ROOT.after(self.ball_velocity, self.ball_screen_collision)

        def ball_pad_collision(self):
            """

            :return:
            """

            (bx1, by1, bx2, by2) = canvas.coords(self.ball)
            (rightpx1, rightpy1, rightpx2, rightpy2) = canvas.coords(self.right_pad)
            (leftpx1, leftpy1, leftpx2, leftpy2) = canvas.coords(self.left_pad)


            if bx2 >= rightpx1  and bx2 <= rightpx2 - 40 and (by2 > rightpy1 and (by2 - 50) < rightpy2):


                    self.x_distace = -self.x_distace


                    pygame.mixer.music.load("pingpongm.mp3")  # Loading File Into Mixer
                    pygame.mixer.music.play()








            if bx1 >= leftpx1 + 40 and bx1 <= leftpx2 and ((by1 +45) > leftpy1 and by1 < leftpy2):


                    self.x_distace = -self.x_distace

                    pygame.mixer.music.load("pingpongm.mp3")  # Loading File Into Mixer
                    pygame.mixer.music.play()







            # self.player1_show_score()

        def player1_show_score(self):
            """

            :return:
            """




            m = canvas.create_text(50, 50, text = self.player1_score,  font= ("Arial", 60), fill = 'white')


            canvas.itemconfig(m, fill = 'black')
            # if self.player1_score > self.player2_socre:
            #     canvas.create_text(350, 350, text="Player One wins the game ", font=("Arial", 30), fill='white')

            self.player1_score += 1

            k = canvas.create_text(50, 50, text=self.player1_score, font=("Arial", 60), fill='white')


        def player_2_show_score(self):
            """

            :return:
            """


            f = canvas.create_text(650, 50, text = self.player2_socre,  font= ("Arial", 60), fill = 'white')


            canvas.itemconfig(f, fill = 'black')
            # if self.player2_socre > self.player1_score:
            #     canvas.create_text(350, 350, text="Player Two wins the game ", font=("Arial", 30), fill='white')

            self.player2_socre += 1

            g = canvas.create_text(650, 50, text=self.player2_socre, font=("Arial", 60), fill='white')



ball = Ball(canvas,'blue')

ROOT.bind("<Key>", ball.pad_motion)


ROOT.mainloop()















