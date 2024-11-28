from file_handler import ProductFH
from models import Product

pfh1 = ProductFH(Product(1, "notebook"))
pfh1.add_in_file()

pfh2 = ProductFH(Product(2, "mouse"))
pfh2.add_in_file()

