from django import forms


class JobApplicationForm(forms.Form):
    EMPLOYMENT_TYPES = (
        ("", "Please choose"),
        ("ft", "Full-time"),
        ("pt", "Part-time"),
        ("contract", "Contract work"),
    )

    DAYS = (
        (1, "Mon"),
        (2, "Tue"),
        (3, "Wed"),
        (4, "Thu"),
        (5, "Fri"),
    )

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required=False)

    employment_type = forms.ChoiceField(
        choices=EMPLOYMENT_TYPES
    )

    start_date = forms.DateField(
        help_text="The earliest date you can start working."
    )

    available_days = forms.MultipleChoiceField(
        choices=DAYS,
        help_text="Select all days that you can work."
    )

    desired_hourly_wage = forms.DecimalField()
    cover_letter = forms.CharField(widget=forms.Textarea)

    confirmation = forms.BooleanField(
        label="I certify that the information I have provided is true."
    )
