import pygame
import utils
from button import textInput, itemButton

class Shop:
    def __init__(self, game, screen):
        self.error = pygame.mixer.Sound("data/sounds/error.ogg")
        self.error.set_volume(0.15)
        self.buy = pygame.mixer.Sound("data/sounds/buy.ogg")
        self.sell = pygame.mixer.Sound("data/sounds/sell.ogg")

        self.STORAGE_PRICE = 10
        self.RAT_PRICE = 1
        self.game = game
        #SHOP--------------------------------------
        self.screen = screen
        self.shop_img = utils.load_image("breeder/07-shop.png")
        self.shop_img_rect = self.shop_img.get_rect(center = self.screen.get_rect().center)
        self.input_buy_rats = textInput(200, 200, "buy")
        self.input_sell_rats = textInput(900, 200, "sell")

        self.storage_button = itemButton(1280/2,200,"buy storage $"+str(self.STORAGE_PRICE), True, "breeder/items/Storage.png",260,100)
        self.items = [
            {"name": "Food", "price": 5, "pos": (320,330), "owned": False, "description": "temporarily satiate rat hunger", "repurchasable": True},
            {"name": "AutoFeeder", "price": 5000, "pos": (320,400), "owned": False, "description": "rats never go hungry", "repurchasable": False},
            {"name": "Medicine", "price": 5, "pos": (320,470), "owned": False, "description": "cure rats", "repurchasable": True},
            {"name": "Doctor", "price": 5000, "pos": (320,540), "owned": False, "description": "rats never sick", "repurchasable": False},
            {"name": "Petter", "price": 500, "pos": (620,330), "owned": False, "description": "slightly increase rat breeding chance when clicking on them", "repurchasable": False},
            {"name": "Tempter", "price": 5000, "pos": (620,400), "owned": False, "description": "greatly increase rat breeding chance when clicking on them", "repurchasable": False},
            {"name": "Scarecrow", "price": 500, "pos": (620,470), "owned": False, "description": "decrease crow attack rate", "repurchasable": False},
            {"name": "CrowDestroyer", "price": 5000, "pos": (620,540), "owned": False, "description": "crows do not kill rats", "repurchasable": False}
        ]
        
        self.button_grid = []
        for x in self.items:
            self.button_grid.append(itemButton(x["pos"][0], x["pos"][1], x["name"]+" $"+str(x["price"]), x["repurchasable"], "breeder/items/"+x["name"]+".png"))

    def transactions(self, mouse_pos):
        if self.storage_button.activated:
            if self.game.money >= self.STORAGE_PRICE:
                self.game.money -= self.STORAGE_PRICE
                self.game.ratGrowth.upper_cap += 100
                self.buy.play()
                print("$ spend: ",self.STORAGE_PRICE,"money left: ",self.game.money,"new upper cap: ",self.game.ratGrowth.upper_cap)
                self.STORAGE_PRICE *= 2
                self.storage_button.change_text("buy storage $"+str(self.STORAGE_PRICE))
            else: self.error.play()
        if self.input_sell_rats.active:
            # print('')
            if self.input_sell_rats.user_text != '':
                if self.game.ratGrowth.rat_count >= int(self.input_sell_rats.user_text): #self.input_sell_rats.execute_order and 
                    self.game.ratGrowth.rat_count -= int(self.input_sell_rats.user_text)
                    if int(self.RAT_PRICE * 0.7) == 0: self.game.money += int(self.RAT_PRICE) * int(self.input_sell_rats.user_text)
                    else: self.game.money += int(self.RAT_PRICE * 0.7) * int(self.input_sell_rats.user_text)
                    self.sell.play()
                    print("sold", self.input_sell_rats.user_text,"rats for $"+str(int(self.RAT_PRICE * 0.7)))
                    print("current balance: ", self.game.money)
                else: self.error.play()
        if self.input_buy_rats.active and self.input_buy_rats.user_text != '':
            if self.game.money >= (self.RAT_PRICE * int(self.input_buy_rats.user_text)):
                if (int(self.input_buy_rats.user_text)+self.game.ratGrowth.rat_count) <= self.game.ratGrowth.upper_cap:
                    print(self.input_buy_rats.user_text)
                    self.game.ratGrowth.rat_count += int(self.input_buy_rats.user_text)
                    self.game.money -= self.RAT_PRICE * int(self.input_buy_rats.user_text)
                    self.buy.play()
                    print("bought", self.input_buy_rats.user_text,"rats for $"+str(int(self.RAT_PRICE)*int(self.input_buy_rats.user_text)))
                    print("current balance: ", self.game.money)
                else: self.error.play()
            else: self.error.play()

        for i in range(len(self.button_grid)):
            # if self.items[i]["owned"]:
            #     self.button_grid[i].activated = True
            self.button_grid[i].update(mouse_pos)#, self.items[i]["owned"]
            if self.button_grid[i].activated:
                if int(self.items[i]["price"]) <= self.game.money and not self.items[i]["owned"]:
                    self.game.money -= int(self.items[i]["price"])
                    if not self.items[i]["repurchasable"]:
                        self.buy.play()
                        self.items[i]["owned"] = True
                    else:
                        self.buy.play()
                        if self.items[i]["name"] == 'food':
                            self.game.food += 1
                            print('+1 food')
                        elif self.items[i]["name"] == 'medicine':
                            print('+1 medicine')
                elif int(self.items[i]["price"]) <= self.game.money and not self.items[i]["owned"]:
                    self.error.play()
                    print('2')
                    self.button_grid[i].activated = False
                    # self.button_grid[i].update_keyup()
                elif self.items[i]["owned"] and not self.items[i]["repurchasable"]:
                    # self.error.play()
                    # print('3')
                    self.button_grid[i].activated = True

                
                # print(self.items[i]["name"],self.items[i]["owned"],self.items[i]["repurchasable"])


    def render(self):
           
        self.screen.blit(self.shop_img, self.shop_img_rect)
        for i in range(len(self.button_grid)): 
            self.button_grid[i].render(self.screen)
        self.input_buy_rats.render(self.screen)
        self.input_sell_rats.render(self.screen)
        self.storage_button.render(self.screen)

    def mouse_down_events(self, mouse_pos):
        self.input_buy_rats.update(mouse_pos)
        self.input_sell_rats.update(mouse_pos)
        self.storage_button.update(mouse_pos)
        self.transactions(mouse_pos)

    def mouse_up_events(self):
        self.storage_button.update_keyup()
        self.input_sell_rats.update_keyup()
        self.input_buy_rats.update_keyup()
        for i in range(len(self.button_grid)): 
            self.button_grid[i].update_keyup()#, self.items[i]["owned"]
                
    def state_events(self, event):
        self.input_buy_rats.input_control(event)
        self.input_sell_rats.input_control(event)

