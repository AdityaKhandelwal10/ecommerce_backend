from rest_framework import serializers

from .models import Store, Category, Product


class CreateStoreSerializer(serializers.ModelSerializer):
    """
    Helps create the store object and saves with the user
    """
    class Meta:
        model = Store
        fields = ['store_name', 'address', 'store_link','id']
        write_only_fields = ['store_name', 'address']
        read_only_fields = ['id', 'store_link']

    
        
    def create(self, validated_data):

        request = self.context.get("request")

        print(validated_data)

        store = Store.objects.create(user = request.user, store_name = validated_data['store_name'], address = validated_data['address'])
        # store.store_name = validated_data['store_name']
        # store.address = validated_data['address']
        # store.user = request.user
        store.store_link  = './store_link'
        store.save()
        return store

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

        