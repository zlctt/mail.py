#coding=utf-8
import smtplib                              
from email.mime.text import MIMEText        
msg_from='3212973635@qq.com'
passwd='dnsvuellaantdfcc'                
msg_to='57820048@qq.com'                  
subject="2019144130Today_TEST"
content="朱超-一.首先连接校园网手机IP：10.101.104.143，查看IP为220.164.161.com.\n二.切换至数据后手机IP为10.19.95.59，查看IP为172.68.189.21"
msg=MIMEText(content)                       
msg['Subject'] = subject                    
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s=smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from,passwd)
    s.sendmail(msg_from,msg_to,msg.as_string())
    print("发送成功")                       
except(s.SMTPException,e):                  
    print("发送失败")                       
finally:                                    
    s.quit()
