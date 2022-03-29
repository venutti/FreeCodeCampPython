MAX_WIDTH = 30

def transform_amount(string):
    a,b = string.split(".")
    return ".".join([a,b.ljust(2, "0")]) #Devuelve el formato con dos decimales detras del punto


class Category():
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def get_withdraw(self):
        return sum([x["amount"] for x in self.ledger if x["amount"] < 0])

    def get_balance(self):
        return sum([x["amount"] for x in self.ledger])

    def check_funds(self, amount):
        return False if amount > self.get_balance() else True

    def deposit(self, amount, description=""):
        self.ledger.append({"amount":amount, "description": description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount): return False
        self.deposit(-amount, description)
        return True

    def transfer(self, amount, other):
        if not self.check_funds(amount): return False
        other.deposit(amount, f"Transfer from {self.name}")
        return self.withdraw(amount, f"Transfer to {other.name}")

    def __repr__(self):
        str_repr = []
        str_repr.append( self.name.center(MAX_WIDTH, "*") )
        for move in self.ledger:
            amount = transform_amount(str(float(move["amount"])))
            description = move["description"][:MAX_WIDTH-len(amount)-1] #Recorta la descripcion para que se amolde al MaxWidth
            amount = amount.rjust(MAX_WIDTH-len(description)) #Rellena el amount para que ocupe todo el MaxWidth
            str_repr.append(description+amount)
        str_repr.append(f"Total: {self.get_balance()}")
        return "\n".join(str_repr)

    def __str__(self):
        return self.__repr__()


def create_chart(percentajes):
    chart = []
    scale = [(str(x*10)+"| ").rjust(5) for x in range(11)] #Crea la escala vertical de 0 a 100
    chart.append(scale[::-1])
    perc_line = []
    for i in range(len(percentajes)):
        for j in range(11):
            if j <= percentajes[i]: #Agrega o.. hasta llenar el cupo
                perc_line.append("o  ")
            else:
                perc_line.append("   ") #Rellena con espacios
        chart.append(perc_line[::-1])
        perc_line = []
    return "\n".join(["".join(x) for x in zip(*chart)])

def create_legend(categories):
    legend = [x.name for x in categories]
    height = len(max(legend, key=len))
    legend = [x.ljust(height) for x in legend] #Ajusta el largo de cada palabra
    legend = ["  ".join(x) for x in zip(*legend)] #Zipea caracter a caracter, agregando dos espacios entre ellos
    space = ["     " for _ in range(height)] 
    legend = ["".join(x) for x in zip(space, legend)] #Agrega el espacio inicial de la leyenda
    return "\n".join(legend)

def create_spend_chart(categories):
    barchart = []
    barchart.append("Percentage spent by category")
    total = sum([x.get_withdraw() for x in categories])
    percentajes = [ int(((x.get_withdraw()/total)*100)//10)  for x in categories ]
    barchart.append(create_chart(percentajes))
    barchart.append("    -"+"---"*len(categories))
    barchart.append(create_legend(categories))
    return "\n".join(barchart)
    

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))