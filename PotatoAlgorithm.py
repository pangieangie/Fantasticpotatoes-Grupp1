
def search_database(actor=None, platform=None, genre=None, language=None):           # Creates a search feature with 4 boxes, if they are left blank it remains none (empty)
    matching_ids = set(shows_table.keys())                                           # Takes show IDs from "shows" table and makes them into a set


    if genre is not None:                                                            # Checks if "genre" box is filled in, if its empty this whole thing is skipped
        target_genre_id = None                                                       # Makes empty variable like a holding space for ID until its found by the system
        for genre_id, genre_name in genres_ref.items():                              # A loop that goes through genres_ref (our pretend dictionary that connects to the genre_ref database page) .items takes both the ID and the name for all genres
            if genre_name == genre:                                                  # Checks if the name taken from genre_ref matches the genre input in the search box
                target_genre_id = genre_id                                           # if the text itself matches then the ID from genres_ref is put in the empty variable from row 7
                break                                                                # stops the for loop. We found the match so don't need to keep searching

        genre_show_id = set()                                                       # makes a new empty set to hold the Show IDs that link to the target genre
        if target_genre_id is not None:                                             # A check to make sure the code actually has an ID from the block above and doesn't break
            for row in genre_mapping:                                               # Starts a for loop that checks the genre_mapping page for ID's matching to shows
                if row[1] == target_genre_id:                                       # Loop goes through each row and finds in what cases the Genre_ID matches the ID we want so like "1" for drama etc. 
                    genre_show_id.add(row[0])                                       # If the line above finds a matching genre id, then it looks at the show_id that matches that specific genre and adds it to the set

            matching_ids = matching_ids.intersection(genre_show_id)                     # Compares the matching_ids set (which is all the shows) and the genre_show_id set (which is the shows with the selected genre)
                                                                                    # Intersection then compares the two and only takes out the items from matching_ids that are also in genre_show_id
    if actor is not None:
        target_actor_id = None
        for actor_id, actor_name in actors_ref.items():
            if actor_name == actor:
                target_actor_id = actor_id
                break

        actor_show_id = set()
        if target_actor_id is not None:
            for row in actor_mapping:
                if row[1] == target_actor_id:
                    actor_show_id.add(row[0])

            matching_ids = matching_ids.intersection(actor_show_id)

    if platform is not None:
        target_platform_id = None
        for platform_id, platform_name in platforms_ref.items():
            if platform_name == platform:
                target_platform_id = platform_id
                break

        platform_show_id = set()
        if target_platform_id is not None:
            for row in platform_mapping:
                if row[1] == target_platform_id:
                    platform_show_id.add(row[0])

            matching_ids = matching_ids.intersection(platform_show_id)

    if language is not None:
        target_language_id = None
        for language_id, language_name in languages_ref.items():
            if language_name == language:
                target_language_id = language_id
                break

        language_show_id = set()
        if target_language_id is not None:
            for row in language_mapping:
                if row[1] == target_language_id:
                    language_show_id.add(row[0])

            matching_ids = matching_ids.intersection(language_show_id)

    platform_scores = {}                                                            # Makes emtpy dictionary that will work as scoreboard for platforms (holds ids and the points) 

    for row in platform_mapping:                                                    # Starts a loop looking at the platform_mapping database page again                                                  
        show_id = row[0]                                                            # Takes the show ID from the row
        platform_id = row[1]                                                        # Takes the platform ID from the row
        if show_id in matching_ids:                                                 # Checks so the show has passed through all the earlier filters and still applies
            if platform_id not in platform_scores:                                  # If that platform hasn't been counted on the scoreboard yet it adds it at 0
                platform_scores[platform_id] = 0

            platform_scores[platform_id] += 1                                       # Gives the platform 1 point because it has a show that meets all the filter criterias

            recommended_platform = None                                             # Makes an emtpy holding space where the winning platform name goes
            if platform_scores:                                                     # Checks so the scoreboard has something in it and isn't just empty
                winning_id = max(platform_scores, key=platform_scores.get)          # Max is a python shortcut that checks the scoreboard and grabs the platform ID with the highest score
                recommended_platform = platforms_ref[winning_id]                    # Uses the platforms_ref database page to turn the winning ID into the corresponding name of the platform, so if 1 wins it changes it to "netflix"

    matching_show_names = []                                                        # Makes an empty list that holds the text names of the winning shows
    for show_id in matching_ids:                                                    # Loops through the winning shows respective IDs
        show_title = shows_table[show_id]                                           # Looks up the show's ID in the Shows_table to get the actual title
        matching_show_names.append(show_title)                                      # Adds the text name of the show to the final list

        return matching_show_names, recommended_platform                            # Returns the winning show names AND the recommended (winning) platform


