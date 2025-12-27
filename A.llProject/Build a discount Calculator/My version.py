print("-"*50)#-------------------------------------------------------------------

#Question1:In Python type hints are optional signals 
#that tell other developers what the data type of a variable or function
#is expected to be.

#Question2:Import for the List type from the typing module:
#Give a way to manage multiple discount strategies 
#and find the best price.
#This allows you to specify that a function parameter 
#is a list containing specific types of objects.

print("-"*50)#-------------------------------------------------------------------


from abc import ABC, abstractmethod
from typing import List

class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name} - ${self.price}'

class DiscountStrategy(ABC):
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        pass

    @abstractmethod
    def add_discount_name(self,product:Product)->str:
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        pass

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: int) -> None:
        self.percent = percent

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return self.percent <= 70
    
    def add_discount_name(self,product:Product)->str:
        return "PercentageDiscount"

    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.percent / 100)

class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return product.price * 0.9 > self.amount
    
    def add_discount_name(self,product:Product)->str:
        return "FixedAmountDiscount"

    def apply_discount(self, product: Product) -> float:
        return product.price - self.amount


class PremiumUserDiscount(DiscountStrategy):
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return user_tier.lower() == 'premium'
    
    def add_discount_name(self,product:Product)->str:
        return "PremiumUserDiscount"
    
    def apply_discount(self, product: Product) -> float:
        return product.price * 0.8
    


class DiscountEngine:
    def __init__(self, strategies:List[DiscountStrategy]) -> None:
        self.strategies = strategies
    
    def calculate_best_price(self, product: Product, user_tier: str) -> float:
        discount_name=[product.name]
        prices = [product.price]

        for strategy in self.strategies:
            if strategy.is_applicable(product, user_tier):

                discount_name.append(strategy.add_discount_name(product))

                discounted = strategy.apply_discount(product)
                prices.append(discounted)
        index=prices.index(min(prices))
        return (discount_name[index],min(prices))

if __name__ == '__main__':
    product = Product('Wireless Mouse', 50.0)
    user_tier = 'Premium'

    strategies = [
        PercentageDiscount(60),
        FixedAmountDiscount(5),
        PremiumUserDiscount()
    ]

    engine = DiscountEngine(strategies)
    best_way,best_price = engine.calculate_best_price(product, user_tier)
    print(
f"Best Way for {product.name} for {user_tier} user is: ${best_way}\n\
Best price for {product.name} for {user_tier} user: ${best_price:.2f}")


#re-read and optimize this project

