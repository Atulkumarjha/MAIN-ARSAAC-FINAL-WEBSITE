import spacy

nlp = spacy.load("en_core_web_sm")


class AACChatbot:
    def __init__(self):
        pass

    def process_input(self, user_input):
        doc = nlp(user_input)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        response = self.get_aac_response(user_input)
        return entities, response

    def get_aac_response(self, user_input):
        response = None

        if "communication" in user_input.lower():
            response = "AAC (Augmentative and Alternative Communication) includes methods and tools to support communication for individuals with speech or language impairments."

        elif "voice output" in user_input.lower():
            response = "Some AAC devices provide voice output, allowing users to express themselves using synthesized speech."

        elif "disability" in user_input.lower():
            response = "Please select the button from the above. Thank you. Do you need anything else?"

        elif "customer support" in user_input.lower():
            response = "Here is the customer support number: 9878456723. Feel free to ask for any assistance."
        
        elif "use this AAC device" in user_input.lower():
            response = "To use our AAC device, you can start by selecting the category of words or phrases you want to communicate. Swipe or press the corresponding buttons to construct sentences."

        elif "customize symbols" in user_input.lower():
            response = "Yes, you can customize symbols on our AAC device. You can upload personalized images or choose from our library of symbols to tailor the communication experience."

        elif "adjust voice output settings" in user_input.lower():
            response = "Voice output settings can be adjusted in the device settings menu. You can change voice preferences, pitch, and speed to suit your preferences."

        elif "languages supported" in user_input.lower():
            response = "Our AAC device currently supports multiple languages, including English, Spanish, French, and more. You can select your preferred language in the settings."

        elif "add new words or phrases" in user_input.lower():
            response = "Absolutely! You can add new words or phrases to the AAC device. Simply go to the customization menu and follow the steps to add personalized content."

        elif "update  software" in user_input.lower():
            response = "Software updates are essential for improved performance. You can update the AAC device by going to the settings menu and selecting the 'Software Update' option."

        elif "compatible with other assistive technologies" in user_input.lower():
            response = "Yes, our AAC device is designed to be compatible with various assistive technologies. It can work seamlessly with switch devices, head pointers, and other accessibility tools."

        elif "battery life" in user_input.lower():
            response = "The battery life of our AAC device depends on usage. On average, a fully charged battery can last up to 8 hours. You can check the battery status in the device settings."

        elif "technical support" in user_input.lower():
            response = "For technical support, you can contact our customer support team at 9878674635. They will assist you with any issues or questions you may have."

        elif "connect the AAC device to a computer or tablet" in user_input.lower():
            response = "Yes, our AAC device supports connectivity to computers and tablets. You can use USB or Bluetooth to establish a connection and transfer data between devices."

        return response

    def ask_question(self, question):
        user_input = input(f"Chatbot: {question}\nUser: ")
        entities, response = self.process_input(user_input)

        if entities:
            print("Entities:", entities)
        if response is not None:
            print("Chatbot:", response)
        if response is None:
            print("I'm sorry, I didn't understand that.")

    def main(self):
        print("Welcome to your AAC Chatbot!")

        # List of predefined questions
        questions = [
            "What is AAC?",
            "How does AAC work?",
            "Tell me about symbols in AAC.",
            "What is voice output in AAC?",
            "Is AAC suitable for all types of disabilities?",
            "How do I use this AAC device?",
            "Can I customize the symbols on the AAC device?",
            "How do I adjust the voice output settings?",
            "What languages are supported by the AAC device?",
            "Can I add new words or phrases to the AAC device?",
            "How do I update the software on the AAC device?",
            "Is the AAC device compatible with other assistive technologies?",
            "What is the battery life of the AAC device?",
            "How do I get technical support for the AAC device?",
            "Can I connect the AAC device to a computer or tablet?"
        ]

        # Ask each question and wait for user input
        for question in questions:
            self.ask_question(question)

        print("Goodbye! Take care.")


if __name__ == "__main__":
    aac_chatbot = AACChatbot()
    aac_chatbot.main()
