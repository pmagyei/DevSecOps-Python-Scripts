class AnonymousSurvey:
    """collect anonymous questions"""
    def __init__(self, question):
        """stores a question and prepare a response"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question"""
        print(self.question)

    def store_response(self, new_response):
        """store a single response"""
        self.responses.append(new_response)
    def show_results(self):
        """Show all responses given"""
        print("Survey results")
        for response in self.responses:
            print(f"- {response}")