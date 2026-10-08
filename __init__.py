# Copyright (C) 2026 AICG3D
# SPDX-License-Identifier: GPL-3.0-or-later
# -*- coding: utf-8 -*-
"""AICG3D-QwenImage21 —— Qwen-Image 2.1 推理加速节点（输出预测策略，提速 30~40%）"""

from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

# 底层 .pyd 里的品牌字符串是等长替换的（改短会破坏文件内部偏移），
# 短出的字节用空格补在尾部，这里统一去掉首尾空格。
for _cls in NODE_CLASS_MAPPINGS.values():
    _cat = getattr(_cls, "CATEGORY", None)
    if isinstance(_cat, str):
        _cls.CATEGORY = _cat.strip()

NODE_DISPLAY_NAME_MAPPINGS = {
    _k: (_v.strip() if isinstance(_v, str) else _v)
    for _k, _v in NODE_DISPLAY_NAME_MAPPINGS.items()
}
