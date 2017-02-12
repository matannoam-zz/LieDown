from ..extensions import schemas


class AddressSchema(schemas.Schema):

    first_name = schemas.String()
    last_name = schemas.String()
    street_1 = schemas.String()
    street_2 = schemas.String()
    city = schemas.String()
    state = schemas.String()
    zip_code = schemas.String()
    phone_number = schemas.String()

    birthdate = schemas.Date()


class OrderSchema(schemas.Schema):

    order_id = schemas.String()
    shipping_address = schemas.Nested(AddressSchema)
    billing_address = schemas.Nested(
        AddressSchema, exclude=['phone_number'])

    placed = schemas.DateTime()
