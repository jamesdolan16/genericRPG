class Entity:
    def __init__(self, li, xPos, yPos, entityName, **details):
        self.xPos = xPos
        self.yPos = yPos
        self.li = li
        self.entityName = entityName
        self.details = details

    def entityScript(self, scriptIndex = 0, *params):
        # runs a script in the "scripts" list, by default the first
        if not params:
            params = ()
        else:
            params = *params
        self.li.runScript(self.details["scripts"][scriptIndex], params)
    
    def event(self, eventId, *params):
        # activates an event if a script is designated for that particular event
        if eventId in self.details["events"]:
            if not params:
                params = ()
            else:
                params = *params
            self.entityScript(self.details["events"][eventId], params)

#############################################################################

class Item(Entity):
    def __init__(self, li, xPos, yPos, entityName, isStatic, itemType,
                 inWorld = True, **details):
        super().__init__(li, xPos, yPos, entityName, **details)
        self.isStatic = isStatic
        self.itemType = itemType
        self.inWorld = inWorld
        
    def pickUp(self):
        # if it's a pickup, it takes itself out of the world, then returns itself
        if self.inWorld and not self.isStatic:
            self.inWorld = False
            self.event("pickedUp", self)
            return self
        else:
            li.runScript("echo Object not pickable;")

    def activate(self):
        # if it's static and activatable, it activates the "activated" event
        if self.isStatic and self.details["activatable"]:
            self.event("activated", self)
        else:
            li.runScript("echo Object not activatable;")

    def equipArmour(self):
        # if it's armour, it returns itself
        if itemType == "armour":
            if not value == None:
                self.event("wasEquipped", self)
                return pickUp()

#############################################################################

def defaultArmour(li):
    # returns the default (empty) armour slot
    return Item(li, xPos = 0, yPos = 0, isStatic = False,
                itemType = "armourBase", inWorld = False, armourList = [])    

class Creature(Entity):
    def __init__(self, li, xPos, yPos, entityName, maxHealth, health = -1,
                 naturalArmour = -10, inventory, **details):
        super().__init__(li, xPos, yPos, entityName, **details)
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
            self.inventory = []
        else:
            self.suitArmour = 0
            self.details["armour"] = defaultArmour(self.li)
        self.naturalArmour = naturalArmour
        self.totalArmour = self.naturalArmour + self.suitArmour
        self.alive = True

    def receiveDamage(self, power, piercing):
        # calculates damage received and changes its own health by that much
        damage = power / (1 + (self.totalArmour / 100) / piercing)
        self.changeHealth(damage)
        self.event("receivedDamage", self)

    def changeHealth(self, amount):
        # changes health - if it is <= 0, it dies
        if self.alive:
            self.health -= amount
            if amount < 0:
                self.event("receivedHealing", self)
            if self.health <= 0:
                self.alive = False
                self.event("died", self)
        else:
            self.li.runScript(
                "echo Creature dead - it cannot act or be acted on;")

    def equipArmour(self, armour):
        # equips armour - increases armour value
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
            self.event("equippedArmour", entityName, armour.armourType)

    def unequipArmour(self, armourType):
        # unequips armour and puts it in inventory - decreases armour value
        armourToUnequip = -1
        for armourIndex in range(len(self.details["armour"].armourList)):
            if self.details[
                "armour"].armourList[armourIndex].armourType == armourType:
                armourToUnequip = armourIndex
        if armourToUnequip != -1:
            self.details["armour"].armourValue -= self.details[
                "armour"].armourList[armourToUnequip].armourValue
            self.inventory.append(
                self.details["armour"].armourList[armourToUnequip])
            del self.details["armour"].armourList[armourToUnequip]
        else:
            return None
        









