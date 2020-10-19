class Coding:

    def __init__(self, x: int) -> None:
        self.x =x

        return None
    
    def coder(self, x: int)-> int:
        for i in range(x):
            x-= 1
    def getx(self, x :int) -> int:
        return x
    def __str__(self) -> str:
        """just for the classes description"""
        val= str(self.x)
        return val

    


 

 

def main():
   bane = Coding(20)
   bane.getx
   bane.coder(20)
   print(str(bane))


if __name__ == "__main__": 
    main()