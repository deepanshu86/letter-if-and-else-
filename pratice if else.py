
print("Do you want write a letter ")
user=input()
if user=="yes":
   letter='''Dear <[Supervisor's First Name]>,

 I am writing this email to inform you I will be on sick leave from
 <[mention dates]> due to <[mention reason of your sickness]>.
 I have attached my medical documents and the letter from my doctor stating
 the number of days off I need to take from work
 to recover completely.
 I will periodically try to look
 at my emails and respond to urgent calls while I am away from work. I apologise
 for the inconvenience that my absence from work may cause.

 Kindly let me know if any additional documents required to approve my leave.
 In case I need an extension of my leaves, I will let you know as quickly as
 possible. Please let me know if you have questions related to my ongoing
 projects or my leave request.

 Thank you for understanding my situation and for all the support.

 Regards,

 <[Your Name]>'''
   superviser=input("Please enter your supervisor name" )
   date=input("Please enter your mention date " )
   reason=input("Please enter your mention reason " )
   name=input("Please enter your name" )
   letter=letter.replace("<[Supervisor's First Name]>",superviser)
   letter=letter.replace("<[mention dates]>",date)
   letter=letter.replace("<[mention reason of your sickness]>",reason)
   letter=letter.replace("<[Your Name]>",name)
   print(letter)
  
else:
    print("Thank you ... , bye bye .....")
