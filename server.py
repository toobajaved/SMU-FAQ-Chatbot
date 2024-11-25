from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import json

class Chatbot:
    def __init__(self):
        # Define a dictionary of subjects and their descriptions (expanded with dataset)
        self.subjects = {
            "application deadline": "The application deadline for most programs is February 1 for the fall term.",
            "how to apply": "You can apply online through our application portal. Make sure to prepare the required documents.",
            "available scholarships": "We offer a range of scholarships for both domestic and international students. Visit our scholarships page for details.",
            "tuition fees": "Tuition fees vary by program. Please refer to our tuition and fees page for accurate details.",
            "contact admissions": "You can contact the admissions office via email at admissions@university.edu or call (123) 456-7890.",
            "campus housing": "Campus housing applications open in March for the fall term. Visit the housing portal to apply.",
            "academic calendar": "The academic calendar provides important dates, including term start/end dates and holidays. Visit our website for more details.",
            "transfer credits": "Transfer credit evaluations are done upon admission. Submit your transcripts for assessment.",
            "international students": "International students can find information on visas, work permits, and support services on our international office webpage.",
            "library hours": "The library is open from 8 AM to 10 PM on weekdays and 10 AM to 6 PM on weekends.",
            "student clubs": "We have over 50 student clubs and organizations. Check the student life section on our website for the list.",
            "career services": "Career Services offers resume reviews, job postings, and career counseling. Visit our office or book online.",
            "study abroad": "Our study abroad programs allow you to study in over 20 countries. Applications are due by March 15.",
            "course registration": "Course registration for the upcoming term opens on April 1. Log in to the portal to register.",
            "withdrawal policy": "Courses can be dropped without penalty within the first two weeks of the term. After that, consult the registrar's office.",
            "financial aid": "Financial aid is available through grants, loans, and scholarships. Visit our financial aid office for assistance.",
            "academic advising": "Academic advisors are available by appointment to help with course planning and degree requirements.",
            "student ID": "Student IDs can be obtained at the campus services desk during the first week of term.",
            "bookstore": "The campus bookstore carries textbooks, supplies, and university merchandise. It is located in the main building.",
            "sports facilities": "Sports facilities include a gym, swimming pool, and sports courts, available to all students with a valid ID.",
            "mental health support": "Counseling and mental health services are available for students. Book appointments through our health center."
        }

        # Define rules with grouped patterns and associated responses
        self.rules = {
            ("hello", "hi", "hey"): "🤖 Hello! This is SMULIBRARYBOT. What subject do you want to learn about today?\nList of subjects: " + ", ".join(self.subjects.keys()),
            ("how are you", "how are you doing"): "🤖 I'm a chatbot, so I don't have feelings, but thanks for asking!",
            ("subjects", "topics"): "🤖 Here are the subjects I can help you with: " + ", ".join(self.subjects.keys()) + ". Please type the subject name to learn more.",
            ("exit", "bye", "goodbye", "quit"): "🤖 Thank you! Have a nice day!",
        }

    def get_response(self, user_input):
        user_input = user_input.lower()

        # Check each rule's patterns to see if any match the user input
        for patterns, response in self.rules.items():
            if any(pattern in user_input for pattern in patterns):
                return response
        
        # Check if user input matches any subject directly
        if user_input in self.subjects:
            # First send the subject explanation, followed by asking for another subject
            subject_info = self.subjects[user_input]
            return f"🤖 {subject_info}\n\nWhat other subject do you want to learn about? (type 'exit' or 'quit' if you're done)"

        # Default response if no patterns or subjects match
        return "🤖 Sorry, I do not understand, can you try again?"

# Initialize the chatbot
chatbot = Chatbot()

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/ask'):
            query = urllib.parse.urlparse(self.path).query
            message = urllib.parse.parse_qs(query).get('message', [''])[0]
            response = chatbot.get_response(message)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'reply': response}).encode())
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('SMULibrarybot.html', 'r') as file:
                self.wfile.write(file.read().encode())
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
