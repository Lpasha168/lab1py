def run_tests():
    tests = [
        #исходные данные
        {
            "name": "1. Нулевой вес",
            "order": {"weight": 0, "total_price": 2000},
            "customer": {}, "address": {"type": "courier"},
            "expected_success": False
        },
        
        {
            "name": "2. Самовывоз",
            "order": {"weight": 10, "total_price": 2000},
            "customer": {}, "address": {"type": "pickup"},
            "expected_cost": 0.0, "expected_success": True
        },
        
        {
            "name": "3. VIP от 5000 руб",
            "order": {"weight": 12, "total_price": 5500},
            "customer": {"is_vip": True}, "address": {"type": "courier"},
            "expected_cost": 0.0, "expected_success": True
        },
       
        {
            "name": "4. Новый клиент (скидка 15%)",
            "order": {"weight": 4, "total_price": 2000},
            "customer": {"is_new": True}, "address": {"type": "courier"},
            "expected_cost": 255.0, "expected_success": True
        },
       
        {
            "name": "5. Отдаленный регион (+20%)",
            "order": {"weight": 10, "total_price": 2000},
            "customer": {}, "address": {"type": "region", "is_remote": True},
            "expected_cost": 2400.0, "expected_success": True
        },
       
        {
            "name": "6. Заказ от 10000 в обычный регион",
            "order": {"weight": 10, "total_price": 12000},
            "customer": {}, "address": {"type": "region", "is_remote": False},
            "expected_cost": 0.0, "expected_success": True
        },
       
        {
            "name": "7. Вес более 50 кг",
            "order": {"weight": 55, "total_price": 2000},
            "customer": {}, "address": {"type": "courier"},
            "expected_success": False
        },
       
        {
            "name": "8. Заказ менее 1000 руб",
            "order": {"weight": 5, "total_price": 500},
            "customer": {}, "address": {"type": "courier"},
            "expected_success": False
        }
    ]

    for t in tests:
        res = calculate_delivery_cost(t["order"], t["customer"], t["address"])
        if res["success"] != t["expected_success"]:
            print(f"FAIL: {t['name']} (Ожидался success={t['expected_success']}, получен {res['success']})")
        elif res["success"] and res["cost"] != t["expected_cost"]:
            print(f"FAIL: {t['name']} (Ожидалась стоимость {t['expected_cost']}, получена {res['cost']})")
        else:
            print(f"SUCCESS: {t['name']} -> {res}")

run_tests()
