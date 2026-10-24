#the analyzer will return length of the text, number of words, and lines in the text;
def analyze_text(text):
      length = len(text)
      number_of_words = len(text.split())
      number_of_lines = len(text.splitlines())
      return {
          'length' : length,
          'Number Of Words' : number_of_words,
          'Number Of Lines' : number_of_lines
      }
