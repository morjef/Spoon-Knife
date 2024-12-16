import random
import time
import os

def generate_random_data(num_items):
  """
  Generates a list of random dictionaries, 
  where each dictionary represents a product with 
  random attributes.

  Args:
    num_items: The number of products to generate.

  Returns:
    A list of dictionaries, where each dictionary 
    represents a product.
  """
  products = []
  for _ in range(num_items):
    product = {
        "name": "".join(random.choices(string.ascii_letters, k=10)),
        "price": round(random.uniform(10, 100), 2),
        "category": random.choice(["electronics", "clothing", "books", "food"]),
        "stock": random.randint(0, 100),
        "rating": round(random.uniform(1, 5), 1)
    }
    products.append(product)
  return products

def filter_products(products, category, min_stock):
  """
  Filters a list of products based on category and minimum stock.

  Args:
    products: A list of product dictionaries.
    category: The category to filter by (optional).
    min_stock: The minimum stock level to filter by (optional).

  Returns:
    A filtered list of products.
  """
  filtered_products = []
  for product in products:
    if category and product["category"] != category:
      continue
    if min_stock and product["stock"] < min_stock:
      continue
    filtered_products.append(product)
  return filtered_products

def sort_products(products, sort_by):
  """
  Sorts a list of products based on a given attribute.

  Args:
    products: A list of product dictionaries.
    sort_by: The attribute to sort by ("name", "price", "stock", "rating").

  Returns:
    A sorted list of products.
  """
  return sorted(products, key=lambda x: x[sort_by])

def main():
  """
  Generates random product data, filters it, sorts it, 
  and displays the results.
  """
  num_products = 100
  products = generate_random_data(num_products)

  print(f"Generated {num_products} random products.")

  filtered_products = filter_products(products, category="electronics", min_stock=50)
  print(f"Filtered products: {len(filtered_products)}")

  sorted_products = sort_products(filtered_products, "price")
  print("Sorted products by price:")
  for product in sorted_products:
    print(product)

if __name__ == "__main__":
  start_time = time.time()
  main()
  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"Execution time: {elapsed_time:.2f} seconds")
