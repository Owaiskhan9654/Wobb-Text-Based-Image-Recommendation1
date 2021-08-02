from flask import Flask, render_template, request
from ranking import rank
import nltk
#nltk.download('punkt')


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search/results', methods=['GET', 'POST'])
def search_request():
    search_term = request.form["input"]
    list1,query= rank(search_term)
    list2 = []
    for i in list1:
        list2.append(i + ".jpeg")
    print(list2)

    return render_template('results.html', list2=list2,query=query)

if __name__ == '__main__':
    app.run(debug=True)

