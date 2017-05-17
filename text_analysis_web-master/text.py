import calc, eq

class Text:

    def __init__(self, title, text):

        self.title = title
        self.text_string = text
        self.sentences = 0
        self.words = 0
        self.syllables = 0
        self.characters = 0
        self.poly_syllables = 0
        self.re = 0
        self.gl = 0
        self.ari = 0
        self.smog = 0

    def __str__(self):
        output_string = make_string(self.title, self.re, self.gl, self.ari, self.smog)
        return output_string

    def process(self):

        self.sentences, self.words, self.syllables, \
        self.characters, self.poly_syllables = calc.analyze_string(self.text_string)

        self.re = eq.fk_re(self.words, self.sentences, self.syllables)
        self.gl = eq.fk_gl(self.words, self.sentences, self.syllables)
        self.ari = eq.ari(self.words, self.sentences, self.characters)
        self.smog = eq.smog(self.poly_syllables)

    def get(self):

        return self.title, self.sentences, self.words, self.syllables, \
               self.characters, self.polysyllables, self.re, self.gl, \
               self.ari, self.smog

def make_string(title, re, gl, ari, smog):
    '''Create formatted string'''
    temp = 'Title: {} RE: {:>10} GL: {:>10} ARI: {:>10} SMOG: {:>10}'.format(title, re, gl, ari, smog)
    return temp
