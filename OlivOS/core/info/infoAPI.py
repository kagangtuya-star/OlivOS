# -*- encoding: utf-8 -*-
'''
_______________________    ________________
__  __ \__  /____  _/_ |  / /_  __ \_  ___/
_  / / /_  /  __  / __ | / /_  / / /____ \
/ /_/ /_  /____/ /  __ |/ / / /_/ /____/ /
\____/ /_____/___/  _____/  \____/ /____/

@File      :   OlivOS/infoAPI.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2025, OlivOS-Team
@Desc      :   None
'''

import OlivOS


OlivOS_Version = '0.11.62'
OlivOS_SVN = 182
OlivOS_Version_Slogan = '高筋碱水面包'

# Compatible    <= Plugin[compatible_svn]                 : Compatible
# OldCompatible <= Plugin[compatible_svn] < Compatible    : OldCompatible Warn
#                  Plugin[compatible_svn] < OldCompatible : NotCompatible Error & Skip
OlivOS_SVN_Compatible = 95
OlivOS_SVN_OldCompatible = -1
OlivOS_compatible_svn_default = 0

OlivOS_Version_Short = '%s(%s)' % (OlivOS_Version, str(OlivOS_SVN))
OlivOS_Version_Title = '%s(%s) - %s' % (OlivOS_Version, str(OlivOS_SVN), OlivOS_Version_Slogan)

OlivOS_Header_UA = 'OlivOS/' + OlivOS_Version

OlivOS_message_mode_rx_default = 'old_string'
OlivOS_message_mode_tx_default = 'old_string'
OlivOS_message_mode_tx_unity = 'olivos_string'

OlivOS_plugin_data_path = './plugin/data'

resourceUrlPath = 'https://api.oliva.icu/olivosver/resource_0_11_15/'
