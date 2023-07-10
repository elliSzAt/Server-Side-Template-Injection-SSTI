Bài này cung cấp source code, nên chúng ta sẽ thực tải source code về để phân tích:

server_ch73.py

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author             : Podalirius

import jinja2
from flask import Flask, flash, redirect, render_template, request, session, abort

mail = """
Hello team,

A new hacker wants to join our private Bug bounty program! Mary, can you schedule an interview?

 - Name: {{ hacker_name }}
 - Surname: {{ hacker_surname }}
 - Email: {{ hacker_email }}
 - Birth date: {{ hacker_bday }}

I'm sending you the details of the application in the attached CSV file:

 - '{{ hacker_name }}{{ hacker_surname }}{{ hacker_email }}{{ hacker_bday }}.csv'

Best regards,
"""

def sendmail(address, content):
    try:
        content += "\n\n{{ signature }}"
        _signature = """---\n<b>Offsec Team</b>\noffsecteam@hackorp.com"""
        content = jinja2.Template(content).render(signature=_signature)
        print(content)
    except Exception as e:
        pass
    return None

def sanitize(value):
    blacklist = ['{{','}}','{%','%}','import','eval','builtins','class','[',']']
    #blacklist =[]
    for word in blacklist:
        if word in value:
            value = value.replace(word,'')
    if any([bool(w in value) for w in blacklist]):
        value = sanitize(value)
    return value

app = Flask(__name__, template_folder="./templates/", static_folder="./static/")
app.config['DEBUG'] = False

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.route("/", methods=['GET','POST'])
def register():
    global mail
    if request.method == "POST":
        #if "name" in request.form.keys() and len(request.form["name"]) != 0 and "surname" in request.form.keys() and len(request.form["surname"]) != 0 and "email" in request.form.keys() and len(request.form["email"]) != 0 and "bday" in request.form.keys() and len(request.form["bday"]) != 0 :
        if True:
            '''if len(request.form["name"]) > 20:
                return render_template("index.html", error="Field 'name' is too long.")
            if len(request.form["surname"]) >= 50:
                return render_template("index.html", error="Field 'surname' is too long.")
            if len(request.form["email"]) >= 50:
                return render_template("index.html", error="Field 'email' is too long.")
            if len(request.form["bday"]) > 10:
                return render_template("index.html", error="Field 'bday' is too long.")'''
            try:
                register_mail = jinja2.Template(mail).render(
                    hacker_name=sanitize(request.form["name"]),
                    hacker_surname=sanitize(request.form["surname"]),
                    hacker_email=sanitize(request.form["email"]),
                    hacker_bday=sanitize(request.form["bday"])
                )
            except Exception as e:
                pass
            sendmail("offsecteam@hackorp.com", register_mail)
            return render_template("index.html", success='OK')
        else:
            return render_template("index.html", error="Missing fields in the application form!")
    elif request.method == 'GET':
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=59073)
```

Đây là 1 form gồm có 4 field input để nhập name, surname, email và birthday. Có 1 số điểm ta cần lưu ý:

  -  Độ dài tối đa của name là 20, surname là 50, email là 50 và birthday là 10.
  -  Hàm sanitize sẽ thực hiện xóa kí tự nằm trong blacklist ra khỏi các chuỗi nhập vào.

Trong bài này templete được sử dụng là jinja2, nhưng tất cả ``{{, }}, {%, %}`` đã bị filter.

![image](https://github.com/elliSzAt/Server-Side-Template-Injection-SSTI/assets/125866921/f7b11482-01e3-4e89-80e6-9634bb0d8bfb)

Trong phần nội dung của mail sẽ được sử dụng trong phần sendmail có một tạo thành filename của file .csv mà ở đây nội dung do chúng ta nhập vào (name, surname, email, birthday) sẽ được viết liền nhau.

Do đó mình có thể lợi dụng điều này để tạo ra các cặp ``{{, }}, {%. %}`` theo ý thích.

Mình sẽ nhập vào như sau:

  -  Name={
  -  Surname={ 9*9
  -  Email=}
  -  Birthday=}

![image](https://github.com/elliSzAt/Server-Side-Template-Injection-SSTI/assets/125866921/0693c588-af4f-4d30-94b1-5f30c3b205f9)

Giờ chúng ta sẽ thấy kết quả chỗ .csv sẽ trở thành 81hi.csv, chứng tỏ chúng ta sẽ thực hiện khai thác SSTI được.

Ở challenge lần này còn bị filter thêm một số khác như ``builtins, class, import,[,]``. Nên mình sẽ lựa chọn payload mà mình thấy thích hợp nhất.

``{{ cycler.__init__.__globals__.os.popen('command').read() }}``


