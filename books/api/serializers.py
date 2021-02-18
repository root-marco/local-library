from rest_framework import serializers
from books import models


class BooksSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Books
		field = '__all__'
