from database_tools import (
    verify_customer,
    get_renewal_details,
    search_products,
    save_interest
)


print("\n--- CUSTOMER TEST ---")

customer = verify_customer("CUST1002")

print(customer)


print("\n--- RENEWAL TEST ---")

renewals = get_renewal_details("CUST1002")

print(renewals)


print("\n--- PRODUCT TEST ---")

products = search_products("Sports")

print(products)


print("\n--- INTEREST TEST ---")

interest = save_interest(
    "CUST1002",
    "Sports"
)

print(interest)