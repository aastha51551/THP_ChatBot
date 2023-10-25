# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

faculty_mapping = {
    "Aerospace": ["FacultyX", "FacultyY", "FacultyZ", "FacultyW", "FacultyQ", "FacultyR", "FacultyS", "FacultyT", "FacultyU", "FacultyV"],
    "Biosciences": ["FacultyA", "FacultyB", "FacultyC", "FacultyD", "FacultyE", "FacultyF", "FacultyG", "FacultyH", "FacultyI", "FacultyJ"],
    "Computer Sciences": ["FacultyK", "FacultyL", "FacultyM", "FacultyN", "FacultyO", "FacultyP", "FacultyQ", "FacultyR", "FacultyS", "FacultyT"],
    "Civil": ["FacultyU", "FacultyV", "FacultyW", "FacultyX", "FacultyY", "FacultyZ", "FacultyA", "FacultyB", "FacultyC", "FacultyD"],
    "Chemical": ["FacultyE", "FacultyF", "FacultyG", "FacultyH", "FacultyI", "FacultyJ", "FacultyK", "FacultyL", "FacultyM", "FacultyN"]
}


class ActionListCourses(Action):
    def name(self) -> Text:
        return "action_list_courses"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dept_name = tracker.get_slot("dept_name")

        department_courses ={
            "Aerospace":["AE102","AE103","AE152","AE153","AE207","AE209","AE214","AE215","AE216","AE219"],
            "Biosciences":["BB101","BB400","BB401","BB402","BB403","BB404","BB405","BB406","BB407","BB408"],
            "Computer Sciences":["CS101","CS103","CS104","CS105","CS152","CS154","CS207","CS208","CS210","CS213"],
            "Civil":["CE102","CE103","CE201","CE203","CE204","CE205","CE206","CE207","CE209","CE211"],
            "Chemical":["CL102","CL152","CL202","CL203","CL205","CL207","CL231","CL232","CL242","CL244"]
        }
        
        # Fetch courses based on the provided department
        if dept_name in department_courses:
            courses = department_courses[dept_name]
            course_list = ", ".join(courses)
            dispatcher.utter_message(f"The courses offered in the {dept_name} department are: {course_list}")
        else:
            dispatcher.utter_message(f"Sorry, I couldn't find any courses for the {dept_name} department.")

        return []

    class ActionFacultyInfo(Action):

        def name(self) -> Text:
            return "action_faculty_info"

        def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            course_name = tracker.get_slot("course_name")

            # Retrieve faculty data for the course
            dept_name = tracker.get_slot("dept_name")
            faculty_list = faculty_data.get(dept_name)

            if course in faculty_list:
                faculty = faculty_list[courses.index(course_name)]
                dispatcher.utter_message(f"The faculty for course {course_name} in the {dept_name} department is {faculty_name}.")
            else:
                dispatcher.utter_message(f"Sorry, I couldn't find faculty information for course {course_name} in the {dept_name} department.")

            return []

