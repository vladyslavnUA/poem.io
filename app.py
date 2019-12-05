import random
from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
    f = open("poem.txt", 'r')
    poem = f.readlines()

@app.route('/')
def index():
  render_template('index.html')

@app.route('/submit-poem') 
def submit():
  render_template('submit-poem.html')

@app.route('/poem')
def display():
  option = request.args.get('choice')
  
  if option == 'backwards':
    index_poem()
    render_template('display.html')

def index_poem():
  print()
  for i in range(len(poem), 0, -1):
      index = str(i)
      line = poem[i-1]
      print(index + ":" + line)
      print()
      
def shuffle_poem():
  print("####################################")
  print()
  lines = [ line for line in poem ]
  random.shuffle(lines)
  for line in lines:
      print(line)
      print()

def custom_shuffle():
  print("####################################")
  print()
  line = [ line for line in poem ]
  for line in line:
    words = [ word for word in line ]
    random.shuffle(words)
    for word in words:
      print (word, end=" ")
    
    print()

index_poem()
shuffle_poem()
custom_shuffle()

app.run(debug=True)