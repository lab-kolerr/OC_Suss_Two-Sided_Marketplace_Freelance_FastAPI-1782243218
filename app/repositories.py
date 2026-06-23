from sqlalchemy.orm import Session
from app.models import User, Service, Freelancer, Client, Project, Escrow, Payment, Review, Category, Notification
from app.schemas import UserCreate, ServiceCreate, FreelancerCreate, ClientCreate, ProjectCreate, EscrowCreate, PaymentCreate, ReviewCreate, CategoryCreate, NotificationCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: UserCreate):
        db_user = User(email=user.email, hashed_password=user.password)  # Hash password before saving
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id, User.isDeleted == False).first()

    def delete(self, user_id: int):
        user = self.get(user_id)
        if user:
            user.isDeleted = True
            self.db.commit()
            return user
        return None

class ServiceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, service: ServiceCreate):
        db_service = Service(title=service.title)
        self.db.add(db_service)
        self.db.commit()
        self.db.refresh(db_service)
        return db_service

    def get(self, service_id: int):
        return self.db.query(Service).filter(Service.id == service_id, Service.isDeleted == False).first()

    def delete(self, service_id: int):
        service = self.get(service_id)
        if service:
            service.isDeleted = True
            self.db.commit()
            return service
        return None

# Similar repository classes for Freelancer, Client, Project, Escrow, Payment, Review, Category, Notification