import sys, pygame
from domain.Buttons import Button

pygame.init()

class UI:

    def __init__(self, service_points):

        self.__ServicePoints = service_points
        self.__size = 800, 800
        self.__screen = pygame.display.set_mode(self.__size)
        self.__point_list = []
        self.__hull = []
        self.__Return = False
        self.__command = ''
        self.__repeat = 0

    def inputNumberOfPoints(self):

        white = 255, 255, 255
        color_light = (170, 170, 170)
        color_dark = (100, 100, 100)
        red = 220, 20 ,60
        numbers = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
        self.__ServicePoints.delete_all_points()
        base_font = pygame.font.Font(None, 32)
        user_text = ''
        input_rect = pygame.Rect(330, 330, 140, 32)
        smallfont = pygame.font.SysFont('Corbel', 40)
        textInput = smallfont.render('Enter the number of points:', True, red)
        smallfont = pygame.font.SysFont('Corbel', 20)
        textCompute = smallfont.render('Wrap points', True, red)
        self.__screen.fill(white)
        pygame.display.flip()

        loop = True
        while loop and self.__repeat == 0:

            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 358 <= mouse[0] <= 458 and 378 <= mouse[1] <= 400:
                        loop = False
                        break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key in numbers:
                        user_text += event.unicode


            if 337 <= mouse[0] <= 477 and 330 <= mouse[1] <= 362:
                pygame.draw.rect(self.__screen, color_light, [337, 330, 140, 32])
            else:
                pygame.draw.rect(self.__screen, color_dark, [337, 330, 140, 32])

            if 358 <= mouse[0] <= 458 and 378 <= mouse[1] <= 400:
                pygame.draw.rect(self.__screen, color_light, [358, 378, 100, 25])
            else:
                pygame.draw.rect(self.__screen, color_dark, [358, 378, 100, 25])

            text_surface = base_font.render(user_text, True, (255, 255, 255))
            self.__screen.blit(text_surface, (input_rect.x + 60, input_rect.y + 5))
            self.__screen.blit(textInput, (190, 250))
            self.__screen.blit(textCompute, (360, 380))
            pygame.display.flip()

        self.__screen.fill(white)
        pygame.display.flip()
        self.__repeat += 1
        return user_text

    def wrapRandomPoints(self):

        black = 0, 0, 0
        white = 255, 255, 255
        red = 220, 20 ,60
        color_light = (170, 170, 170)
        color_dark = (100, 100, 100)
        smallfont = pygame.font.SysFont('Corbel', 20)
        textRepeat = smallfont.render('Repeat', True, red)
        textReturn = smallfont.render('Menu', True, red)
        self.__point_list = self.__ServicePoints.get_all_points()
        self.__hull = self.__ServicePoints.solveHull()
        self.__screen.fill(white)
        pygame.display.flip()

        loop = True

        while loop:

            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 0 <= mouse[0] <= 60 and 0 <= mouse[1] <= 20:
                       loop = False
                       break
                    if 0 <= mouse[0] <= 60 and 25 <= mouse[1] <= 45:
                       self.__Return = True
                       loop = False
                       break

            if 0 <= mouse[0] <= 60 and 0 <= mouse[1] <= 20:
                pygame.draw.rect(self.__screen, color_light, [0, 0, 60, 20])
            else:
                pygame.draw.rect(self.__screen, color_dark, [0, 0, 60, 20])

            if 0 <= mouse[0] <= 60 and 25 <= mouse[1] <= 45:
                pygame.draw.rect(self.__screen, color_light, [0, 25, 60, 20])
            else:
                pygame.draw.rect(self.__screen, color_dark, [0, 25, 60, 20])

            for point in self.__point_list:
                pygame.draw.circle(self.__screen, black, (point.x, point.y), 4)

            for i in range(0, len(self.__hull) - 1):
                # time.sleep(0.25)
                pygame.draw.line(self.__screen, black, (self.__hull[i].x, self.__hull[i].y), (self.__hull[i + 1].x, self.__hull[i + 1].y))
            pygame.draw.line(self.__screen, black, (self.__hull[len(self.__hull) - 1].x, self.__hull[len(self.__hull) - 1].y),(self.__hull[0].x, self.__hull[0].y))

            self.__screen.blit(textRepeat, (0, 0))
            self.__screen.blit(textReturn, (0, 25))
            pygame.display.flip()

    def wrapGivenPoints(self):

        black = 0, 0, 0
        white = 255, 255, 255
        red = 220, 20 ,60
        color_light = (170, 170, 170)
        color_dark = (100, 100, 100)
        nrPoints = 0
        self.__screen.fill(white)
        pygame.display.flip()

        smallfont = pygame.font.SysFont('Corbel', 20)
        textCompute = smallfont.render('Wrap points', True, red)
        textReturn = smallfont.render('Menu', True, red)
        loop = True
        while loop:

            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 0 <= mouse[0] <= 100 and 0 <= mouse[1] <= 20:
                        loop = False
                        break
                    elif 0 <= mouse[0] <= 100 and 20 <= mouse[1] <= 40:
                        self.__Return = True
                        loop = False
                        break
                    else:
                        nrPoints += 1
                        pygame.draw.circle(self.__screen, black, (mouse[0], mouse[1]), 4)
                        self.__ServicePoints.add_point(mouse[0], mouse[1])

            if 0 <= mouse[0] <= 100 and 0 <= mouse[1] <= 20:
                pygame.draw.rect(self.__screen, color_light, [0, 0, 100, 20])
            else:
                pygame.draw.rect(self.__screen, color_dark, [0, 0, 100, 20])

            if 0 <= mouse[0] <= 100 and 20 <= mouse[1] <= 40:
                pygame.draw.rect(self.__screen, color_light, [0, 25, 100, 20])
            else:
                pygame.draw.rect(self.__screen, color_dark, [0, 25, 100, 20])

            self.__screen.blit(textCompute, (0 , 0))
            self.__screen.blit(textReturn, (0, 25))
            pygame.display.flip()

        self.__point_list = self.__ServicePoints.get_all_points()
        self.__hull = self.__ServicePoints.solveHull()

        self.__screen.fill(white)
        pygame.display.flip()

        textReturn = smallfont.render('Return', True, red)
        loop = True
        while loop and self.__Return == False:

            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 0 <= mouse[0] <= 100 and 0 <= mouse[1] <= 20:
                       self.__Return == True
                       loop = False
                       break

            if 0 <= mouse[0] <= 100 and 0 <= mouse[1] <= 20:
                pygame.draw.rect(self.__screen, color_light, [0, 0, 60, 20])
            else:
                pygame.draw.rect(self.__screen, color_dark, [0, 0, 60, 20])

            for point in self.__point_list:
                pygame.draw.circle(self.__screen, black, (point.x, point.y), 4)

            for i in range(0, len(self.__hull) - 1):
                # time.sleep(0.25)
                pygame.draw.line(self.__screen, black, (self.__hull[i].x, self.__hull[i].y), (self.__hull[i + 1].x, self.__hull[i + 1].y))
            pygame.draw.line(self.__screen, black, (self.__hull[len(self.__hull) - 1].x, self.__hull[len(self.__hull) - 1].y),(self.__hull[0].x, self.__hull[0].y))

            self.__screen.blit(textReturn, (0, 0))
            pygame.display.flip()
        return nrPoints

    def menu(self):

        black = 0, 0, 0
        wrapRandom = False
        wrapGiven = False
        color_light = (170, 170, 170)
        color_dark = (100, 100, 100)
        width = self.__screen.get_width()
        height = self.__screen.get_height()
        white = 255, 255, 255
        self.__screen.fill(white)
        pygame.display.flip()
        pygame.display.set_caption("ConvexHullVisualizer")

        red = 220, 20 ,60
        smallfont = pygame.font.SysFont('Corbel', 35)
        microfont = pygame.font.SysFont('Corbel', 13)
        textTitle = smallfont.render('Convex hull visualisation(gift wrapping)', True, red)
        textRandom = smallfont.render('Wrap random points', True, red)
        textGiven = smallfont.render('Wrap given points', True, red)
        textArtist = microfont.render('by b1ka', True, red)

        loop = True
        while loop:

            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if width/2-125 <= mouse[0] <= width/2+160 and height/2-105 <= mouse[1] <= height/2-55:
                        self.__command = 'wrapRandom'
                        loop = False
                        break
                    elif width / 2 - 135 <= mouse[0] <= width / 2 + 160 and height / 2 - 35 <= mouse[1] <= height / 2+10:
                        self.__command = 'wrapGiven'
                        loop = False
                        break

            if width / 2 - 135 <= mouse[0] <= width / 2 + 160 and height / 2 - 105 <= mouse[1] <= height / 2-55:
                pygame.draw.rect(self.__screen, color_light, [width/2-135, height/2-105, 295, 50])
            else:
                pygame.draw.rect(self.__screen, color_dark, [width/2-135, height/2-105, 295, 50])

            if width / 2 - 135 <= mouse[0] <= width / 2 + 160 and height / 2 - 35 <= mouse[1] <= height / 2+10:
                pygame.draw.rect(self.__screen, color_light, [width/2-135, height/2-35, 295, 50])
            else:
                pygame.draw.rect(self.__screen, color_dark, [width/2-135, height/2-35, 295, 50])

            self.__screen.blit(textTitle, (140,200))
            self.__screen.blit(textRandom, (width/2-130 , height/2-100))
            self.__screen.blit(textGiven, (width/2-115, height/2-30))
            self.__screen.blit(textArtist, (750, 750))
            pygame.display.update()

    def run(self):

        self.menu()
        white = 255, 255, 255
        self.__screen.fill(white)
        pygame.display.flip()
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            if self.__command == 'wrapRandom':
               self.__ServicePoints.delete_all_points()
               if self.__repeat == 0:
                  n = self.inputNumberOfPoints()
               if n != '':
                  n = int(n)
                  self.__ServicePoints.createRandomPoints(n)
                  self.wrapRandomPoints()
               else:
                   self.__Return = True
            if self.__command == 'wrapGiven':
               self.__ServicePoints.delete_all_points()
               nr = self.wrapGivenPoints()
               if nr < 3:
                   self.__command == 'wrapGiven'
               self.__repeat = 0
            if self.__Return == True:
                self.__Return = False
                self.menu()
                self.__repeat = 0
