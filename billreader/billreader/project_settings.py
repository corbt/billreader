import os
from billreader.settings import MEDIA_ROOT

#MEDIA_ROOT is the general directory for static user-uploaded content

#USERS_ROOT is a subdirectory containing each user's information
USER_ROOT=os.path.join(MEDIA_ROOT,'userdata')