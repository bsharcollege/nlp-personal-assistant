import spacy

class FAQManager:
    def __init__(self):
        self.faqs = {}
        self.nlp = spacy.load("en_core_web_md")

    def add_faq(self, question, answer):
        self.faqs[question] = answer

    def remove_faq(self, question):
        if question in self.faqs:
            del self.faqs[question]

    def get_answer(self, question):
        question_doc = self.nlp(question)
        best_match = None
        best_similarity = 0.0

        for faq_question in self.faqs:
            faq_doc = self.nlp(faq_question)
            similarity = question_doc.similarity(faq_doc)
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = faq_question

        if best_match:
            return self.faqs[best_match]
        else:
            return "Sorry, I don't have an answer for that."