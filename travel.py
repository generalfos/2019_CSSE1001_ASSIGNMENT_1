""" Travel Inspiration

    This program prompts users for input about their preferences in a
    travel destination. Using these responses the program will recommend
    the best match in a database of potential travel destinations.

"""

__author__ = "Joel Foster, 45820384"
__date__ = "28/03/2019"



from destinations import Destinations

def invalid_choice(user_input):
    """ Indicates to user that their input is invalid

        Parameters:
            user_input(str): the user's input 

    """
    print("\nI'm sorry, but", user_input,\
              "is not a valid choice. Please try again.")

def interest_is_valid(user_input, catergory):
    """ Determines if user input to interest questions is valid.

    User input is valid iff it is an integer which lies within the range [-5, 5]
    (inclusive).
    
    Parameters:
        user_input (str): user response to question.
        catergory (str): used to define which interest input is being checked.

    Returns:
        user_input (str): returns a correct user input. 

    """
    try:
        int(user_input)
    except ValueError:
        invalid_choice(user_input)
        print("\nHow much do you like ", catergory, "? (-5 to 5)", sep="")
        user_input = input("> ")
        return user_input
    while int(user_input) not in range(-5,6):
            invalid_choice(user_input)
            print("\nHow much do you like ", catergory,"? (-5 to 5)", sep="")
            user_input = input("> ")
            return user_input
    return user_input
    
def main():
    """
    Prompts user for input and depending upon the input recommends a 
    destination to the user or returns None if no destination
    meets user specifications.

    """

    # Define lists of possible inputs to be called later.
    continent_list = "  1) Asia\n  2) Africa\n  3) North America\n  \
4) South America\n  5) Europe\n  6) Oceania\n  7) Antarctica"
    money_list = "  $$$) No object\n \
 $$) Spendable, so long as I get value from doing so\n \
 $) Extremely important; I want to spend as little as possible"
    crime_list = "  1) Low\n  2) Average\n  3) High"
    child_list = "  1) Yes\n  2) No"
    season_list = "  1) Spring\n  2) Summer\n  3) Autumn\n  4) Winter"
    climate_list = "  1) Cold\n  2) Cool\n  3) Moderate\n  4) Warm\n  5) Hot"
    
    print("Welcome to Travel Inspiration!\n")
    name = input("What is your name? ")
    print("\nHi, ", name, "!", sep="")

    print("\nWhich continents would you like to travel to?")
    print(continent_list)
    continent_input = input("> ")
    
    # Validates user input and if invalid prompts user for another input.
    for i in continent_input:
        if i not in ["1", "2", "3", "4", "5", "6", "7", ",", " "]:
            invalid_choice(continent_input)
            print("\nWhich continents would you like to travel to?")
            print(continent_list)
            continent_input = input("> ")
        
    print("\nWhat is money to you?")
    print(money_list)
    money_input = input("> ")

    while money_input not in ["$$$", "$$", "$"]:
        invalid_choice(money_input)
        print("\nWhat is money to you?")
        print(money_list)
        money_input = input("> ")
    
    print("\nHow much crime is acceptable when you travel?")
    print(crime_list)
    crime_input = input("> ")

    while crime_input not in ["1", "2", "3"]:
        invalid_choice(crime_input)
        print("\nHow much crime is acceptable when you travel?")
        print(crime_list)
        crime_input = input("> ")

    print("\nWill you be travelling with children?")
    print(child_list)
    child_input = input("> ")

    while child_input not in ["1", "2"]:
        invalid_choice(child_input)
        print("\nWill you be travelling with children?")
        print(child_list)
        child_input = input("> ")
    
    print("\nWhich seasons do you plan to travel in?")
    print(season_list)
    season_input = input("> ")

    for i in season_input:
        if i not in ["1", "2", "3", "4", ",", " "]:
            invalid_choice(season_input)
            print("\nWhich seasons do you plan to travel in?")
            print(season_list)
            season_input = input("> ")
        
    print("\nWhat climate do you prefer?")
    print(climate_list)
    climate_input = input("> ")

    while climate_input not in ["1", "2", "3", "4"]:
        invalid_choice(climate_input)
        climate_question()
        climate_input = input("> ")
        
    print("\nNow we would like to ask you some questions about your interests,\
 on a scale of -5 to 5. -5 indicates strong dislike, whereas 5 indicates strong\
 interest, and 0 indicates indifference.")

    print("\nHow much do you like sports? (-5 to 5)")
    sports_input = input("> ")
    sports_input = interest_is_valid(sports_input, "sports")
    
    print("\nHow much do you like wildlife? (-5 to 5)")
    wildlife_input = input("> ")
    wildlife_input = interest_is_valid(wildlife_input, "wildlife")
    
    print("\nHow much do you like nature? (-5 to 5)")
    nature_input = input("> ")
    nature_input = interest_is_valid(nature_input, "nature")
  
    print("\nHow much do you like historical sites? (-5 to 5)")
    landmarks_input = input("> ")
    landmarks_input = interest_is_valid(landmarks_input, "historical sites")
    
    print("\nHow much do you like fine dining? (-5 to 5)")
    dining_input = input("> ")
    dining_input = interest_is_valid(dining_input, "fine dining")
    
    print("\nHow much do you like adventure activities? (-5 to 5)")
    adventure_input = input("> ")
    adventure_input = interest_is_valid(adventure_input, "adventure activities")
    
    print("\nHow much do you like the beach? (-5 to 5)")
    beach_input = input("> ")
    beach_input = interest_is_valid(beach_input, "beach")
    
    print("\nThank you for answering all our questions. \
Your next travel destination is:")
    
    desired_continents = []
    desired_seasons = []

    # Convert user input into a 'usable' format
    # (i.e. values within the database). 

    for num in continent_input:
        if num == '1':
            desired_continents.append('asia')
        elif num == '2':
            desired_continents.append('africa')
        elif num == '3':
            desired_continents.append('north america')
        elif num == '4':
            desired_continents.append('south america')
        elif num == '5':
            desired_continents.append('europe')
        elif num == '6':
            desired_continents.append('oceania')
        elif num == '7':
            desired_continents.append('antarctica')

    if child_input == '1':
        child_friendly = True
    elif child_input == '2':
        child_friendly = False

    if crime_input == '1':
        crime_index = 'low'
    elif crime_input == '2':
        crime_index = 'average'
    elif crime_input == '3':
        crime_index = 'high'

    if climate_input == '1':
        desired_climate = 'cold'
    elif climate_input == '2':
        desired_climate = 'cool'
    elif climate_input == '3':
        desired_climate = 'moderate'
    elif climate_input == '4':
        desired_climate = 'warm'
    elif climate_input == '5':
        desired_climate = 'hot'

    for num in season_input:
        if num == '1':
            desired_seasons.append('spring')
        elif num == '2':
            desired_seasons.append('summer')
        elif num == '3':
            desired_seasons.append('autumn')
        elif num == '4':
            desired_seasons.append('winter')

    # Establish local variables\objects. 
    all_destinations = []
    recommendation = "None"
    possible_recommendations = []
    score_list = []

    all_spring_factors = []
    all_summer_factors = []
    all_autumn_factors = []
    all_winter_factors = []
            
    for destination in Destinations().get_all():
        # Create base lists for each relevant catergory.
        all_destinations.append(destination.get_name())
        all_spring_factors.append(destination.get_season_factor('spring'))
        all_summer_factors.append(destination.get_season_factor('summer'))
        all_autumn_factors.append(destination.get_season_factor('autumn'))
        all_winter_factors.append(destination.get_season_factor('winter'))

        # Determine which destinations in the database meet user requirements.
        if child_friendly == True:
            
            if crime_index == "high":
                if destination.get_continent() in desired_continents and \
                destination.get_cost() <= money_input and \
                destination.is_kid_friendly() == child_friendly and \
                desired_climate == destination.get_climate():
                    possible_recommendations.append(destination.get_name())

            elif crime_index == "average":
                if destination.get_continent() in desired_continents and \
                destination.get_cost() <= money_input and \
                destination.get_crime() != "high" and \
                destination.is_kid_friendly() == child_friendly and \
                desired_climate == destination.get_climate():
                    possible_recommendations.append(destination.get_name())

            elif crime_index == "low":
                if destination.get_continent() in desired_continents and \
                destination.get_cost() <= money_input and \
                destination.get_crime() == "low" and \
                destination.is_kid_friendly() == child_friendly and \
                desired_climate == destination.get_climate():
                    possible_recommendations.append(destination.get_name())
             
        elif child_friendly == False:
            
            if crime_index == "high":
                if destination.get_continent() in desired_continents and \
                destination.get_cost() <= money_input and \
                desired_climate == destination.get_climate():
                    possible_recommendations.append(destination.get_name())

            elif crime_index == "average":
                if destination.get_continent() in desired_continents and \
                destination.get_cost() <= money_input and \
                destination.get_crime() != "high" and \
                desired_climate == destination.get_climate():
                    possible_recommendations.append(destination.get_name())

            elif crime_index == "low":
                if destination.get_continent() in desired_continents and \
                destination.get_cost() <= money_input and \
                destination.get_crime() == "low" and \
                desired_climate == destination.get_climate():
                    possible_recommendations.append(destination.get_name())

    # Determine if there are any possible recommendations.
    if len(possible_recommendations) > 0:
        recommended_destination_indices = []
    
        # Determine the location (index) of each possible destination
        # within the list of all destinations.
        for destination in possible_recommendations:
            recommended_destination_indices.append(all_destinations.index(destination))

        relevant_season_factors = []

        # Obtain relevant season factors.
        for index in recommended_destination_indices:
            for season in desired_seasons:
                if season == "winter":
                    relevant_season_factors.append(all_winter_factors[index])
                elif season == "summer":
                    relevant_season_factors.append(all_summer_factors[index])
                elif season == "spring":
                    relevant_season_factors.append(all_spring_factors[index])
                elif season == "autumn":
                    relevant_season_factors.append(all_autumn_factors[index])

        season_factor = max(relevant_season_factors)

        # Calculate interest_score for all destinations.
        for destination in Destinations().get_all():
            interest_score = int(sports_input) * \
                             destination.get_interest_score('sports') \
                             + int(wildlife_input) * \
                             destination.get_interest_score('wildlife') \
                             + int(nature_input) * \
                             destination.get_interest_score('nature') \
                             + int(landmarks_input) * \
                             destination.get_interest_score('historical') \
                             + int(dining_input) * \
                             destination.get_interest_score('cuisine') \
                             + int(adventure_input) * \
                             destination.get_interest_score('adventure') \
                             + int(beach_input) * \
                             destination.get_interest_score('beach')
            score = season_factor * interest_score
            score_list.append(score)

        # Obtain relevant scores
        relevant_scores = []
        for index in recommended_destination_indices:
            relevant_scores.append(score_list[index])

        # Find the possible destination with the greatest score. 
        for score in relevant_scores:
            if score ==  max(relevant_scores):
                final_index = relevant_scores.index(score)

        recommendation = possible_recommendations[final_index]
        print(recommendation)

    else:
        print(recommendation)
    


if __name__ == "__main__":
    main()



