from InstagramAPI import InstagramAPI
import time
import tkinter
from Tkinter import *

def main_account_screen():
    global main_screen
    main_screen = Tk()
   # main_screen = Toplevel(main_screen)
    main_screen.title("Login")
    main_screen.geometry("300x250")
    Label(main_screen, text="Please enter details below to login").pack()
    Label(main_screen, text="").pack()
    
    global username_l
    global password_l
    username_l = StringVar()
    password_l = StringVar()
    
    Label(main_screen, text="Username  ").pack()
    username_login_entry = Entry(main_screen, textvariable=username_l)
    username_login_entry.pack()
    
    Label(main_screen, text="").pack()
    Label(main_screen, text="Password * ").pack()
    password_login_entry = Entry(main_screen, textvariable=password_l, show= '*')
    password_login_entry.pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Login", width=10, height=1, command = logging_in).pack()
    
    main_screen.mainloop()
 
def logging_in():
    username=username_l.get()
    password=password_l.get()

    
    
    global InstagramAPI
    global user_id
    InstagramAPI = InstagramAPI(username, password)
    login = InstagramAPI.login()
    InstagramAPI.getProfileData()
    user_id=InstagramAPI.LastJson['user']['pk']

    InstagramAPI.getProfileData()
    user_id=InstagramAPI.LastJson['user']['pk']
    
    global following_list
    InstagramAPI.getUserFollowings(user_id)
    following_list=InstagramAPI.LastJson['users']
    
    global followers_list
    InstagramAPI.getUserFollowers(user_id)
    followers_list=InstagramAPI.LastJson['users']

            
    if login == True:
        #Button(text="Login", height="2", width="30", command = user_screen).pack()
        #Label(text="").pack()
        print "logged in"
        global functions_screen
        functions_screen = Toplevel(main_screen)
        functions_screen.title("Functions")
        functions_screen.geometry("300x250")
        Label(functions_screen, text="Please choose").pack()
        Label(functions_screen, text="").pack()
        Button(functions_screen, text="Follower", width=10, height=1, command = follower).pack()
        Button(functions_screen, text="Following", width=10, height=1, command = following).pack()
        Button(functions_screen, text="Unfollower", width=10, height=1, command = unfollower).pack()
        Button(functions_screen, text="Show Unfollower", width=10, height=1, command = show_unfollower).pack()

def following():
    followers   = []
  
    next_max_id = True
    while next_max_id:
        print next_max_id
        #first iteration hack
        if next_max_id == True: next_max_id=''
        _ = InstagramAPI.getUserFollowers(user_id,maxid=next_max_id)
        followers.extend ( InstagramAPI.LastJson.get('users',[]))
        next_max_id = InstagramAPI.LastJson.get('next_max_id','')
        time.sleep(1)
    
    followers_list=followers
    user_list = map(lambda x: x['username'] , following_list)
    following_set= set(user_list)
    print len(following_set)
    Label(functions_screen, text=len(following_set)).pack()
    
    
def follower():
    followers   = []
  
    next_max_id = True
    while next_max_id:
        print next_max_id
        #first iteration hack
        if next_max_id == True: next_max_id=''
        _ = InstagramAPI.getUserFollowers(user_id,maxid=next_max_id)
        followers.extend ( InstagramAPI.LastJson.get('users',[]))
        next_max_id = InstagramAPI.LastJson.get('next_max_id','')
        time.sleep(1)
        
    followers_list=followers
    user_list = map(lambda x: x['username'] , followers_list)
    followers_set= set(user_list)
    print len(followers_set)
    Label(functions_screen, text=len(followers_set)).pack()
    
    
def unfollower():
    followers   = []
  
    next_max_id = True
    while next_max_id:
        print next_max_id
        #first iteration hack
        if next_max_id == True: next_max_id=''
        _ = InstagramAPI.getUserFollowers(user_id,maxid=next_max_id)
        followers.extend ( InstagramAPI.LastJson.get('users',[]))
        next_max_id = InstagramAPI.LastJson.get('next_max_id','')
        time.sleep(1)
        
    followers_list=followers
    user_list = map(lambda x: x['username'] , following_list)
    following_set= set(user_list)
    user_list = map(lambda x: x['username'] , followers_list)
    followers_set= set(user_list)
    
    not_following_back=following_set-followers_set
    
    Label(functions_screen, text=len(not_following_back)).pack()

def show_unfollower():    
    followers   = []
  
    next_max_id = True
    while next_max_id:
        print next_max_id
        #first iteration hack
        if next_max_id == True: next_max_id=''
        _ = InstagramAPI.getUserFollowers(user_id,maxid=next_max_id)
        followers.extend ( InstagramAPI.LastJson.get('users',[]))
        next_max_id = InstagramAPI.LastJson.get('next_max_id','')
        time.sleep(1)
        
    followers_list=followers
    user_list = map(lambda x: x['username'] , following_list)
    following_set= set(user_list)
    user_list = map(lambda x: x['username'] , followers_list)
    followers_set= set(user_list)
    
    not_following_back=following_set-followers_set
    Label(functions_screen, text="\n".join(map(str, not_following_back))).pack()

main_account_screen()