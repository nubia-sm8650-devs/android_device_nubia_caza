#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from device.
$(call inherit-product, device/nubia/cerro/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Boot animation
TARGET_SCREEN_HEIGHT := 2480
TARGET_SCREEN_WIDTH := 1116

PRODUCT_BRAND := nubia
PRODUCT_DEVICE := cerro
PRODUCT_MANUFACTURER := nubia
PRODUCT_MODEL := NX721J
PRODUCT_NAME := lineage_cerro
PRODUCT_SYSTEM_DEVICE := PQ83A01
PRODUCT_SYSTEM_NAME := PQ83A01-UN

PRODUCT_GMS_CLIENTID_BASE := android-zte

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="PQ83A01-UN PQ83A01 14 UKQ1.230917.001 20240203.100147 release-keys" \
    BuildFingerprint=nubia/PQ83A01-UN/PQ83A01:14/UKQ1.230917.001/20240203.100147:user/release-keys \
    DeviceName=$(PRODUCT_SYSTEM_DEVICE) \
    DeviceProduct=$(PRODUCT_SYSTEM_NAME)
