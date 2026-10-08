import sender_stand_request
import data

def test_get_data_order():
    # создание заказа
    track = sender_stand_request.create_orders(data.order_body)
    # Получить заказ по его номеру
    res_get_data_order = sender_stand_request.get_orders_track(track)
    
    assert res_get_data_order.status_code == 200
