class FrenchConverter:
    
    def convert_to_french(self, num):
        if num < 17:
            return ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", 
                    "sept", "huit", "neuf", "dix", "onze", "douze", 
                    "treize", "quatorze", "quinze", "seize"][num]
        
        if num < 20:
            return "dix-" + self.convert_to_french(num - 10)
        
        if num == 20:
            return "vingt"
        
        if num == 30:
            return "trente"
        
        if num == 40:
            return "quarante"
        
        if num == 50:
            return "cinquante"
    
        if num == 60:
            return "soixante"
        
        if num < 70:
            tens = num // 10 * 10
            remainder = num % 10
            if remainder == 1:
                return self.convert_to_french(tens) + '-et-' + self.convert_to_french(remainder)
            return self.convert_to_french(tens) + ('-' + self.convert_to_french(remainder) if remainder != 0 else '')
        
        if num < 80:
            remainder = num % 10
            return "soixante" + ("-et-" if remainder == 1 else "-") + self.convert_to_french(num - 60)
        
        if num < 100:
            if num < 90:
                return "quatre-vingt" + ('-' + self.convert_to_french(num - 80) if num % 80 != 0 else 's')
            else:
                return "quatre-vingt-" + self.convert_to_french(num - 80)
        
        if num == 100:
            return "cent"
        
        if num < 200:
            remainder = num % 100
            return "cent" + ("-" + self.convert_to_french(remainder) if remainder != 0 else "")
        
        if num < 1000:
            hundreds = num // 100
            remainder = num % 100
            if remainder == 0:
                return self.convert_to_french(hundreds) + "-cents"
            else:
                return self.convert_to_french(hundreds) + "-cent-" + self.convert_to_french(remainder)
        
        if num == 1000:
            return "mille"
        
        if num < 2000:
            remainder = num % 1000
            return "mille" + ("-" + self.convert_to_french(remainder) if remainder != 0 else "")
        
        if num < 1000000:
            milles = num // 1000
            remainder = num % 1000
            if remainder == 0:
                return self.convert_to_french(milles) + "-milles"
            else:
                return self.convert_to_french(milles) + "-mille-" + self.convert_to_french(remainder)
        
        return "Number out of range"
