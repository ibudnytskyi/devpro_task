from generator.generator import generate_sample_data
from utils.products_items import get_all_product_names, get_products_above_threshold


def test_get_all_product_names():
    data = generate_sample_data()
    names = get_all_product_names(data)

    expected_names = ["Pizza", "Sushi", "Burger", "Pad Thai"]

    print("All product names:", names)

    assert len(names) == len(expected_names)
    assert all(name in names for name in expected_names)


def test_get_products_above_threshold():
    data = generate_sample_data()
    threshold = 15.0
    products_above_threshold = get_products_above_threshold(data, threshold)

    assert all(product["price"] >= threshold for product in products_above_threshold)

    expected_products = [
        {"id": 2, "name": "Sushi", "category": "Japanese", "price": 24.99}

    ]

    print("Expected products:", expected_products)
    print("Actual products:", products_above_threshold)

    assert len(products_above_threshold) == len(expected_products)
    assert all(expected_product in products_above_threshold for expected_product in expected_products)
