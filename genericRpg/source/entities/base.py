class Entity:
    def __init__(self, li, xPos, yPos, **details):
        self.xPos = xPos
        self.yPos = yPos
        self.li = li
        self.details = details

#############################################################################

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

    def equipArmour(self):
        if itemType == "armour":
            value = pickUp()
            if not value == None:
                return pickUp()

#############################################################################

def defaultArmour(li):
    return Item(li, xPos = 0, yPos = 0, isStatic = False,
                itemType = "armourBase", inWorld = False, armourList = [])    

class Creature(Entity):
    def __init__(self, li, xPos, yPos, maxHealth, health = -1,
                 naturalArmour = 25, **details):
        super().__init__(li, xPos, yPos, details)
        self.maxHealth = maxHealth
        if health == -1:
            self.health = maxHealth
        else:
            self.health = health
        if "armour" in self.details:
            try:
                self.suitArmour = self.details["armour"].armourValue
            except NameError:
                self.suitArmour = 0
            originalArmour = self.details["armour"]
            self.details["armour"] = defaultArmour(self.li)
            self.details["armour"].armourList.append(originalArmour)
        else:
            self.suitArmour = 0
            self.details["armour"] = defaultArmour(self.li)
        self.naturalArmour = naturalArmour
        self.totalArmour = self.naturalArmour + self.suitArmour
        self.alive = True

    def receiveDamage(self, power, piercing):
        damage = power / (1 + (self.totalArmour / 100) / piercing)
        self.changeHealth(damage)

    def changeHealth(self, amount):
        if self.alive:
            self.health -= amount
            if self.health <= 0:
                self.alive = False
        else:
            self.li.runScript(
                "echo Creature dead - it cannot act or be acted on;")

    def equipArmour(self, armour):
        typeInArmour = False
        for armourPiece in self.details["armour"].armourList:
            if armourPiece.armourType == armour.armourType:
                typeInArmour = True
        if typeInArmour:
            self.li.runScript(
                "echo " + armour.armourType + " already equipped;")
        else:
            self.details["armour"].armourList.append(armour)
            self.details["armour"].armourValue += armour.armourValue

    def unequipArmour(self, armourType):
        armourToUnequip = -1
        for armourIndex in range(len(self.details["armour"].armourList)):
            if self.details[
                "armour"].armourList[armourIndex].armourType == armourType:
                armourToUnequip = armourIndex
        if armourToUnequip != -1:
            del self.details["armour"].armourList[armourToUnequip]
            return self
        else:
            return None
        









