from database.connection import get_db
from database.models import (
    Product as ProductModel,
    Sale as SaleModel,
    SaleDetail as SaleDetailModel
)

from business_objects.Sale import Sale as SaleBusinessObject


class SalesRegisterManagement:

    def __init__(self) -> None:
        with get_db() as session:
            self._session = session

    
    def register_sale(self, sale: SaleBusinessObject) -> None:
        # Se registra la venta
        self._session.add(
            SaleModel(
                date=sale.date,
                total= sale.total,
            )
        )
        self._session.commit()

        # Se obtiene el id de la venta registrada
        sale_id = self._session.query(SaleModel).order_by(SaleModel.id.desc()).first().id # type: ignore

        # Se registran los detalles de la venta
        for detail in sale.details:
            self._session.add(
                SaleDetailModel(
                    sale_id=sale_id,
                    product_id=detail.product.product_id,
                    quantity=detail.quantity,
                    unit_sale_price=detail.unit_price,
                    total_unit_price=detail.total_price,
                )
            )
        self._session.commit()

        # Se actualiza el stock de los productos
        for detail in sale.details:
            # Iteramos sobre los detalles de la venta para acceder a los productos y hacemos update de los stocks
            self._session.query(ProductModel).filter(ProductModel.id == detail.product.product_id).update(
                {
                    'quantity': ProductModel.quantity - detail.quantity
                }
            )
        self._session.commit()
