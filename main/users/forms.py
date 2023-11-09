from django import forms#forms  из Django, который предоставляет классы для создания форм.


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')#Максимальная длина поля установлена на 100 символов
    #Оба поля имеют виджет  forms.PasswordInput , который скрывает введенные символы пароля. Метки для полей установлены на "Password" и "Confirm Password" соответственно.
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput,
                                       label='Confirm Password')

    def clean(self):
        cleaned_data = super().clean()# super()  используется для обращения к родительскому классу,
        # а  clean()  - это метод родительского класса  forms.Form ,
        # который выполняет очистку и валидацию данных формы по установленным правилам.
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")


