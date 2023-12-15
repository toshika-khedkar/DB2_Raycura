
import pygame,sys,random
from pygame.math import Vector2
pygame.font.init()
font = pygame.font.SysFont("Arial", 20)




def run_game():
    class Button:
        
        def __init__(self, text,  pos, font, bg="black", feedback=""):
            
            self.x, self.y =pos
            self.font = pygame.font.SysFont("Arial", font)
            if feedback == "":
                self.feedback = "text"
            else:
                self.feedback = feedback
            self.change_text(text, bg)
        def change_text(self, text, bg="black"):
        
            self.text = self.font.render(text, 1, pygame.Color("White"))
            self.size = self.text.get_size()
            self.surface = pygame.Surface(self.size)
            self.surface.fill(bg)
            self.surface.blit(self.text, (90, 90))
            self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        def show(self):
            screen.blit(button1.surface, (self.x, self.y))
        def click(self, event):
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if self.rect.collidepoint(x, y):
                        self.change_text(self.feedback, bg="red")
    class SNAKE:
        def __init__(self):
            self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
            self.direction = Vector2(0,0)
            self.new_block = False

            self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
            self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
            self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
            self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
            
            self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
            self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
            self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
            self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

            self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
            self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

            self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
            self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
            self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
            self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
            self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

        def draw_snake(self):
            self.update_head_graphics()
            self.update_tail_graphics()

            for index,block in enumerate(self.body):
                x_pos = int(block.x * cell_size)
                y_pos = int(block.y * cell_size)
                block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

                if index == 0:
                    screen.blit(self.head,block_rect)
                elif index == len(self.body) - 1:
                    screen.blit(self.tail,block_rect)
                else:
                    previous_block = self.body[index + 1] - block
                    next_block = self.body[index - 1] - block
                    if previous_block.x == next_block.x:
                        screen.blit(self.body_vertical,block_rect)
                    elif previous_block.y == next_block.y:
                        screen.blit(self.body_horizontal,block_rect)
                    else:
                        if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                            screen.blit(self.body_tl,block_rect)
                        elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                            screen.blit(self.body_bl,block_rect)
                        elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                            screen.blit(self.body_tr,block_rect)
                        elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                            screen.blit(self.body_br,block_rect)

        def update_head_graphics(self):
            head_relation = self.body[1] - self.body[0]
            if head_relation == Vector2(1,0): self.head = self.head_left
            elif head_relation == Vector2(-1,0): self.head = self.head_right
            elif head_relation == Vector2(0,1): self.head = self.head_up
            elif head_relation == Vector2(0,-1): self.head = self.head_down

        def update_tail_graphics(self):
            tail_relation = self.body[-2] - self.body[-1]
            if tail_relation == Vector2(1,0): self.tail = self.tail_left
            elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
            elif tail_relation == Vector2(0,1): self.tail = self.tail_up
            elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

        def move_snake(self):
            if self.new_block == True:
                body_copy = self.body[:]
                body_copy.insert(0,body_copy[0] + self.direction)
                self.body = body_copy[:]
                self.new_block = False
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0,body_copy[0] + self.direction)
                self.body = body_copy[:]

        def add_block(self):
            self.new_block = True

        def play_crunch_sound(self):
            self.crunch_sound.play()

        def reset(self):
            self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
            self.direction = Vector2(0,0)


    class FRUIT:
        def __init__(self):
            self.randomize()
            # self.snake

        def draw_fruit(self):
            fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
            screen.blit(apple,fruit_rect)
            #pygame.draw.rect(screen,(126,166,114),fruit_rect)

        def randomize(self):
            # score=
            
            self.x = random.randint(0,cell_col - 1)
            self.y = random.randint(0,cell_row - 1)
            self.pos = Vector2(self.x,self.y)
    # ob= FRUIT()
    # ob.randomize(self)
    class MAIN:
        def __init__(self):
            self.snake = SNAKE()
            self.fruit = FRUIT()

        def update(self):
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()

        def draw_elements(self):
            self.draw_grass()
            self.fruit.draw_fruit()
            self.snake.draw_snake()
            self.draw_score()

        def check_collision(self):
            if self.fruit.pos == self.snake.body[0]:
                self.fruit.randomize()
                self.snake.add_block()
                self.snake.play_crunch_sound()

            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomize()

        def check_fail(self):
            if not 0 <= self.snake.body[0].x < cell_col or not 0 <= self.snake.body[0].y < cell_row:
                self.game_over()

            for block in self.snake.body[1:]:
                if block == self.snake.body[0]:
                    self.game_over()
            
        def game_over(self):
            self.snake.reset()

        def draw_grass(self):
            grass_color = (167,209,61)
            for row in range(cell_row):
                if row % 2 == 0: 
                    for col in range(cell_col):
                        if col % 2 == 0:
                            grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                            pygame.draw.rect(screen,grass_color,grass_rect)
                        else:
                            grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                            pygame.draw.rect(screen,(175,215,70),grass_rect)
            
                else:
                    for col in range(cell_col):
                        if col % 2 != 0:
                            grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                            pygame.draw.rect(screen,grass_color,grass_rect)	
                        else:
                            grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                            pygame.draw.rect(screen,(175,215,70),grass_rect)
                    

        def draw_score(self):
            score_text = str(len(self.snake.body) - 3)
            score_surface = game_font.render(" SCORE: "+score_text,True,(56,74,12))
            score_x = int(800)
            score_y = int(80)
            score_rect = score_surface.get_rect(center = (score_x,score_y))
            apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
            bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

            pygame.draw.rect(screen,(167,209,61),bg_rect)
            screen.blit(score_surface,score_rect)
            screen.blit(apple,apple_rect)
            pygame.draw.rect(screen,(56,74,12),bg_rect,2)
    
            
    button1 = Button(
    "Click here",
    (200, 200),
    font=30,
    bg="navy",
    feedback="You clicked me")
    pygame.mixer.pre_init(44100,-16,2,512)
    pygame.init()
    cell_size = 35
    cell_col=20
    cell_row=15
    screen = pygame.display.set_mode(((cell_col * cell_size) ,(cell_row * cell_size)))
    clock = pygame.time.Clock()

    apple = pygame.image.load('Graphics/apple.png').convert_alpha()
    game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)
    window_width, window_height = 950, 527
    #  col row
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Snake Game')
    # window =tk.Tk()
    window.blit(screen,(600,600))
    pygame.display.update()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE,150)

    main_game = MAIN()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                button1.click(event)
                
                sys.exit()
            button1.show()
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:  # Check for left mouse button click
            #         pos = pygame.mouse.get_pos()
            #         for button in buttons:
            #             if button.is_clicked(pos):
            #                 print(f"Button '{button.text}' clicked!")
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0,-1)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1,0)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0,1)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1,0)

        screen.fill((0,0,0))
        main_game.draw_elements()
    
        pygame.display.update()
    
        clock.tick(60)





if __name__ == "__main__":
    run_game() 