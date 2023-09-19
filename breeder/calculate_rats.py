from random import getrandbits
import numpy as np
import matplotlib.pyplot as plt

class BreederCalculations:
    #every second the rat status will update according to this code
    #real time graphing????
    def __init__(self):
        self.timer = 0
        self.rat_count = 3
        self.upper_cap = 100
        self.next_increase = 0

        self.spawn_crow = False

        #every turn, healhy status decreases if no food or bad conditions
        #flucuate randomly

    def crow_eat_rat(self):
        #do once every rat spawn cylce only
        if getrandbits(1):
            if self.rat_count//3 < 1:
                self.next_increase -= 1
            else:
                self.next_increase -= self.rat_count/3

    def calculate_next_change(self):
        self.next_increase += self.rat_count / 3
        if (self.next_increase+self.rat_count) > self.upper_cap:
            self.next_increase = self.upper_cap - self.rat_count

    def update(self):
        if self.timer == 60:
            # print(int(self.rat_count), self.next_increase,)
            self.next_increase = 0
            if self.rat_count > 1:
                self.crow_eat_rat()
                self.calculate_next_change()
            elif self.rat_count == 1:
                self.crow_eat_rat()
            self.rat_count += self.next_increase
            self.timer = 0
        self.timer += 1
        

        # if self.rat_count >= self.upper_cap:
        #     #don't increase
        #     self.next_increase = 0
        #     self.rat_count = self.upper_cap
        #     #decay rats!!??
        # else:
        #     #increase
        #     #do nothing if rat count is 0
        #     if self.rat_count == 1:
        #         #get eaten?
        #         pass
        #         #reach uppercap?
        #         # self.crow_eat_rat()
        #     elif self.rat_count < 1:
        #         #get eaten?
        #         # self.crow_eat_rat()
        #         #exponential growth
        #         self.next_increase += 1
        #         #reach uppercap?

        # self.rat_count += self.next_increase





        #if unhealthy guaranteed mice die.
        # if 0% healthy 50% die
        # else, die proportional to health

        #crow can eat mice.
        # chance that crow comes
        #if 1 crow comes, every second, 1 mice dies

# test = []
# test_calc = BreederCalculations()
# for x in range(40):
#     test_calc.update()
#     test.append(test_calc.rat_count)
# plt.plot(test)
# plt.xlabel('iterations')
# plt.ylabel('rat count')
# plt.title('rat growth affected by crows eating them over time')
# plt.show()