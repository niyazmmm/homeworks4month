from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(min_length=5, max_length=254)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField()


class CommentCreateForm(forms.Form):
    text = forms.CharField(max_length=400)

