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

        store_name = validated_data['store_name']
        address = validated_data['address']

        store = Store.objects.create(user = request.user, store_name = store_name, address = address)

        link = str(f"http://127.0.0.8000/{store_name}/{store.id}").replace(' ','')
        store.store_link = link
        store.save()
        return store


# class CreateStoreHyperLinkedSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Store
#         fields = ['url','store_name', 'address', 'store_link','id']
#         write_only_fields = ['store_name', 'address']
#         read_only_fields = ['id', 'store_link', 'url']

#         def create(self, validated_data):
            

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['store','product_name', 'description', 'mrp', 'sale_price', 'category'] 
