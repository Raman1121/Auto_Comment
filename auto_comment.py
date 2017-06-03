import facebook

graph = facebook.GraphAPI(access_token = '', version = '2.3')   #Get access token and version from the Graph API official documentation

post = graph.get_object(id = '')   # Post ID here

# Now we have to extract time from this JSON response 
# Put the response in a JSON formatter 

time = post['comments']['data'][0]['created_time']

time = time.split('T')[2]

#Cleaning up the time response 
time_created = time.split('-')[2] 


# REST OF THE CODE HERE 



