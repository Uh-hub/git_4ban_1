from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    # 클래스 상속
    def __init__(self, *args, **kwargs): #오버라이딩
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True