class Entity:
    def __init__(self, li, xPos, yPos, **details):
        self.xPos = xPos
        self.yPos = yPos
        self.li = li
        self.details = details

class Item(Entity):
    def __init__(self, li, xPos, yPos, isStatic, itemType, inWorld = True,
                 **details):
        super().__init__(li, xPos, yPos, details)
        self.isStatic = isStatic
        self.itemType = itemType
        self.inWorld = inWorld
        
    def pickUp(self):
        if self.inWorld and not self.isStatic:
            self.inWorld = False
            return self
        else:
            li.runScript("echo Object not pickable;")

    def runScript(self):
        self.li.runScript(self.details["script"])

    def activate(self):
        if self.isStatic and self.details["activatable"]:
            self.runScript()
        else:
            li.runScript("echo Object not activatable;")

class Creature(Entity):
    def __init__(self, li, xPos, yPos, maxHealth, health = -1, armour = 25,
                 **details):
        super().__init__(li, xPos, yPos, details)
        self.maxHealth = maxHealth
        if health == -1:
            self.health = maxHealth
        else:
            self.health = health
        self.armour = armour
        self.alive = True

    def receiveDamage(self, power, piercing):
        damage = power / (1 + (self.armour / 100) / piercing)
        self.changeHealth(damage)

    def changeHealth(self, amount):
        if self.alive:
            self.health -= amount
            if self.health <= 0:
                self.alive = False
        else:
            self.li.runScript(
                "echo Creature dead - it cannot act or be acted on;")













