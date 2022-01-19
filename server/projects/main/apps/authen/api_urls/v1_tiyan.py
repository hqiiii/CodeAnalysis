# -*- coding: utf-8 -*-
# Copyright (c) 2021-2022 THL A29 Limited
#
# This source code file is made available under MIT License
# See LICENSE for details
# ==============================================================================

"""
v1 接口定义，供节点端/ 外界调用

URL前缀：/api/authen/
"""
# 第三方 import
from django.urls import path

# 项目内 import
from apps.authen.apis import v1 as apis_v1

# 前缀/api/authen/
urlpatterns = [
    path("urlauth/", apis_v1.ProxyServerAuthenticationAPIView.as_view(), name="apiv1_tiyan_authen_urlauth"),
]
