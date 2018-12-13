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
    ('card_type_Credit', 'Credit'),
    ('card_type_Debit', 'Debit'),
    ('card_type_Prepaid', 'Prepaid'),
    )
    
    BANK_CHOICES = (('bank_name_Sonali Bank Limited','Sonali Bank Limited'),
                    ('bank_name_Janata Bank Limited','Janata Bank Limited'),
                    ('bank_name_Agrani Bank Limited','Agrani Bank Limited'),
                    ('bank_name_Rupali Bank Limited','Rupali Bank Limited'),
                    ('bank_name_Bangladesh Krishi Bank','Bangladesh Krishi Bank'),
                    ('bank_name_AB Bank','AB Bank'),
                    ('bank_name_Bank Asia Limited','Bank Asia Limited'),
                    ('bank_name_BRAC Bank Limited','BRAC Bank Limited'),
                    ('bank_name_City Bank Limited','City Bank Limited'),
                    ('bank_name_Dhaka Bank','Dhaka Bank'),
                    ('bank_name_Dutch Bangla Bank Limited','Dutch Bangla Bank Limited'),
                    ('bank_name_IFIC Bank Limited','IFIC Bank Limited'),
                    ('bank_name_Jamuna Bank Limited','Jamuna Bank Limited'),
                    ('bank_name_Meghna Bank','Meghna Bank'),
                    ('bank_name_Midland Bank','Midland Bank'),
                    ('bank_name_Modhumoti Bank','Modhumoti Bank'),
                    ('bank_name_Mutual Trust bank Limited','Mutual Trust bank Limited'),
                    ('bank_name_National Credit and Commerce Bank Limited','National Credit and Commerce Bank Limited'),
                    ('bank_name_NRB Bank Limited','NRB Bank Limited'),
                    ('bank_name_NRB Commercial Bank Limited','NRB Commercial Bank Limited'),
                    ('bank_name_Prime Bank','Prime Bank'),
                    ('bank_name_Trust Bank','Trust Bank'),
                    ('bank_name_Pubali Bank Limited','Pubali Bank Limited'),
                    ('bank_name_United Commercial Bank Limited','United Commercial Bank Limited'),
                    ('bank_name_Standard Charter','Standard Charter Bank'),
                    ('bank_name_One Bank','One Bank'),
                    ('bank_name_Premier Bank','Premier Bank')
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
                      ("reward_emi_available","EMI Discount"),
                      ("hajj_card","Hajj")
                      )
    
    VISA_VS_MASTERCARD_CHOICES = (("is_visa","Visa"),
                                 ("is_mastercard","Mastercard"),)
                                 
    INTEREST_RATE_CHOICES = (("'interest_rate_1-10","1-10%"),
                              ("interest_rate_11-20", "11-20%"),
                              ("interest_rate_21-30", "21-30%"),
                              ("interest_rate_zero","zero%(For debit cards)"))


    CREDIT_LIMIT_CHOICES = (("max_credit_limit_0-100000", "0 to 1 Lakh"),
                            ("max_credit_limit_100000-500000","1 to 5 Lakh"), 
                            ("max_credit_limit_1000000+", "More than 10 Lakh"),
                            ("max_credit_limit_N/A", "Not Applicable(For Debit Cards)"),
                            ('max_credit_limit_unknown', "Unknown Ok"))
    
    name = forms.CharField(label = "Name")
    age = forms.IntegerField(label="Age")
    Occupation = forms.CharField(label="Occupation")
    address = forms.CharField(label="Address")
    
    card_type = forms.MultipleChoiceField(choices = CARD_TYPE_CHOICES, 
                                          widget = forms.CheckboxSelectMultiple, label="Card Type")
    
    interest_rate = forms.MultipleChoiceField(choices=INTEREST_RATE_CHOICES,
                                      widget = forms.CheckboxSelectMultiple,
                                      label = "Interest Rate")
    
    max_credit_limit = forms.MultipleChoiceField(choices=CREDIT_LIMIT_CHOICES,
                                                 widget = forms.CheckboxSelectMultiple,
                                                 label = "Choose Credit Limit"
                                                 )
    
    visa_vs_mastercard = forms.MultipleChoiceField(choices=VISA_VS_MASTERCARD_CHOICES,
                                           widget = forms.CheckboxSelectMultiple,
                                           label = "Visa/Mastercard")
    
    bank = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                     choices=BANK_CHOICES,
                                     label="List of supported banks",required=False)
    
    rewards = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                        choices=REWARD_CHOICES,
                                        label = "Rewards",required=False)
    
    

    