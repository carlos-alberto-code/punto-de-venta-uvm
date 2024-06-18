from controllers.controllers import PurchaseDetailController


controller = PurchaseDetailController()


purchase_details = [
    {"product_id": 1, "quantity": 2, "unit_purchase_price": 10.0, "total_unit_price": 20.0},
    {"product_id": 2, "quantity": 1, "unit_purchase_price": 15.0, "total_unit_price": 15.0},
]

purchase_data = {
    "supplier_id": 25,
    "date": "2022-01-01",
    "total": 35.0
}

controller.create_with_details(purchase_details, **purchase_data)