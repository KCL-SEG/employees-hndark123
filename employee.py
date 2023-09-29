"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Contract:
    def __init__(self, wage):
        self.wage = wage

class SalaryContract(Contract):
    def __init__(self, salary):
        super().__init__(0)
        self.salary = salary

    def calculatePay(self):
        return self.salary

class HourlyContract(Contract):
    def __init__(self, hourly_wage, hours_worked):
        super().__init__(hourly_wage)
        self.hours_worked = hours_worked

    def calculatePay(self):
        return self.wage * self.hours_worked
    
class Commission:
    def __init__(self, commission_type, bonus, num_of_contracts, contract_rate):
        self.commission_type = commission_type
        self.bonus = bonus
        self.num_of_contracts = num_of_contracts
        self.contract_rate = contract_rate

    def calculateCommission(self):
        if self.commission_type == "bonus":
            return self.bonus
        elif self.commission_type == "contract":
            return self.num_of_contracts * self.contract_rate
        else:
            return 0

class Employee:
    def __init__(self, name, contract, commission=None):
        self.name = name
        self.contract = contract
        self.commission = commission
    
    def get_pay(self):   
        contract_pay = self.contract.calculatePay()
        commission_pay = 0
        if self.commission:
            commission_pay = self.commission.calculateCommission()
        return contract_pay + commission_pay

    def __str__(self):
        contract_desc = f"{self.name} works on a "
        if isinstance(self.contract, SalaryContract):
            contract_desc += f"monthly salary of {self.contract.salary}"
        elif isinstance(self.contract, HourlyContract):
            contract_desc += f"contract of {self.hours_worked} hours at {self.contract.wage}/hour"
        if self.commission:
            if self.commission.commission_type == "bonus":
                commission_desc = f" and receives a bonus commission of {self.commission.bonus}"
            else:
                commission_desc = f" and receives a commission for {self.commission.num_of_contracts} contract(s) at {self.commission.contract_rate}/contract"

            contract_desc += commission_desc
        
        return f"{contract_desc}. Their total pay is {self.get_pay()}"
        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', SalaryContract(4000))
print(billie)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(25, 100))
print(charlie)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', SalaryContract(3000), Commission("contract", 0, 4, 200))
print(renee)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(25, 150), Commission("contract", 0, 3, 220))
print(jan)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', SalaryContract(2000), Commission("bonus", 1500, 0, 0))
print(robbie)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(30, 120), Commission("bonus", 600, 0, 0))
print(ariel)
