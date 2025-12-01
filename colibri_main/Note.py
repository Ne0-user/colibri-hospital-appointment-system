class Note:
    def __init__(self, reason, lab_results, treatments, follow_up):
        self.reason = reason
        self.lab_results = lab_results
        self.treatments = treatments
        self.follow_up = follow_up

    def __str__(self):
        return (
            f"Reason: {self.reason}\n"
            f"Lab results: {self.lab_results}\n"
            f"Treatments: {self.treatments}\n"
            f"Follow up: {self.follow_up}\n"
            "----\n"
        )
