#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from nubia sm8650-common
$(call inherit-product, device/nubia/sm8650-common/common.mk)

DEVICE_PATH := device/nubia/cerro

# Audio
PRODUCT_COPY_FILES += \
    $(DEVICE_PATH)/audio/audio_policy_configuration.xml:$(TARGET_COPY_OUT_VENDOR)/etc/audio/sku_pineapple/audio_policy_configuration.xml \
    $(DEVICE_PATH)/audio/mixer_paths_pineapple_mtp.xml:$(TARGET_COPY_OUT_VENDOR)/etc/audio/sku_pineapple/mixer_paths_pineapple_mtp.xml \
    $(DEVICE_PATH)/audio/resourcemanager_pineapple_mtp.xml:$(TARGET_COPY_OUT_VENDOR)/etc/audio/sku_pineapple/resourcemanager_pineapple_mtp.xml \
    $(DEVICE_PATH)/audio/usecaseKvManager.xml:$(TARGET_COPY_OUT_VENDOR)/etc/usecaseKvManager.xml

# Display
PRODUCT_COPY_FILES += \
    $(DEVICE_PATH)/configs/display_id_4630946566460097411.xml:$(TARGET_COPY_OUT_VENDOR)/etc/displayconfig/display_id_4630946566460097411.xml

# Inherit from proprietary targets
$(call inherit-product, vendor/nubia/cerro/cerro-vendor.mk)
