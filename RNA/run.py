#!/usr/bin/env python
# encoding: utf-8

"""

"""

##
from flask import Flask, render_template, request, redirect    # Flask imports

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'F34TF$($e34D'


@app.route('/', methods=['GET', 'POST'])
def index():
    '''

    '''
    if request.method == 'POST':
        data = request.form['seq']
        print(data)
        d = data.split(',')
        try:
            sentence, sep = d[0], d[1]
            print(f'separator is {sep}')
        except:
            sentence = d[0]
            sep = ''
        dicseq = {'sentence': sentence, 'sep': sep}

        # {'sentence':'ATGGCCA'}
        return render_template('index.html', **dicseq)
    return render_template('index.html')


if __name__ == '__main__':
    port = 5033
    host = '0.0.0.0'
    app.run(port=port, host=host)
