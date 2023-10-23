

from django import forms
from Dumper.models import Post, Comments

class PostFormClass(forms.ModelForm):
    """ With this class, Django provides us functionality to create forms and save the user input
    directly into the models we assign. In this class, we are creating the Form to save data into
    :var 'model = Post' """
    class Meta():
        model = Post
        # We are adding the functionality to take in below information from the user.
        fields = ('author', 'title', 'text')

        # CSS Functionality can be added to below-mentioned classes.
        widgets = {
            'title' : forms.TextInput(attrs={'class':'textinputclass'}),
            'text' : forms.Textarea(attrs={'class' : 'editable medium-editor-textarea postcontent'})
        }


class CommentsFormClass(forms.ModelForm):

    class Meta():
        model = Comments
        fields = ('author', 'text')

        widgets = {
            'author' : forms.TextInput(attrs={'class' : 'textinputclass'}),
            'text' : forms.Textarea(attrs={'class' : 'editable medium-editor-textarea'})
        }