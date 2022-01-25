import csv
from datetime import datetime

def main():
    try:
        tax_percent = 0.06

        print("Inkom Emporium\n")
        current_date_and_time = datetime.now()
        #print(f"{current_date_and_time:%A %I:%M %p}")
        
        prod_file = "products.csv"
        req_file = "request.csv"
        prod_dict = read_products(prod_file)
        # for line in prod_dict.items():
        #     print(line)
        #print('\nPurchased Items:\n')
        subtotal, item_count = process_request(req_file, prod_dict)
        print(f'\nNumber of Items: {item_count}')
        print(f'Subtotal: {subtotal:.2f}')
        tax_amount, final_total = compute_total(subtotal, tax_percent)
        print(f'Sales Tax: {tax_amount:.2f}')
        print(f'Total: {final_total:.2f}')
        print('\nThank you for shopping at the Inkom Emporium.')
        print(f"{current_date_and_time:%A %I:%M %p}")
    except FileNotFoundError:
        print('Error: File not found')
    except PermissionError:
        print('Error: User does not have the necessary permissions to access this file')
    except KeyError:
        print('Error: Incorrect key')

def read_products(prod_file):
    products = {}
    with open(prod_file, 'rt') as prod_csv:
        reader = csv.reader(prod_csv)
        next(reader)
        for row in reader:
            key = row[0]
            products[key] = [row[1], float(row[2])]
    return products

def process_request(req_file, prod_dict):
    with open(req_file, mode='rt') as req_csv:
        reader = csv.reader(req_csv)
        next(reader)
        subtotal = 0
        item_count = 0
        for row in reader:
            prod_line = prod_dict[row[0]]
            prod_name = prod_line[0]
            prod_quantity = int(row[1])
            single_price = prod_line[1]
            total_price = prod_quantity * prod_line[1]
            subtotal += total_price
            item_count += prod_quantity
            print(f'{prod_name}: {prod_quantity} @ {single_price:.2f}')
    return subtotal, item_count

def compute_total(subtotal, tax_percent):
    tax_amount = subtotal * tax_percent
    final_total = subtotal + tax_amount
    return tax_amount, final_total

if __name__ == "__main__":
    main()