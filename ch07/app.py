#!/usr/bin/python3
#-*- coding: utf-8 -*-

import argparse
import re
import subprocess
from flask import Flask, jsonify, request
from flask import render_template

app = Flask(__name__)

@app.route('/name2', methods=['POST'])
def name2_check():
    if request.method == 'POST':
        return "Hello, " + request.form['firstname'] + '!'

@app.route('/name/<mode>', methods=['GET'])
def name_check(mode):
    return "Hello %s. How are you?\n" % mode

@app.route('/', methods=['GET'])
def hello_test():
    return render_template('hello_test.html')

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="")
        parser.add_argument('--listen-port', type=str, required=True, help='REST service listen port')
        args = parser.parse_args()
        listen_port = args.listen_port
    except Exception as e:
        print('Error: %s' % str(e))

    ipaddr = "127.0.0.1"
    print("Starting the service with ip_addr=" + ipaddr)
    app.run(debug=False, host=ipaddr, port=int(listen_port))