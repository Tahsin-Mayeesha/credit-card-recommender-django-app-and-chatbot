from sklearn.externals import joblib
import numpy as np
import os
from .models import Card,Recommendation,Profile
from .location import location_scoring_cards

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


full_dir = "recommender/model/knn.pickle"
model = joblib.load(os.path.realpath(full_dir))


def generate_recommendations(user,feature_list,user_input,user_profile,model=model):
    query = [1 if entry in user_input else 0 for entry in feature_list]
    query = np.array(query)
    result = model.kneighbors(query.reshape(1,-1))
    recommendation_indices = result[1].tolist()[0]
    recommendation_scores = result[0].tolist()[0]
    
    current_profile = Profile.objects.filter(user=user)
    if(len(current_profile)>0):
        for obj in current_profile:
            obj.delete()
    
    make_profile = Profile.objects.create(user=user,
                                          occupation=user_profile['occupation'],
                                          area=user_profile['area'],
                                          city=user_profile['city']
                                          )
    
    save_recommendations(user,recommendation_indices,recommendation_scores)
    return (recommendation_indices,recommendation_scores)

def save_recommendations(user,rec_indices,rec_scores):
    current_recs = Recommendation.objects.filter(user=user)
    if len(current_recs)>0:
        for obj in current_recs:
            obj.delete()
    for index in [0,1,2,3,4]:
            card = Card.objects.get(pk=rec_indices[index])
            score = rec_scores[index]
            rec_object = Recommendation.objects.create(user=user,card=card,recommendation_score=score)

def get_recommendations(user):
    current_recs = Recommendation.objects.filter(user=user)
    current_profile = Profile.objects.filter(user=user)[0]
    user_location = {'city':current_profile.city,'area':current_profile.area}
    card_preference_banks = []
    for obj in current_recs:
        card = obj.card
        card_preference_banks.append(card.bank_name)
    bank_distances = location_scoring_cards(user_location,card_preference_banks)
    print(bank_distances)
    results = []
    for obj in current_recs:
            card = obj.card
            result_dict = {}
            result_dict['card_name'] = card.card_name
            result_dict['bank_name'] = card.bank_name
            result_dict['url'] = card.url
            result_dict['score'] = round(obj.recommendation_score,3)
            
            bank_distance= bank_distances[card.bank_name.replace("Limited",'').lower().strip()]
            if bank_distance!=np.inf:
                result_dict['nearby'] = True
                result_dict['distance'] = bank_distance
            else:
                result_dict['nearby'] = False
            results.append(result_dict)

    return results
    


