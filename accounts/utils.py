def detectUser(user):
    if user.role == 1:
        redirectUrl = 'adminDashboard'
        return redirectUrl
    elif user.role == 2:
        redirectUrl = 'sekreterDashboard'
        return redirectUrl
    elif user.role == 3:
        redirectUrl = 'supervisorDashboard'
        return redirectUrl
    elif user.role == 4:
        redirectUrl = 'raporDashboard'
        return redirectUrl
    elif user.role == 5:
        redirectUrl = 'agentDashboard'
        return redirectUrl
    elif user.role == None and user.is_superadmin:
        redirectUrl = '/admin'
        return redirectUrl
    
    
    

    