from sklearn.externals import joblib
from feature_preprocessing import feature_maps
import numpy as np
import pandas as pd
import os

user_input = {'visaVsMasterCard': ['mastercard'], 
              'card-type': ['credit'], 'BankName': ['IFIC Bank'], 
              'reward': ['fine dining'], 
              'InterestRate': [], 
              'CreditLimit': []}

cards = pd.read_csv("data.csv")

def get_card_names(indices):
    return cards.iloc[indices[0],:]["card_name"]
    


feature_list = ['international_transaction_available', 'balance_transfer_available',
       'dual_currency', 'reward_supplementary_card', 'reward_airport_lounge',
       'reward_cashback_available', 'reward_luxary_resort_hotel',
       'reward_insurance_plan', 'reward_travel_benefits', 'reward_fine_dining',
       'reward_buffet_discount', 'reward_medical_discount', 'reward_shopping',
       'reward_airlines_ticket', 'reward_point_program',
       'reward_emi_available', 'hajj_card', 'is_visa', 'is_mastercard',
       'bank_name_AB Bank', 'bank_name_Agrani Bank Limited',
       'bank_name_BRAC Bank Limited', 'bank_name_Bangladesh Krishi Bank',
       'bank_name_Bank Asia Limited', 'bank_name_City Bank Limited',
       'bank_name_Dhaka Bank', 'bank_name_Dutch Bangla Bank Limited',
       'bank_name_IFIC Bank Limited', 'bank_name_Jamuna Bank Limited',
       'bank_name_Janata Bank Limited', 'bank_name_Meghna Bank',
       'bank_name_Midland Bank', 'bank_name_Modhumoti Bank',
       'bank_name_Mutual Trust bank Limited', 'bank_name_NRB Bank Limited',
       'bank_name_NRB Commercial Bank Limited',
       'bank_name_National Credit and Commerce Bank Limited',
       'bank_name_One Bank', 'bank_name_Premier Bank', 'bank_name_Prime Bank',
       'bank_name_Pubali Bank Limited', 'bank_name_Rupali Bank Limited',
       'bank_name_Sonali Bank Limited', 'bank_name_Standard Charter',
       'bank_name_Trust Bank', 'bank_name_United Commercial Bank Limited',
       'card_type_Credit', 'card_type_Debit', 'card_type_Prepaid',
       'interest_rate_1-10', 'interest_rate_11-20', 'interest_rate_21-30',
       'interest_rate_zero', 'max_credit_limit_0-100000',
       'max_credit_limit_100000-500000', 'max_credit_limit_1000000+',
       'max_credit_limit_N/A', 'max_credit_limit_unknown']


def user_features(user_input):
    user_features = []
    for input in user_input:
        user_features.extend(user_input[input])
    return user_features

def make_query(user_features):
    mapping = [feature_maps[feature] for feature in user_features]
    query = []
    for ml_feature in feature_list:
        if ml_feature in mapping:
            query.append(1)
        elif ml_feature in ['max_credit_limit_N/A','max_credit_limit_unknown']:
            query.append(1)
        else:
            query.append(0)
    return query

query = make_query(user_features(user_input))
full_dir = "knn.pickle"
model = joblib.load(os.path.realpath(full_dir))
query = np.array(query)
print(query)
result = model.kneighbors(query.reshape(1,-1))
print(result)

indices = result[1]
scores = result[0]
indices = indices.tolist()
print(indices)
card_names = get_card_names(indices).tolist()
print(",".join(card_names))
