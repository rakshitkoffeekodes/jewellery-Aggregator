from sqlalchemy import LargeBinary, Date
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()
from seller.database import Base


class Admin(Base):
    __tablename__ = "admin"

    admin_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(50))
    email = Column(String(50), unique=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    # is_active = Column(Boolean, default=True)
    # is_superuser = Column(Boolean, default=False)
    mobile_number = Column(Integer, default=True)
    gst_number = Column(String(50))
    shop_name = Column(String(50))
    address = Column(String(50))
    city = Column(String(50))
    state = Column(String(10))


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_email = Column(String(60), primary_key=True, index=True, unique=True)
    user_password = Column(String(60))
    user_name = Column(String(60), )
    user_surname = Column(String(60), )
    user_mobile_number = Column(Integer, )
    user_gst_number = Column(String(50), nullable=True)
    user_shop_name = Column(String(50), nullable=True)
    user_address = Column(String(50), nullable=True)
    user_city = Column(String(50), nullable=True)
    user_state = Column(String(10), nullable=True)
    role = Column(String(60))
    register_date = Column(DateTime, default=func.now())
    permissions = relationship('Permission', secondary='user_permissions', back_populates='users')

    # group = Column(String(60))

    @property
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class UserPermission(Base):
    __tablename__ = "user_permissions"

    user_permissions_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    permission_id = Column(Integer, ForeignKey("auth_permissions.id"), primary_key=True)


class Permission(Base):
    __tablename__ = "auth_permissions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    codename = Column(String(50))
    users = relationship('User', secondary='user_permissions', back_populates='permissions')


class UserRequest(Base):
    __tablename__ = 'user_requests'
    user_request_id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), default='pending')
    description = Column(String(50), default='')
    user_id = Column(Integer, ForeignKey("users.user_id"))


class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True, index=True)
    product_images = Column(LargeBinary)
    product_name = Column(String(50))
    net_weight = Column(Integer)
    product_base_metal = Column(String(50))
    product_carats = Column(String(50))
    plating = Column(String(50))
    quantity = Column(Integer)
    # category = Column(String(50))
    manufacturing_id = Column(String(10))
    caratsync_id = Column(String(10))
    product_description = Column(String(100))
    is_accept = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("User.user_id"))
    metal_purity_id = Column(Integer, ForeignKey("metal_purity.metal_purity_id"))
    product_category_id = Column(Integer, ForeignKey("product_category.product_category_id"))


class Metal(Base):
    __tablename__ = 'metal'
    metal_id = Column(Integer, primary_key=True, index=True)
    metal_name = Column(String(50), )


class MetalPurity(Base):
    __tablename__ = 'metal_purity'
    metal_purity_id = Column(Integer, primary_key=True, index=True)
    purity_group_name = Column(String(50), )
    purity = Column(String(50), )
    metal_id = Column(Integer, ForeignKey("metal.metal_id"))


class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    commission = Column(Integer)
    total = Column(Integer)
    order_date = Column(Date)
    dispatch_date = Column(Date)
    status = Column(Boolean, default=True)
    product = Column(Integer, ForeignKey("Product.product_id"))
    buyer = Column(Integer, ForeignKey("User.user_id"))
    seller = Column(Integer, ForeignKey("User.user_id"))


class Rating(Base):
    __tablename__ = "rating"
    rating_id = Column(Integer, primary_key=True, index=True)
    product = Column(Integer, ForeignKey("Product.product_id"))
    buyer = Column(Integer, ForeignKey("User.user_id"))
    rating = Column(Integer)
    rating_message = Column(String(50))


class ProductCategory(Base):
    __tablename__ = 'product_category'
    product_category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, default='jewelry')
    parent_category_id = Column(Integer, ForeignKey('product_category.product_category_id'), nullable=True)
    parent_category = relationship('ProductCategory', remote_side=[product_category_id])
