from config import app
from mail import EmailManager
from flask import render_template, redirect, url_for,request
import re

ml = EmailManager()


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/AntiguaAndBarbuda')
def antigua():
    return render_template('AntiguaAndBarbuda.html')


@app.route('/sai')
def sai():
    return render_template('Sai.html')


@app.route('/491subclass')
def subclass491():
    return render_template('491subclass.html')


@app.route('/newsletter')
def newsletter():
    return render_template("newsletter.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/186subclass')
def subclass186():
    return render_template("186subclass.html")


@app.route('/485subclass')
def subclass485():
    return render_template("485subclass.html")


@app.route('/188ASubclass')
def subclass188():
    return render_template("188Asubclass.html")


@app.route('/189subclass')
def subclass189():
    return render_template("189subclass.html")


@app.route('/101subclass')
def subclass101():
    return render_template("101subclass.html")


@app.route('/evaluation', methods=["POST", "GET"])
def evaluation():
    if request.method == "POST":
        ml.send_mail('shunyangli0@gmail.com','在线评估','send_eva',info=request.form)
        return redirect(url_for('hello_world'))
    return render_template('evaluation.html')


@app.route('/search/<info>')
def search(info):
    res = re.findall(r"关于|澳康", info)
    if len(res) != 0:
        return redirect(url_for('about'))

    res = re.findall(r"485|毕业|临时|学生", info)
    if len(res) != 0:
        return redirect(url_for('subclass485'))

    res = re.findall(r"186|雇主|担保|187|482", info)
    if len(res) != 0:
        return redirect((url_for('subclass186')))

    res = re.findall(r"188|投资|商业|132", info)
    if len(res) != 0:
        return redirect((url_for('subclass188')))

    res = re.findall(r"189|技术|独立|489|476", info)
    if len(res) != 0:
        return redirect((url_for('subclass189')))

    res = re.findall(r"101|家庭|配偶|309|100|父母|子女", info)
    if len(res) != 0:
        return redirect((url_for('subclass101')))

    res = re.findall(r"491|偏远|489", info)
    if len(res) != 0:
        return redirect((url_for('subclass491')))

    res = re.findall(r"快讯|新闻", info)
    if len(res) != 0:
        return redirect((url_for('newsletter')))

    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
