import csv

from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path

from .models import Spell
from .forms import CsvUploadForm


@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
    change_list_template = "spells/spell_changelist.html"

    def get_urls(self):
        admin_urls = super().get_urls()
        custom_urls = [
            path('upload_csv/', self.upload_csv),
        ]
        return custom_urls + admin_urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]

            reader = csv.DictReader(csv_file)

            for row in reader:
                new_spell = Spell()
            # Create Hero objects from passed in data

            self.message_user(request, "CSV file uploaded")
            return redirect("..")
        form = CsvUploadForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )
    
    def validate_csv(self, csv_file):
        reader = csv.reader(csv_file)
        reader[0]