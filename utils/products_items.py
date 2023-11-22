
def get_all_product_names(data):
    return [product["name"] for product in data["products"]]


def get_products_above_threshold(data, threshold):
    return [product for product in data["products"] if product["price"] >= threshold]
