class Players:

    def __init__(self,name,hot_dog,pizza,meatballs,burger):
        self.name = name
        self.hot_dog = hot_dog
        self.pizza = pizza
        self.meatballs = meatballs
        self.burger = burger
        self.finalscore = hot_dog+pizza+meatballs+burger
    
    def __add__(self, otherplayer):
        result = self.finalscore + otherplayer.finalscore
        return result
    
    def __sub__(self, otherplayer):
        result = self.finalscore - otherplayer.finalscore
        return result
    
    def __repr__(self):
        result = 'The competitor {}, eats {} hot-dogs, {} pizzas, {} meatballs and {} burger '\
            'accumulating up to {} points\n'.format(self.name, self.hot_dog, self.pizza, self.meatballs,
            self.burger, self.finalscore)
        return result

def result(p1, p2, p3, p4, p5):
    Result = {
        p1.name : p1.finalscore,
        p2.name : p2.finalscore,
        p3.name : p3.finalscore,
        p4.name : p4.finalscore,
        p5.name : p5.finalscore 
    }

    scoreboard = sorted(Result.items(), key=lambda x:x[1])
    count = 1

    #sorted by accumulated points

    print('      Scoreboard       \n' \
        '|--------------------|')
    for i in scoreboard:
        print("| {:^8} |{:^4}lugar|".format(i[0], count))
        count += 1
    print("|--------------------|\n")


if __name__ == '__main__':
    p1 = Players('igor', 10, 21, 30,4)
    p2 = Players('cath', 20, 10, 40,2)
    p3 = Players('gabriel', 15, 25,30,7)
    p4 = Players('lara', 25, 10,30,5)
    p5 = Players('lis', 30, 22,30,10)
    result(p1,p2,p3,p4,p5)

    #print relevants infos of each player

    print(p1)
    print(p2)         #just some examples
    print(p3)

    #comparing the score between two players or adding their points

    #just some examples
    print('The sum of the score between {} and {} is {}\n'.format(p1.name,p2.name,p1 + p2))
    print('The difference in the score between {} and {} is {}\n'.format(p3.name,p4.name,p3 - p4))   
    


