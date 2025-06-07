import pandas as pd

class Portfolio:
    def load_portfolio(self):
        # You can mock loading here — or skip if not needed
        self.links = [
            "https://github.com/vaibhavgaikwad7/Credibility-Detection-of-Health-Web-Blogs-Using-Explainable-AI",
            "https://github.com/vaibhavgaikwad7/Portfolio-Optimization-Using-Bidirectional-CNN-LSTM-with-Attention-Mechanism",
            "https://github.com/vaibhavgaikwad7/Energy-Consumption-Predictor"
            "https://github.com/vaibhavgaikwad7/Impact-of-weather-conditions-on-motor-vehicle-collisions-in-NYC"
            "https://github.com/vaibhavgaikwad7/AI-Job-Market-Trends-in-USA-using-Tableau"
        ]

    def query_links(self, skills):
        # Always return all 3 links (or you can return based on skills later)
        return self.links
