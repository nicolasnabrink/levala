from rest_framework import serializers

from user.models import Company, Comment, Pedido

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['pedido', 'review', 'datetime', 'score']

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = ['user', 'company', 'datetime', 'body']

class CompanySerializer(serializers.ModelSerializer):
    pedido_set = PedidoSerializer(many=True)

    class Meta:
        model = Company
        fields = ['name', 'user', 'logoURL', 'cnpj', 'tel', 'job', 'city', 'pedido_set']