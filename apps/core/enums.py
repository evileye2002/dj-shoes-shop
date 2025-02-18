from django.db import models


class PaymentMethods(models.TextChoices):
    ONLINE_PAYMENT = "online", "Thanh toán trực tuyến"
    CASH_ON_DELIVERY = "cash", "Thanh toán khi nhận hàng"


class OrderStatus(models.TextChoices):
    PENDING = "pending", "Đang chờ"
    PREPARING = "preparing", "Đang chuẩn bị"
    SHIPPING = "shipping", "Đang vận chuyển"
    DELIVERED = "delivered", "Đã nhận"
    CANNCELED = "cannceled", "Đã huỷ đơn"


class Rating(models.IntegerChoices):
    ONE = 1, "1 sao"
    TWO = 2, "2 sao"
    THREE = 3, "3 sao"
    FOUR = 4, "4 sao"
    FIVE = 5, "5 sao"


PRODUCT_ORDER_CHOICES = {
    "newest": "-created_at",
    "increasep": "min_price",
    "decreasep": "-min_price",
    "treviews": "-total_reviews",
    "areviews": "-avg_review",
    "discounts": "-max_discount",
}
