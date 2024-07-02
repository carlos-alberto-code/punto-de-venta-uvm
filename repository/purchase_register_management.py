from database.connection import get_db
from database.models import (
    Product as ProductModel,
    Purchase as PurchaseModel,
    PurchaseDetail as PurchaseDetailModel
)
from business_objects.Purchase import Purchase as PurchaseBusinessObject

class PurchaseRegisterManagement:
    def __init__(self) -> None:
        with get_db() as session:
            self._session = session

    def register_purchase(self, purchase: PurchaseBusinessObject) -> None:
        # Registrar la compra
        self._session.add(
            PurchaseModel(
                date=purchase.date,
                total=purchase.total,
            )
        )
        self._session.commit()

        # Obtener el id de la compra registrada
        purchase_id = self._session.query(PurchaseModel).order_by(PurchaseModel.id.desc()).first().id  # type: ignore

        # Registrar los detalles de la compra
        for detail in purchase.details:
            self._session.add(
                PurchaseDetailModel(
                    purchase_id=purchase_id,
                    product_id=detail.product.product_id,
                    quantity=detail.quantity,
                    unit_purchase_price=detail.unit_purchase_price,
                    total_unit_price=detail.total_purchase_price,
                )
            )
        self._session.commit()

        # Actualizar el stock de los productos
        for detail in purchase.details:
            self._session.query(ProductModel).filter(ProductModel.id == detail.product.product_id).update(
                {
                    'quantity': ProductModel.quantity + detail.quantity
                }
            )
        self._session.commit()
