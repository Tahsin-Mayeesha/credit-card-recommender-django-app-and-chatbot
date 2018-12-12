from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "your full name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "your email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "your message"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email
    
    

class PreferenceForm(forms.Form):
    
    CARD_TYPE_CHOICES = (
    ('credit', 'Credit'),
    ('debit', 'Debit'),
    ('prepaid', 'Prepaid'),
    )
    
    BANK_CHOICES = (('Sonali Bank Limited','Sonali Bank Limited'),
                    ('Janata Bank Limited','Janata Bank Limited'),
                    ('Agrani Bank Limited','Agrani Bank Limited'),
                    ('Rupali Bank Limited','Rupali Bank Limited'),
                    ('Bangladesh Krishi Bank','Bangladesh Krishi Bank'),
                    ('AB Bank','AB Bank'),
                    ('Bank Asia Limited','Bank Asia Limited'),
                    ('BRAC Bank Limited','BRAC Bank Limited'),
                    ('City Bank Limited','City Bank Limited'),
                    ('Dhaka Bank','Dhaka Bank'),
                    ('Dutch Bangla Bank Limited','Dutch Bangla Bank Limited'),
                    ('IFIC Bank Limited','IFIC Bank Limited'),
                    ('Jamuna Bank Limited','Jamuna Bank Limited'),
                    ('Meghna Bank','Meghna Bank'),
                    ('Midland Bank','Midland Bank'),
                    ('Modhumoti Bank','Modhumoti Bank'),
                    ('Mutual Trust bank Limited','Mutual Trust bank Limited'),
                    ('National Credit and Commerce Bank Limited','National Credit and Commerce Bank Limited'),
                    ('NRB Bank Limited','NRB Bank Limited'),
                    ('NRB Commercial Bank Limited','NRB Commercial Bank Limited'),
                    ('Prime Bank','Prime Bank'),
                    ('Trust Bank','Trust Bank'),
                    ('Pubali Bank Limited','Pubali Bank Limited'),
                    ('United Commercial Bank Limited','United Commercial Bank Limited'),
                    ('Standard Charter','Standard Charter Bank'),
                    ('One Bank','One Bank'),
                    ('Premier Bank','Premier Bank')
                    )
    
    REWARD_CHOICES = (("international_transaction_available","International Transaction"),
                      ("balance_transfer_available","Balance Transfer"),
                      ("dual_currency","Dual Currency"),
                      ("reward_supplementary_card","Supplementary Card"),
                      ("reward_airport_lounge","Airport Lounge"),
                      ("reward_cashback_available","Cashback Available"),
                      ("reward_luxary_resort_hotel","Luxary Resort/Hotel"),
                      ("reward_insurance_plan","Insurance Program"),
                      ("reward_travel_benefits","Travel Benefits"),
                      ("reward_fine_dining","Fine Dining"),
                      ("reward_buffet_discount","Buffet Discount"),
                      ("reward_medical_discount","Medical Discount"),
                      ("reward_shopping","Shopping Points"),
                      ("reward_airlines_ticket","Air Travel Ticket Discount"),
                      ("reward_point_program","Loyalty Points Program"),
                      ("reward_emi_available","EMI Discount")
                      )

    name = forms.CharField(label = "Name")
    age = forms.IntegerField(label="Age")
    address = forms.CharField(label="Address")
    card_type = forms.ChoiceField(choices = CARD_TYPE_CHOICES, widget = forms.RadioSelect, label="Card Type")
    
    
    #bank = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
     #                                choices=BANK_CHOICES,
     #                                label="Choose preferred banks among the currently supported ones.")
    
    #rewards = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
    #                                    choices=REWARD_CHOICES,
    #                                    label = "Choose the required rewards.")

    