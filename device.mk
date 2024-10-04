#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/nubia/caza

# Soong
PRODUCT_SOONG_NAMESPACES += \
    $(DEVICE_PATH)

# Inherit from proprietary targets
$(call inherit-product, vendor/nubia/caza/caza-vendor.mk)
