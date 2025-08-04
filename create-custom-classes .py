class pen:
    def __init__(self,brand,color):
      self.brand = brand
      self.color = color
      def write(self):
         print(f"{self.brand} pen is writing in {self.color} color.")

         #usage:
         p1 = pen("Reynolds","blue")
         p1.write()
         p2 = pen("cello","black")
         p2.write()