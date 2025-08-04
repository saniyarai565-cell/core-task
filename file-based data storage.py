import json

class FeedbackCollector:
    def _init_(self, filename="feedback.json"):
        self.filename = filename

    def submit_feedback(self, username, feedback):
        entry = {"username": username, "feedback": feedback}
        data = self._load_data()
        data.append(entry)
        self._save_data(data)
        print("Thank you! Your feedback has been saved.")

    def _load_data(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_data(self, data):
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def view_all_feedback(self):
        feedbacks = self._load_data()
        for fb in feedbacks:
            print(f"{fb['username']} said: {fb['feedback']}")
            collector = FeedbackCollector()
            collector.submit_feedback("ram", "Great app experience!")
            collector.view_all_feedback()