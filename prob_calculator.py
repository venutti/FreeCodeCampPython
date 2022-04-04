import copy
import random

def listar_dic(dic):
    res = []
    for k,w in dic.items():
        for _ in range(w):
            res.append(k)
    return res

def contiene(lista1, lista2):
    for item in lista2:
        try:
            lista1.remove(item)
        except:
            return False
    return True

class Hat():
    def __init__(self, **kwargs):
        self.contents = listar_dic(kwargs)

    def draw(self, number_daws):
        if number_daws > len(self.contents):
            return self.contents
        hat_content = copy.copy(self.contents)
        drawned = []
        #Sacar num_balls_drawn bolas
        for _ in range(number_daws):
            drawned.append(hat_content.pop(random.randrange(len(hat_content))))
        return drawned

    def __str__(self):
        return str(self.contents)

    def __repr__(self):
        return self.__str__()
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    #Crear una expresion para expexted_balls
    expected_balls = listar_dic(expected_balls)
    #Repetir el experimento num_experiments veces
    for _ in range(num_experiments):
        #Copiar el contenido del hat
        drawned = hat.draw(num_balls_drawn)
        #Ver si drawned contiene a expected_balls
        if contiene(drawned, expected_balls):
            M += 1
            
    return M/num_experiments

random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
