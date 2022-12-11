from django import forms

# CSV File Upload Form
class CsvUploadForm(forms.Form):
    csv_file = forms.FileField()