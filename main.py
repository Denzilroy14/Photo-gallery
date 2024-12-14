import os
from flask import*
app=Flask(__name__)
IMAGE_FOLDER=os.path.join('static','images')
app.config['FOLDER']=IMAGE_FOLDER
@app.route('/')
@app.route('/home')
def home():
    data=os.listdir(app.config['FOLDER'])
    return render_template('homepage.html',data=data)
@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['FOLDER'],filename,as_attachment=True)
if __name__=='__main__':
    if not os.path.exists(app.config['FOLDER']):
        os.makedirs(app.config['FOLDER'])
    app.run(debug=True)