from rest_framework import serializers
from .models import Movie, Genre


# class ReviewListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ('title','content',)


# 필요한가?
class MovieTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)

# 필요한가?
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title','overview',)

# 필요
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
    

# class ActorListSerializer(serializers.ModelSerializer):
#     movie_set = MovieTitleSerializer(many=True)
#     class Meta:
#         model = Actor
#         fields = '__all__'
#         # read_only_fields = ('movie_set',)

# 필수
class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'


# class ReviewDetailSerializer(serializers.ModelSerializer):
#     movie = MovieTitleSerializer(read_only = True)
#     class Meta:
#         model = Review
#         fields = '__all__'
#         # read_only_fields = ('movie',)


