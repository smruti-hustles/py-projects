#translator
from googletrans  import Translator

translator=Translator()
inp=input()
out=translator.translate(inp,dest="hi")  # "hi" stands for hindi
print(out.text)