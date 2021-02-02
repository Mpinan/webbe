from app import db
from sqlalchemy.exc import IntegrityError

class Review(db.Model):

    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    review_name = db.Column(db.String(128), nullable=False)
    review_text = db.Column(db.String(255))


    def __init__(self, review_name, review_text):

        self.review_name = review_name
        self.review_text = review_text


    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
            return True, self.id
        except IntegrityError:
            return False, None

    def delete(review_id):
        review_to_delete = Review.query.filter_by(id=review_id).first()
        db.session.delete(review_to_delete)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            return False

    @staticmethod
    def get_all_reviews():
      return Review.query.all()
    
    @staticmethod
    def get_one_review(id):
      return BlogpostModel.query.get(id)

    def __repr__(self):
      return '<id {}>'.format(self.id)

    @property
    def reviews_serializer(review):
      return {
        'id': review.id,
        'review_name': review.review_name,
        'review_text': review.review_text,
        }
