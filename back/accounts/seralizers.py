from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


# class MovieTitleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ('title',)


# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ('title','overview',)


# class ActorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Actor
#         fields = '__all__'
    

# class ActorListSerializer(serializers.ModelSerializer):
#     movie_set = MovieTitleSerializer(many=True)
#     class Meta:
#         model = Actor
#         fields = '__all__'
#         # read_only_fields = ('movie_set',)


# class MovieDetailSerializer(serializers.ModelSerializer):
#     actors = ActorSerializer(many=True)
#     review_set = ReviewListSerializer(many=True)
#     class Meta:
#         model = Movie
#         fields = '__all__'


# class ReviewDetailSerializer(serializers.ModelSerializer):
#     movie = MovieTitleSerializer(read_only = True)
#     class Meta:
#         model = Review
#         fields = '__all__'
#         # read_only_fields = ('movie',)

