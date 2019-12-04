import random

class Message():
    greetings = ['Best Regards, Obi One', 'Sincerely yours, Leyla', 'Be aware of your dark side, Yoda']
    listMessages = []

    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver

    def insertObjectOfMessage(self):
        ask = True
        while ask:
            objectOfMessage = input("You're pleased to insert the object of the message:"
                                    "(not longer than 30 characters)\n")
            if len(objectOfMessage) <= 30:
                self.objectOfMessage = objectOfMessage
                print("You've inserted your message correctly!")
                print(f"The message you inserted is '{objectOfMessage}'.")
                ask = False
            else:
                print("The message you inserted is longer than 30 characters...Be polite, please.\nNewly insert the"
                      " object of the message, please.")

    def insertBodyOfMessage(self):
        ask = True
        while ask:
            bodyOfMessage = input("You're pleased to insert the object of the message:"
                                    "(not longer than 500 characters)\n")
            if len(bodyOfMessage) <= 500:
                self.bodyOfMessage = bodyOfMessage
                print("You've inserted your body of the message correctly!")
                print(f"The message you inserted is '{bodyOfMessage}'.")
                ask = False
            else:
                print("The message you inserted is longer than 500 characters...Be polite, please.\nNewly insert the"
                      " object of the message, please.")

    def confidentialMessage(self, confidentiality=0):
        'It assumes the message is not confidential.'
        self.confidentiality = confidentiality

    def countConsonants(self):
        counter = 0
        for letter in self.objectOfMessage:
            if letter not in 'aeiouAEIOU0123456789 ':
                counter += 1
        if not(counter):
            counter = 1                             # Just to manage absence of consonants in the object of the message.
        return counter

    def cypherCaesar(self):
        self.encryptedMessage = ''
        self.counterConsonants = self.countConsonants()
        if self.counterConsonants:
            for letter in self.bodyOfMessage:
                a = ord(letter) + self.counterConsonants
                self.encryptedMessage += chr(a)

    def decipherCaesar(self):
        self.decryptedMessage = ''
        for letter in self.encryptedMessage:
            a = ord(letter) - self.counterConsonants
            self.decryptedMessage += chr(a)

    def _append_greetings(self):
        self.greetings_to_you_now = random.choice(self.greetings)
        self.bodyOfMessage += ("\n" + self.greetings_to_you_now)

    def append_greetings(self):
        self._append_greetings()

    def _to_fullText(self):
        self.transformedMessage = f"FROM: {self.sender}   TO: {self.receiver}    OBJ: {self.objectOfMessage}   \n" \
                                  f"BODY: {self.bodyOfMessage}"

    def to_fullText(self):
        self._to_fullText()

    def __str__(self):
        return f"FROM: {self.sender}   TO: {self.receiver}    OBJ: {self.objectOfMessage}   \n" \
               f"PRIORITY: {self.confidentiality}\n" \
               f"BODY: {self.bodyOfMessage}    LENGTH OF BODY: {len(self.bodyOfMessage)}"

    @classmethod
    def createThreeinstanceMessage(cls, numCreations=3):
        for i in range(numCreations):
            sender = input("Who is the sender?\n")
            receiver = input("Who is the receiver?\n")
            objectNow = Message(sender, receiver)
            objectNow.insertObjectOfMessage()
            objectNow.insertBodyOfMessage()
            conf = input("Is this message confidential?"
                         "('yes/y' to say 'yes', any other answer will be treated like 'no')\n").lower()
            if conf == 'yes' or conf == 'y':
                conf = 1
            else:
                conf = 0
            objectNow.confidentialMessage(confidentiality=conf)
            if objectNow.confidentiality == 1:
                objectNow.cypherCaesar()
                objectNow.decipherCaesar()
            objectNow.append_greetings()
            # Here we're removing the greetings already used:
            del cls.greetings[cls.greetings.index(objectNow.greetings_to_you_now)]
            cls.listMessages.append(objectNow)

    @classmethod
    def printOrderListMessageBySender(cls):
        'Order the objects created by sender in decreasing alphabetical order'
        cls.orderedListMessageBySenderDESC = sorted([message.sender for message in cls.listMessages], reverse=True)
        for messageOrderedBySender in cls.orderedListMessageBySenderDESC:
            for messageUnordered in cls.listMessages:
                if messageOrderedBySender == messageUnordered.sender:
                    print(messageUnordered)


    @classmethod
    def printMessages(cls):                     # Now you have to order by sender DESC
        for element in cls.listMessages:
            print(element)
