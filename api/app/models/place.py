from peewee import *
from base import BaseModel
from user import User
from city import City

class Place(BaseModel):
	owner = ForeignKeyField(User, related_name="places")
	city = ForeignKeyField(City, related_name="places")
	name = CharField(128, null=False)
	description = TextField()
	number_rooms = IntegerField(default=0)
	number_bathrooms = IntegerField(default=0)
	max_guest = IntegerField(default=0)
	price_by_night = IntegerField(default=0)
	latitude = FloatField()
	longitude = FloatField()

	# returns hash of all class attributes, inc. inherited ones
	def to_dict(self):
		owner = User.get(User.id == self.owner)
		city = City.get(City.id == self.city)

		return {	'id': self.id,
					'created_at': self.created_at.strftime('%Y/%m/%d %H:%M:%S'),
					'updated_at': self.updated_at.strftime('%Y/%m/%d %H:%M:%S'),
					'owner_id': owner.id,
					'city_id': city.id,
					'name': self.name,
					'description': self.description,
					'number_rooms': self.number_rooms,
					'number_bathrooms': self.number_bathrooms,
					'max_guest': self.max_guest,
					'price_by_night': self.price_by_night,
					'latitude': self.latitude,
					'longitude': self.longitude	}