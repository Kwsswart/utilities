class roman():
    
    def int_to_roman(self, n):
        """ Function to convert integers to roman integers """

        values = [
            1000, 900, 500, 400, 
            100, 90, 50, 40, 
            10, 9, 5, 4, 
            1]
        sym =[
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"]
        roman_num = ""
        i=0
        while n > 0:
          for o in range(n // values[i]):
            roman_num += sym[i]
            n -= values[i]
          i += 1
        return roman_num
    
    def roman_to_int(self, r):
        """ Function to convert roman numberals to integers """

        values = [
            1000, 900, 500, 400, 
            100, 90, 50, 40, 
            10, 9, 5, 4, 
            1]
        sym =[
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"]
        number = 0
        for i in range(len(r)):
            for j in range(len(sym)):
                if sym[j] == r[i]:
                    number += values[j]        
        return number
