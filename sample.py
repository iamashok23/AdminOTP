import adminotp
import sendmail1
details={
        505 : ["Ashok","PFS21","ashokmangali631@gmail.com",25000],
        606 : ["Vinod","DA7","vinodkumarnaikmegavath502@gmail.com",35000],
        707 : ["Rahul","DS6","rahulkondu5gmail.com",50000]
    } 
admin_email = input("Enter Admin email id: ")
x = adminotp.otp(admin_email)
if x == True:
    print("Mails sending in progress")
    for data in details:
        if details[data][-1] < 50000:
            sendmail1.send_message1(details[data][1],details[data][0],details[data][-1])

    print("All Mails sent Successfully")
else:
    print("Wrong OTP Entered, Verification Failed !")

