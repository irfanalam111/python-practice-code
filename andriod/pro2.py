import pyttsx3

class view(pyttsx3.Engine):
    def __init__(self):
        super.__init__(self)
        voices=self.getProperty('voice')
        engine=self.setProperty('voice',voices[1].id)
        rate=self.getProperty('rate')
        self.setProperty('rate',160)



v=view()
