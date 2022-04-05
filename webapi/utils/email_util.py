# -*- coding: UTF-8 -*-
import smtplib
import traceback
from email.mime.text import MIMEText

# 系统邮件配置 第三方SMTP服务
SYS_EMAIL_HOST = 'smtp.126.com'  # 设置服务器
SYS_EMAIL_USER = ''  # 邮箱账号
SYS_EMAIL_PWD = ''  # 邮箱密码
SYS_EMAIL_SMTP_PORT = 25  # smtp端口
POST_BASE_URL = 'http://192.168.8.100:8080/post?postId={}'  # 文章基础URL配置


def make_content(post_id: int, post_name: str):
    """
    生成邮件内容
    :param post_id:  文章ID
    :param post_name: 文章标题
    :return:
    """
    mail_template = """
    <p>你评论的文章<i>{post_name}</i>有新的回复</p>
    <p><a href='{post_url}'>点击查看</a></p>
    """
    # 获得完整的文章URL
    post_url = POST_BASE_URL.format(post_id)
    mail_message = mail_template.format(post_name=post_name, post_url=post_url)
    return mail_message


def send_email(receiver: str, post_id: int, post_name: str):
    """
    发送邮件通知
    :param receiver: 邮箱地址
    :param post_id:  文章ID
    :param post_name: 文章标题
    :return:
    """
    sender = SYS_EMAIL_USER
    content = make_content(post_id, post_name)
    message = MIMEText(content, 'html', 'utf-8')
    message['FROM'] = sender
    message['TO'] = receiver
    message['Subject'] = '新回复'

    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(SYS_EMAIL_HOST, SYS_EMAIL_SMTP_PORT)
        smtp_obj.login(SYS_EMAIL_USER, SYS_EMAIL_PWD)
        smtp_obj.sendmail(sender, receiver, message.as_string())
    except smtplib.SMTPException as e:
        traceback.print_exc()


def test_case():
    receiver = '1104440778@qq.com'
    post_id = 1
    post_name = 'FastAPI Vue Blog'
    send_email(receiver, post_id, post_name)


if __name__ == '__main__':
    test_case()
