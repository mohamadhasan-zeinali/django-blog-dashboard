from rest_framework import viewsets
from . serializers import *
from reviews.models import *
from rest_framework.permissions import IsAuthenticated
from django.core.mail import  send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.response import  Response

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article_model.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


# forget password request endpoint
class ForgetPasswordEmail(viewsets.ModelViewSet):
    http_method_names = ['get', 'create', 'post']
    serializer_class = ForgetPasswordSerializer
    queryset = User.objects.none()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')  # extract email from serializer
        user = User.objects.filter(email=email).first()
        if user:
            token = PasswordResetTokenGenerator().make_token(user)
            protocol = request.scheme
            host = request.get_host()
            reset_password_url = f"{protocol}://{host}/{token}"
            send_mail(
                'Reset your password',
                f'Please click the link to reset your password {reset_password_url}',
                '{your email goes here}',
                [email],
                fail_silently=False,
            )
            return Response({'email': f'reset password sent successfully to: {email}'})
        return Response({'email': 'your email dosnt exist'})