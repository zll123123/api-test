# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
class SendEmail:
    global send_user
    global email_host
    global password
    password = "hwkkecphqauxdgjd"
    email_host = "smtp.qq.com"
    send_user = "2806341129@qq.com"

    def send_mail(self, user_list, sub, content):
        user = "shape" + "<" + send_user + ">"

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message["Subject"] = sub
        message["From"] = user
        message["To"] = ";".join(user_list)

        # 邮件正文内容
        message.attach(MIMEText(content, "plain", "utf-8"))

        # 构造附件（附件为HTML格式的网页）
        filename = "../report/report.html"
        time = datetime.date.today()
        att = MIMEText(open(filename, "rb").read(), "html", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename="%s_Result.html"' % time
        message.attach(att)

        smtp_obj = smtplib.SMTP(email_host, 587)
        smtp_obj.starttls()
        smtp_obj.login(send_user, password)
        smtp_obj.sendmail(user, user_list, message.as_string())
        smtp_obj.quit()

    def send_main(self):
        # user_list = ['xxx@qq.com','xxx@qq.com']
        user_list = ["zhangll2019@foxmail.com"]
        sub = "接口自动化测试报告"
        content = "接口自动化测试结果:见附件"
        self.send_mail(user_list, sub, content)


if __name__ == "__main__":
    SendEmail().send_main()
