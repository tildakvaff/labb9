# Laboration 2 - Datastrukturer -LinkedQ
#Tillämpad Datalogi DD1320
# Erik Hellström, Eyasu Alemiye





class Node:
    def __init__(self,value): #konstruktor för att skapa noder med value och referensvärdet (=None)
        self.value = value
        self.next = None

    
    def getNext(self):
        return self.next
    

#klass som länkar noderna och metoder för att lägga till, ta ut, ta fram storlek och kontrollera om tom
class LinkedQ:
    def __init__(self):
        self.first = None#pekar på första element
        self.last = None#pekar på sista element



    #Metod för att ta bort element ut den länkade kön
    def dequeue(self):
        x = self.first.value
        self.first = self.first.next
        return x





    #metod för att kontrollera om tom
    def isEmpty(self):
        return self.first == None
    
    #metod för att lägga till element i länkade kön
    def enqueue(self, value):
        x = Node(value)

        if self.first == None:
            self.first = x
            self.last = x

        elif self.first != None:
            self.last.next = x
            self.last = x






    #DENNA KOMMER FRÅN KAP 4.5
    def peek(self):
        if self.isEmpty() is False:
            return self.first.value
        else:
            return None

    #Metod för att ta fram den länkade kön storlek
    def size(self):
        current = self.first
        count = 0
        while current != None:
            count = count +1
            current = current.getNext()
        return count


