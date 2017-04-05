from flask import Flask, render_template, request
# from bottle import route, run, template, static_file, request, get, post, default_app
import peekyt
import os, time
# , logging

app = Flask(__name__)
app.debug = True
base_dir = os.path.dirname(__file__)

@app.route('/')
def home():
    return render_template('index.html')

# search
@app.route('/search', methods=['POST', 'GET'])
def search():
    search_term=request.form['search_term']
    opt = request.form['opt'] or ""
    # search_log(search_term,opt)
    results = peekyt.search(search_term + " " + opt)
    return render_template('search.html', results=results, search_term=search_term, opt=opt)

# logging.basicConfig(filename=os.path.join(base_dir,'larila.log'),level=logging.INFO)

# # log
# def search_log(search_term,opt):
#     ts = time.strftime("%c")
#     ip = request.remote_addr
#     logging.info("%s\t%s\t%s\t%s\t" % (ts,ip,search_term,opt))
#
# # static files
# @route('/assets/<filepath:path>')
# def server_static(filepath):
#     static_path = os.path.join(base_dir,'assets')
#     return static_file(filepath, root=static_path)
#
# # search
# @route('/search', method='POST')
# def search():
#     search_term=request.forms.get('search_term')
#     opt = request.forms.get('opt') or ""
#     search_log(search_term,opt)
#     results = peekyt.search(search_term + " " + opt)
#     return template('results', results=results, search_term=search_term, opt=opt)
#
# # (test dummy)
# @route('/search_dummy') # si no hay internet...
# def search_dummy():
#     return template('search_dummy')
#
# # about
# @route('/about/<section>')
# def about(section):
#     return template('about', section=section)
#
# # home
# @route('/')
# def root():
#     return template('main')
#
# application = default_app() # for PythonAnywhere's WSGI cfg

if __name__ == '__main__':
    app.run()
