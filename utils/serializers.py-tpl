from rest_framework import serializers


class NullableCurrentUserDefault:
    requires_context = True

    def __call__(self, serializer_field):
        try:
            return serializer_field.context['request'].user
        except KeyError:
            return


class GenericCreationBaseSerializer(metaclass=serializers.SerializerMetaclass):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), allow_null=True
    )
