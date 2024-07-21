from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from datetime import datetime, timedelta
import plaid
from uuid import uuid4
from .models import User
from .utils import get_plaid_client
from .tasks import get_transactions, get_accounts, get_access_token

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ('id', 'name')