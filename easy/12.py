class Solution:
    def romanToInt(self, s: str) -> int:
        acum = 0
        prevChar = ""
        for n in reversed(s):          
            match n:
                case "I":
                    if prevChar in ["V","X","L","C","D","M"]:
                        acum -= 1
                    else:
                        acum += 1
                case "V":
                    if prevChar in ["X","L","C","D","M"]:
                        acum -= 5
                    else:        
                        acum += 5             
                case "X":
                    if prevChar in ["L","C","D","M"]:
                        acum -= 10
                    else:        
                        acum += 10
                case "L":
                    if prevChar in ["C","D","M"]:
                        acum -= 50                                       
                    else:        
                        acum += 50
                case "C":
                    if prevChar in ["D","M"]:
                        acum -= 100
                    else:        
                        acum += 100
                case "D":
                    if prevChar == "M":
                        acum -= 500
                    else:        
                        acum += 500
                case "M":
                    acum += 1000
            prevChar = n                                                            
        return acum
            
