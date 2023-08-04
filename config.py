class Settings:
    """This class contains a few settings that can be changed prior to running the program to change the shape and
    values ranges of the data that is output."""
    number_of_data_points = 2000  # number of rows that will be generated and written to the CSV

    u_score_max = 100  # maximum user score that will be generated

    no_users = 3000  # maximum number of user reviews that will be generated

    c_score_max = 100  # maximum critic score that will be generated

    no_critics = 3000  # maximum number of critic reviews that will be generated

    year_min = 1974  # earliest year that will be generated

    year_max = 2023  # latest year that will be generated

    len_min = 60  # minimum movie length that will be generated

    len_max = 120  # maximum movie length that will be generated
