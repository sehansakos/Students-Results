##references
##
##colors:
##https://matplotlib.org/stable/gallery/color/named_colors.html
##
##global keyword:
##https://www.w3schools.com/python/python_variables_global.asp
##
##max count
##https://stackoverflow.com/questions/3090175/find-the-greatest-largest-maximum-number-in-a-list-of-numbers
##
## I declare that my work contains no examples of misconduct, such as plagiarism, or 
##collusion. 
## Any code taken from other sources is referenced within my code soluƟon.
## Student ID: …20230332…………………..…
## Date: ……01/12/2023………………..…

from graphics import *  

# Student count 
progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0
total_count = 0

students_data = []

# Print result and update counts
def show_result(pass_credit, defer_credits, fail_credits):
    global total_count
    global progress_count
    global trailer_count
    global retriever_count
    global excluded_count
    
    total_count += 1
    if pass_credits == 120:
        outcome = 'Progress'
        progress_count += 1
    elif pass_credits >= 100:
        outcome ='Progress(module trailer)'
        trailer_count += 1
    elif fail_credits >= 80:
        outcome ='Exclude'
        excluded_count += 1
    else:
        outcome ='Module retriever'
        retriever_count += 1

    print(outcome)

    # Store data in the list
    students_data.append((outcome, pass_credits, defer_credits, fail_credits))

    
# Function to validate total count 
def total_sum():
    return progress_count + trailer_count + retriever_count + excluded_count


# Function to validate if the input is an integer and credits range 
def get_credits(question):
    while True: 
        try:
            credits = int(input(question))
            if credits not in range(0, 121, 20): 
                print("Out of range")
            else:
                return credits;
        except ValueError: 
            print("Integer required")

# Function to get user profile (student or staff)
def user_profile():
    while True:
        user_profile = input("Are you a student or staff? Enter '1' for student or '2' for staff: ")
        if user_profile.lower() == '1' or user_profile.lower() == '2':
            return user_profile.lower()
        else:
            print("Invalid input. Please enter '1' for student or '2' for staff.")



# Histogram data
chart_height = 600;
bar_width = 80
bar_gap = 20
initial_gap = 40
footer_gap = 100

# Calculate chart height 
def chart_hight_sum():
    highest_count = max(progress_count, trailer_count, retriever_count, excluded_count)
    return highest_count*20 + 300

    
def display_histogram():
    height = chart_hight_sum()
    win = GraphWin("Histogram", 600, 500)
    win.setBackground("Mint Cream")

    histogram_header(win)
    
    histogram_bar(win, 0, "Progress", progress_count, "palegreen")
    histogram_bar(win, 1, "Trailer", trailer_count, "limegreen")
    histogram_bar(win, 2, "Retriever", retriever_count, "yellowgreen")
    histogram_bar(win, 3, "Excluded", excluded_count, "pink")

    histogram_footer(win)

# draw a histogram bar
def histogram_bar(win, bar_index, bar_name, count, color,):
    # calculate bar x cordinates dep
    bar_x = initial_gap + bar_index * (bar_width + bar_gap)
    bar_height = 40*count
    
    #create bar rectangle
    rectangle = Rectangle(Point(bar_x, win.getHeight() - footer_gap), Point(bar_x + bar_width, win.getHeight() - footer_gap - bar_height))
    rectangle.setFill(color)
    rectangle.draw(win)

    #bar count text
    count_text = Text(Point(bar_x + bar_width/2, win.getHeight() - footer_gap - bar_height - 20), str(count))
    count_text.draw(win)

    #bar_name_text
    bar_name = Text(Point(bar_x + bar_width/2, win.getHeight()- footer_gap + 20), bar_name)
    bar_name.draw(win)

# histogram header information
def histogram_header(win):
    heading = Text(Point(200, 30), 'Histogram Results')
    heading.draw(win)
    heading.setTextColor("grey")
    heading.setSize(24)
    heading.setStyle("bold")
    heading.setFace("helvetica")

# histogram footer information
def histogram_footer(win):
    footer = Text(Point(150, win.getHeight() - footer_gap + 50), str(total_count) + " outcomes total")
    footer.draw(win)                                    
    footer.setTextColor("grey")
    footer.setSize(20)
    footer.setFace("helvetica")

    base_line = Rectangle(Point(20, win.getHeight() - footer_gap), Point((bar_width + bar_gap)*5 + 50, win.getHeight() - footer_gap))
    base_line.draw(win)


# Get user profile
user_profile = user_profile()


# Get credit info until user quits with q
while True:
    if user_profile == '1':
        pass_credits = get_credits("\nPlease enter your credits at pass:")
        defer_credits = get_credits("Please enter your credits at defer:")
        fail_credits = get_credits("Please enter your credits at fail:")

        total_credits = pass_credits + defer_credits + fail_credits

        if total_credits != 120:
            print('Total incorrect')
        else:
            show_result(pass_credits, defer_credits, fail_credits)
            
             

    elif user_profile == '2':
        while True:
            pass_credits = get_credits("\nEnter your total PASS credits:")
            defer_credits = get_credits("Enter your total DEFER credits:")
            fail_credits = get_credits("Enter your total FAIL credits:")

            total_credits = pass_credits + defer_credits + fail_credits

            if total_credits != 120:
                print('Total incorrect')
            else:
                show_result(pass_credits, defer_credits, fail_credits)
            
                

            another_set = input("\nWould you like to enter another set of data?" 
                        "\nEnter 'y' for yes or 'q' to quit and view results: ")
            if another_set.lower() == 'q':
                break

        total_count = total_sum()
        display_histogram()

        

        # Display data from the list
        print("\nPart 2:")
        for data in students_data:
            print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")


        # Read data from the list    
        file = open('Progression_data.txt', 'r')
        print("\nPart 3:")
        for data in students_data:
            print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")
            
        file.close()


        # Save data to a text file
        with open("Progression_data.txt", "w") as file:
            file.write("Part 3:\n")
            for data in students_data:
                file.write(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}\n")
    break





