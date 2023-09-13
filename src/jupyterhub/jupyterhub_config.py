import os
import sys
import shutil
from jupyter_client.localinterfaces import public_ips

c = get_config()  #noqa

# c.SudoSpawner.sudospawner_path = '/*actual path*/sudospawner'
c.JupyterHub.spawner_class = 'dockerspawner.SwarmSpawner'
#------------------------------------------------------------------------------

c.JupyterHub.hub_ip = public_ips()[0]
c.JupyterHub.admin_access = True
c.Authenticator.admin_users = {'ansoncar',"Teresa","Maura"}
c.Authenticator.allowed_users = {'ansoncar',"Teresa","Maura"}
c.LocalAuthenticator.group_whitelist = ['hub']
c.JupyterHub.authenticator_class = 'firstuseauthenticator.FirstUseAuthenticator'
c.LocalAuthenticator.create_system_users = True
c.JupyterHub.statsd_prefix = 'jupyterhub'

#shutdown the server after no activity for an hour
c.ServerApp.shutdown_no_activity_timeout = 60 * 60
#shutdown kernels after no activity for 30 minutes
c.MappingKernelManager.cull_idle_timeout = 30 * 60
#check for idle kernels every two minutes
c.MappingKernelManager.cull_interval = 2 * 60