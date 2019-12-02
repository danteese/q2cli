# ----------------------------------------------------------------------------
# Copyright (c) 2016-2019, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# Important notes: 
# Do not get confused about qiime dev refresh-cache this is only 
# for dependencies. 
# This is a very primitive cli in order to use the minimal 
# actions to invoke cache based system to save time in processing
# and files. By default the cache is not initialized in the working
# directory so you should run qiime cache init. 
# The cache is active with the ENV variable QIIME2CACHE 
# set in True, else is not active and should be active by running 
# qiime cache activate. If you want any result without the intervention
# of cache, please disable before running with qiime cache deactivate
# In order to work with cache inside Jupyter please use magic commands
# as pointed here https://stackoverflow.com/questions/37890898/how-to-set-env-variable-in-jupyter-notebook 
# This command do not interact with the qiime framework. The code for
# for this is in qiime2.sdk.cache

# Further development:
# 1. Identify the parent execution 
# 2. Config file with state and local variables

import click
import os

from q2cli.click.command import ToolCommand, ToolGroupCommand

@click.group(help='Utilities for controlling how cache works. This may not be replaced by the group command "dev".',
            cls=ToolGroupCommand)

def cache():
    pass 


@cache.command(name='init',
               short_help='Set up files and directories to work with cache',
               help="This command should be executed in the directory where the user is "
                    "going to work recording the current qiime2 pipeline.",
               cls=ToolCommand)
def init(): 
    import qiime2.sdk
    click.echo("Initializing cache in the current directory.")
    if not qiime2.sdk.get_cache_state(os.getcwd()):
        qiime2.sdk.set_cache_state(os.getcwd(), 1)
    qiime2.sdk.verify_cache_file(os.getcwd())


@cache.command(name="activate",
               short_help='Set env variable qiime-cache to true',
               help="This command verify if the current directory has "
               ".cache directory, else create it and set ENV VAR QIIME2CACHE to true.",
               cls=ToolCommand)
def activate():
    qiime2.sdk.set_cache_state(os.getcwd(), 1)
    qiime2.sdk.verify_cache_file(os.getcwd())
    click.echo("Qiime cache activated.")


@cache.command(name="deactivate",
               short_help='Disable cache env variable',
               help="This command set to false QIIME2CACHE environment",
               cls=ToolCommand)
def deactivate():
    qiime2.sdk.set_cache_state(os.getcwd(), 0)
    click.echo("Qiime cache deactivated.")

