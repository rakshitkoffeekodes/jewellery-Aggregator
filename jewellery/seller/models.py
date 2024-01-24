from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, Table, Date, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Admin(Base):
    __tablename__ = "auth_admin"

    admin_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(50))
    email = Column(String(50), unique=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    is_active = Column(Boolean, default=True)
    mobile_number = Column(Integer, default=True)
    gst_number = Column(String(50))
    shop_name = Column(String(50))
    address = Column(String(50))
    city = Column(String(50))
    state = Column(String(10))


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(60), primary_key=True, index=True, unique=True)
    password = Column(String(60))
    name = Column(String(60), nullable=True)
    surname = Column(String(60), nullable=True)
    role = Column(String(60))
    group = Column(String(60))
    register_date = Column(DateTime, default=func.now())
    user_permissions = relationship("UserPermission", back_populates="app")
    auth_group = relationship("Group", secondary="auth_user_groups", back_populates="users")

    @property
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class UserPermission(Base):
    __tablename__ = "user_permissions"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    permission_id = Column(Integer, ForeignKey("permission.id"), primary_key=True)
    user = relationship("User", back_populates="user_permissions")
    permission = relationship("Permission", back_populates="user_permissions")


class Group(Base):
    __tablename__ = "auth_group"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    users = relationship("app", secondary="auth_user_groups", back_populates="auth_group")
    group_permissions = relationship("Permission", secondary="auth_group_permissions", back_populates="groups")


auth_user_groups = Table(
    "auth_user_groups",
    Base.metadata,
    Column("user_id", ForeignKey("users.user_id"), primary_key=True),
    Column("group_id", ForeignKey("auth_group.id"), primary_key=True),
)


class Permission(Base):
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    codename = Column(String(50))
    user_permissions = relationship("UserPermission", back_populates="permission")
    groups = relationship("Group", secondary="auth_group_permissions", back_populates="group_permissions")


auth_group_permissions = Table(
    "auth_group_permissions",
    Base.metadata,
    Column("group_id", ForeignKey("auth_group.id"), primary_key=True),
    Column("permission_id", Integer, ForeignKey("permission.id"), primary_key=True),
)

auth_user_user_permissions = Table(
    "auth_user_user_permissions",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.user_id"), primary_key=True),
    Column("permission_id", Integer, ForeignKey("permission.id"), primary_key=True),
)


class UserDetails(Base):
    __tablename__ = 'UserDetails'
    user_details_id = Column(Integer, primary_key=True, index=True)
    mobile_number = Column(Integer, default=True)
    gst_number = Column(String(50), nullable=True)
    shop_name = Column(String(50), nullable=True)
    address = Column(String(50), nullable=True)
    city = Column(String(50), nullable=True)
    state = Column(String(10), nullable=True)
    # userid  = Column(String(10))
    # subuser = relationship("Subuser", primaryjoin="app.user_id == Subuser.user_id", cascade="all, delete-orphan")


class Order(Base):
    __tablename__ = "Order"

    order_id = Column(Integer, primary_key=True, index=True)
    product = Column(Integer, ForeignKey("Product.product_id"))
    buyer_user = Column(Integer, ForeignKey("UserDetails.user_details_id"))
    quantity = Column(Integer)
    commission = Column(Integer)
    total = Column(Integer)
    order_date = Column(Date)
    dispatch_date = Column(Date)
    status = Column(Boolean, default=True)


class RejectProduct(Base):
    __tablename__ = "RejectProduct"
    reject_product_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("Product.product_id"))
    raason = Column(String(100))


class Rating(Base):
    __tablename__ = "Rating"

    rating_id = Column(Integer, primary_key=True, index=True)
    product = Column(Integer, ForeignKey("Product.product_id"))
    user = Column(Integer, ForeignKey("UserDetails.user_details_id"))
    rating = Column(Integer)
    rating_message = Column(String(50))


class ProductCategory(Base):
    __tablename__ = 'product_category'

    product_category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, default='jewelry')
    parent_category_id = Column(Integer, ForeignKey('product_category.product_category_id'), nullable=True)
    parent_category = relationship('ProductCategory', remote_side=[product_category_id])


product_purity_association = Table(
    "ProductPurity",
    Base.metadata,
    Column("product_id", Integer, ForeignKey("Product.product_id")),
    Column("purity_id", Integer, ForeignKey("Purity.purity_id")),
)

product_metal_association = Table(
    "ProductMetal",
    Base.metadata,
    Column("product_id", Integer, ForeignKey("Product.product_id")),
    Column("metal_id", Integer, ForeignKey("Metal.metal_id")),
)


class Metal(Base):
    __tablename__ = 'Metal'
    metal_id = Column(Integer, primary_key=True, index=True)
    metal_name = Column(String(50), )
    products = relationship("Product", secondary=product_metal_association, back_populates="metals")


class Purity(Base):
    __tablename__ = 'Purity'
    purity_id = Column(Integer, primary_key=True, index=True)
    purity_group_name = Column(String(50), )
    purity = Column(String(50), )
    products = relationship("Product", secondary=product_purity_association, back_populates="purities")


class Product(Base):
    __tablename__ = 'Product'
    product_id = Column(Integer, primary_key=True, index=True)
    images = Column(LargeBinary)
    product_name = Column(String(50))
    net_weight = Column(Integer)
    base_metal = Column(String(50))
    plating = Column(String(50))
    diamonds = Column(String(50))
    karats = Column(String(50))
    # price = Column(Integer)
    quantity = Column(Integer)
    stock = Column(String(10), default="Is Stock")
    # category = Column(String(50))
    manufacturing_id = Column(String(10))
    description = Column(String(100))
    listing_user = Column(Integer, ForeignKey("UserDetails.user_details_id"))

    purities = relationship("Purity", secondary=product_purity_association, back_populates="products")
    metals = relationship("Metal", secondary=product_metal_association, back_populates="products")
