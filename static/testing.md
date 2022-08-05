


# User Story testing

Issue No. | Title | Acceptance criteria | Testing carried out
----------|-------|---------------------|-------------------------
#01 | Manage posts | Admin can create, update or remove posts | Ensured that the admin user has full functionality of the create/delete/edit buttons by creating and deleting posts multiple times
#02 | Account registration | Easy registration process and login/logout process | Manually tested the registration form several times to ensure it works properly as well as logged in and logged out many times
#03|  Create post | The registered users can create posts pending approval from admin user | Ensure the creating, editing, viewing and deleting post is appropriately processed and that the procedures are straight forward. Restrict the editing and deleting post process to user's own entry only except for superusers
#04 | Create Drafts | Admin can create drafts that dont appear on the home page | Manually tested the draft dropdown menu and posted multiple drafts , also made sure they are not appearing outside of the django admin page.
#05 | Site pagination | User can select each item to view and change pages | Created multiple user profiles and multiple posts in order to check if everything works, also clicked the "Next" button to make sure it goes to next page
#06 | View Address | User can see posters address on main page | Made multiple posts and logged out to ensure I can still see the address for each post
#07 | View post list | All site visitor users can view the post list | Making sure every single post is visible on the home page to every user regardless if hes logged in or not, also making sure posts with draft status aren't visible. 
#08 | Open a post | Every user can open an individual post and view the contents inside but not interract with the post | Ensured the post details are available to everyone that clicks on the individual post, tested the link that opens post and it never failed, also made sure non-authenticated users cannot interract with the post at all
#09 | Phone Number | Every user can click on post details and see posters phone number | Created multiple user profiles and multiple posts where I added my number then logged out to make sure any non-authenticated or authenticated user can see the phone number
#10 | Big picture | A good sized picture of the item visible in post details | Manually added multiple posts and uploaded many different images to make sure they are properly displayed in the post details page, also checked if they are responsive
#11 | Delete a post | Authenticated user can delete his own posts but no one else's | Manually created multiple users and made a single post for each, then i logged in to different accounts to make sure a user can only delete his own post
#12 | Like/Unlike | Likes are visible to everyone but only registered users can interract with the button | Made sure I cannot use the like button while logged out, tested if it worked while i was logged in and checked to see if I can remove a like aswell as add a like to a post
#13 | View Likes | Likes properly saved and displayed on the homepage/post details | Liked and unliked manually on different user profiles and refreshed many times to see if they displayed properly on both pages
#14 | Searchbar | Not implemented | No tests
#15 | Comment | Not implemented | No tests
#16 | Approve Comments| Not implemented | No tests

## Manual Testing 

| Feature| Acceptance Criteria | Tests Carried out | Result |  
| --- | --- | --- | --- | 
| Admin CRUD | Admin account can create/update/delete posts | Created admin account, logged in and clicked every button for create,update or delete| Pass |
| Admin restricted access | Access to admin page is not available to normal users | Created a normal user and attempted to log into the admin page | Pass |
| Non Authenticated user/like  | Like button is visible but not activated/interractable | Logged out and refreshed the page to test if I can use the like button | Pass |  
| Non Authenticated user/create  | Post Item option is not visible if you're logged out|Logged out and refreshed the page many times, clicked on different pages of the website to check if Post Item is visible| Pass | 
| Registration/ left blank |A message appearing that says "fill out this field"| Attempted to create an account with fields left blank or adding a space and then clicking sign up| Pass | 
| Registration/ bad email| A message appearing that instructs you about email address format| Tried creating an account by using random letters and numbers, also by not finishing the address after "@"| Pass | 
| Registration/ Common Password |A message appearing that instructs you the password is too common| Added a password that was very simple and easy to guess such as "password"| Pass | 
| Registration/ Short Password |A message appearing that says your password is too short and it must contain 8 characters | Created account and added password "123"| Pass | 
| Login/ Blank Field | A message instructing you to fill out this field|Attempted to log in without filling up the username field | Pass | 
|Login/ Incorrect Username|A message that says "username or password you specified are not correct"|Tried logging in with random letters and numbers in the username field| Pass |
|Login/ Incorrect Password| A message that says "username or password you specified are not correct"|Tried logging in with random letters and numbers in the password field| Pass |
|Logged in/ like  | Like button is visible and active| Created a new user, logged in and clicked on the like button to see if I can interract with it| Pass | 
|Logged in/ Post Item  |Post Item button is visible in navigation bar|Created a new user and logged in, checked in the top left to see if Post Item was there, also clicked on it| Pass | 
|Post Item/ no image |The placeholder image should take its place| Created a new account and logged in, created a new post but didn't upload a picture and refreshed to check the homepage | Pass |
|Post Item/ Blank Fields |Not allowed to post if required fields are empty| Logged in and pressed on Post Item button, left every field empty and pressed on Post| Pass |
| Delete/ not author |Button should say "Delete not available"|Logged in on admin, created a post and then logged out and into another account. Checked the post I created previously and the delete button| Pass |
| Delete/ author |Delete button should be available and visible|Created a post on an account and then refreshed the homepage, clicked on the post and scrolled down to see the delete button| Pass | 
| Delete page|Page should pop up asking if you're sure you want to delete|Clicked on my own post, scrolled down and clicked the delete button| Pass |
|Message/ login | Message appears confirming successful login |Logged in on an account| Pass |
|Logout Page |Page pops up asking the user to confirm logout| Clicked on log out button| Pass |
|Message/ logout |Message appears confirming successful logout|Clicked on the log out button and then again on log out| Pass |
|Message/ Post Item|Message appears confirming your successful post| Clicked on post item and filled out the form, then clicked on post| Pass |
|Pagination|Next button appears on the bottom of the page and its clickable|Scrolled down and clicked on next button| Pass |
|Footer Socials|Social icons appear in the footer and open their pages in a new tab| Clicked on the social icons on the bottom of the page| Pass |


