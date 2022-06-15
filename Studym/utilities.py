import random

class TopicAPI:
    def __init__(self, text=None, topic_obj=None):
        self.text = text
        self.topic_obj = topic_obj
    
    def title(self, random_title = 'Enter Title Here - '):
        if self.text[0] == '*':
            return self.text[1:self.text.find('\n')]
        else:
            random_title += str(random.randint(100000, 999999))
            return random_title

    def text(self):
        return self.text

    def quiz(self, topic_obj=None):
        if not topic_obj: topic_obj = self.topic_obj
        textl, heads = topic_obj.getTextList()
        randtl = random.choice(textl)
        ans = randtl[0]
        options = [ans] + random.choices([h for h in heads if h != ans], k=3)
        shuffled_options = random.sample(options, len(options))
        
        randomq = random.choice(randtl[1:])

        return randomq, shuffled_options, ans

