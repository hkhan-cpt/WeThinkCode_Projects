

def create_outline():
    """
    TODO: implement your code here
    """

    #Step 1: Creats a set and print it underneath a heading
    course_topics= set([ #Creating a set
    "Introduction to Python", 
    "Tools of the Trade", 
    "How to make decisions", 
    "How to repeat code", 
    "How to structure data", 
    "Functions", 
    "Modules"
    ])

    course_topics= list(course_topics) #Step 4 -Converts set into a list 
    list.sort(course_topics) #Step 4 -Sorts the list alphabetically
    print("Course Topics:\n* " + "\n* ".join(course_topics)) #Printing to match the required format
    

    #Step 2: Define a map and print it out under a heading
    problems_list= ["Problem 1", "Problem 2", "Problem 3"] #Creating a list
    problems_dictionary= { #Creating a dictionary to enable mapping
    "Introduction to Python": problems_list,
    "Tools of the Trade": problems_list,
    "How to make decisions": problems_list,
    "How to repeat code": problems_list,
    "How to structure data": problems_list,
    "Functions": problems_list,
    "Modules": problems_list,
    }

    #Printing to match the required format
    print("Problems:") 
    for item in problems_dictionary: #Using for loop to run through the dictionary to ensure it is correctly printed
        print("*", item, ":", ", ".join(problems_list)) 


    #Step 3: Create a few tuples and print them out as a list
    def function(criteria): #Step 4 -Defining function to enable use of key to sort accordingly  
        return criteria[4] #Step 4 -Selecting sort criteria
    
    #Creating tuple examples
    student_tuple_1= ("3", "Tony", "Tools of the Trade", "Problem 2", "[COMPLETED]") 
    student_tuple_2= ("1", "Steve", "How to make decisions", "Problem 3", "[STARTED]")
    student_tuple_3= ("2", "Natasha", "Introduction to Python" , "Problem 1", "[GRADED]")

    tuple_list= [student_tuple_1, student_tuple_2, student_tuple_3] #Creating a list of example tuples
    tuple_list.sort(key=function, reverse=True) #Step 4- Sorting alphabetically in reverse

    #Printing to match the required format
    print("Student Progress:") 
    for a in range(0, len(tuple_list)): #Using for loop to run through the list to ensure it is correctly printed
        print(f"{tuple_list[a][0]}. {tuple_list[a][1]} - {tuple_list[a][2]} - {tuple_list[a][3]} {tuple_list[a][4]}")
    print("\n")


    #Step 4: Sorting data by specified criteria


if __name__ == "__main__":
    create_outline()
