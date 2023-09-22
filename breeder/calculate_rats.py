from random import getrandbits
import matplotlib.pyplot as plt

class BreederCalculations:
    #every second the rat status will update according to this code
    #real time graphing????
    def __init__(self, game):
        self.game = game
        self.rat_count = 10
        self.upper_cap = 100
        self.lower_cap = 0
        self.next_increase = 0

        self.spawn_crow = False

        #every turn, healhy status decreases if no food or bad conditions
        #flucuate randomly

    def crow_eat_rat(self):
        #do once every rat spawn cylce only
        if self.game.crow.state == 'attack':
            if True:
                if self.rat_count//3 < 1:
                    self.next_increase -= 1
                else:
                    self.next_increase -= self.rat_count/3
                    # print('yujkm,')


    def calculate_next_change(self):
        if self.rat_count > 1:
            self.next_increase += self.rat_count / 4
            if (self.next_increase+self.rat_count) > self.upper_cap:
                self.next_increase = self.upper_cap - self.rat_count

    def update(self):
        self.rat_seller()
        # if self.timer == 60:
        # print(int(self.rat_count), self.next_increase,)
        
        self.next_increase = 0
        if self.rat_count > 1:
            self.crow_eat_rat()
            self.calculate_next_change()
        elif self.rat_count == 1:
            self.next_increase = 0
            self.crow_eat_rat()
        elif self.rat_count < self.lower_cap:
            self.rat_count = 0
        self.rat_count += self.next_increase
        self.manage_rat_data(self.game.rat_data, self.rat_count)
    
    def manage_rat_data(self, data_list, x):
        if len(data_list) < 10:
            data_list.append(x)
        else:
            data_list.pop(0)
            data_list.append(x)
        # print(self.game.rat_data)

    def plotter(self):
        print('plotted')
        plt.clf()
        plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], self.game.rat_data)
        plt.xlabel('iterations')
        plt.ylabel('rat count')
        plt.title('rat growth affected by crows eating them over time')
        plt.savefig('./data/images/breeder/rat_data.png')

    def manual_breeding():
        pass

    def rat_seller(self):
        #every cycle in that timed loop in breeder game
        #constantly converts 10% of all rats to money
        # if self.game.breeder_shop.items[6]["owned"]:
        self.game.money += self.rat_count * 0.1 * self.game.breeder_shop.RAT_PRICE
        self.rat_count -= self.rat_count * 0.1
        


    #these status conditions update every few cycles like crow
    # def get_sick(self):
    #     pass
    # def get_hungry(self):
    #     if self.food:
            
    #     pass