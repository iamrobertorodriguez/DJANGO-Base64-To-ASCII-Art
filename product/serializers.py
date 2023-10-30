from rest_framework import serializers

class ConversionSerializer(serializers.Serializer):
    base_64 = serializers.CharField(
        max_length=None,
        allow_blank=False,
        help_text="Base64 value that you wish to turn into ASCI Art."
    )
    size = serializers.CharField(
        max_length=None,
        allow_blank=False,
        help_text="Size of the result, allowed values are: xs, s, md, lg, xl."
    )

class ConversionResponseSerializer(serializers.Serializer):
    ascii_art = serializers.CharField(
        max_length=None,
        allow_blank=True,
        help_text="Your ASCII art."
    )
