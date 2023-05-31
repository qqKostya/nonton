from typing import List


class Product:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name


class ProductsImpl:
    def __init__(self):
        self.product_list: List[Product] = []

    def addProduct(self, product: Product) -> bool:
        for p in self.product_list:
            if p.id == product.id:
                return False
        self.product_list.append(product)
        return True

    def deleteProduct(self, product: Product) -> bool:
        for p in self.product_list:
            if p.id == product.id:
                self.product_list.remove(p)
                return True
        return False

    def getName(self, id: str) -> str:
        for p in self.product_list:
            if p.id == id:
                return p.name
        return ""

    def findByName(self, name: str) -> List[str]:
        found_ids = []
        for p in self.product_list:
            if p.name == name:
                found_ids.append(p.id)
        return found_ids


products = ProductsImpl()

product1 = Product("1", "Apple")
product2 = Product("2", "Banana")
product3 = Product("3", "Apple")

print(products.addProduct(product1))
print(products.addProduct(product2))
print(products.addProduct(product3))

print(products.getName("2"))
print(products.getName("4"))

print(products.findByName("Apple"))
print(products.findByName("Orange"))
