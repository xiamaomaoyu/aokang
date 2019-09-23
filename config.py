from flask import Flask

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
# 端口要根据设置来改
# 端口一般是465
app.config['MAIL_PORT'] = 465

# qq使用的不是TLS协议
# 应用了TLS的传输协议
# app.config['MAIL_USE_TLS'] = True

# 应用ssl传输协议
app.config['MAIL_USE_SSL'] = True

# 配置邮件的用户名(仅仅只是qq号，不要@qq.com)
app.config['MAIL_USERNAME'] = '1479201404'

# 邮件账户的密码,这个密码是指的授权码!
# 不是密码，一定要授权码，一般是16位的字符
app.config['MAIL_PASSWORD'] = 'jsgejgmzucsuieed'

# 设置默认发送的邮箱账号（这里要求是123@qq.com，这种格式）
app.config['MAIL_DEFAULT_SENDER'] = '1479201404@qq.com'
