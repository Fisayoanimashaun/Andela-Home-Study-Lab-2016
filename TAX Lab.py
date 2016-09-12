#Tax Calculator
"""
Country X calculates tax for its citizens using a graduated scale rate as shown below:
Yearly Income: 0 - 1000
Tax Rate: 0%
Yearly Income: 1,001 - 10,000
Tax Rate: 10%
Yearly Income: 10,001 - 20,200
Tax Rate: 15%
Yearly Income: 20,201 - 30,750
Tax Rate: 20%
Yearly Income: 30,751 - 50,000
Tax Rate: 25%
Yearly Income: Over 50,000
Tax Rate: 30%
"""

def calculate_tax(people):
    while True:
        try:
            name_list = people.keys()
            for name in name_list:
                income = people[name]
                if income <= 1000:
                    people[name] = 0
                elif income in range(1001, 10001):
                    tax_1 = 0 * 1000
                    tax_2 = 0.10 * (income - 1000)
                    tax = (tax_1 + tax_2)
                    people[name] = tax
                elif income in range(10001, 20201):
                    tax_1 = 0 * 1000
                    tax_2 = 0.1 * 9000
                    tax_3 = 0.15 * (income - 10000)
                    tax = (tax_1 + tax_2 + tax_3)
                    people[name] = tax
                elif income in range(20201, 30751):
                    tax_1 = 0 * 1000
                    tax_2 = 0.1 * 9000
                    tax_3 = 0.15 * 10200
                    tax_4 = 0.20 * (income - 20200)
                    tax = (tax_1 + tax_2 + tax_3 + tax_4)
                    people[name] = tax
                elif income in range(30751, 50001):
                    tax_1 = 0 * 1000
                    tax_2 = 0.1 * 9000
                    tax_3 = 0.15 * 10200
                    tax_4 = 0.20 * 10550
                    tax_5 = 0.25 * (income - 30750)
                    tax = (tax_1 + tax_2 + tax_3 + tax_4 + tax_5)
                    people[name] = tax
                elif income > 50000:
                    tax_1 = 0 * 1000
                    tax_2 = 0.1 * 9000
                    tax_3 = 0.15 * 10200
                    tax_4 = 0.20 * 10550
                    tax_5 = 0.25 * 19250
                    tax_6 = 0.30 * (income - 50000)
                    tax = (tax_1 + tax_2 + tax_3 + tax_4 + tax_5 + tax_6)
                    people[name] = tax
            return people
            break
        except (AttributeError, TypeError):
            raise ValueError("The provided input is not a dictionary")
        

                    
                    
                    
                    
                
                
                
            
	
    


