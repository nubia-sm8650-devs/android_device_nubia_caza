#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/nubia/caza',
    'hardware/qcom-caf/sm8650',
    'hardware/qcom-caf/wlan',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qualcomm.qti.dpm.api@1.0',
        'libtensorflowlite_jni',
        'vendor.qti.ImsRtpService-V1-ndk',
        'vendor.qti.diaghal@1.0',
        'vendor.qti.hardware.dpmaidlservice-V1-ndk',
        'vendor.qti.hardware.dpmservice@1.0',
        'vendor.qti.hardware.qccsyshal@1.0',
        'vendor.qti.hardware.qccsyshal@1.1',
        'vendor.qti.hardware.qccsyshal@1.2',
        'vendor.qti.qesdhal@1.0',
        'vendor.qti.qesdhal@1.1',
        'vendor.qti.qesdhal@1.2',
        'vendor.qti.qesdhal@1.3',
        'vendor.qti.hardware.wifidisplaysession@1.0',
        'vendor.qti.imsrtpservice@3.0',
        'vendor.qti.imsrtpservice@3.1',
        'vendor.qti.qccvndhal_aidl-V1-ndk',
        'libskia',
    ): lib_fixup_vendor_suffix,
    (
        'libar-pal',
        'libar-acdb',
        'liblx-osal',
        'libats',
        'libagm',
        'libpalclient',
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/bin/wfdservice64': blob_fixup()
        .add_needed('libwfdservice_shim.so'),
    'system_ext/lib64/libwfdmmsrc_system.so': blob_fixup()
        .add_needed('libgui_shim.so'),
    'system_ext/lib64/libwfdnative.so': blob_fixup()
        .remove_needed('android.hidl.base@1.0.so')
        .add_needed('libinput_shim.so'),
    'system_ext/lib64/libwfdservice.so': blob_fixup()
        .replace_needed('android.media.audio.common.types-V2-cpp.so', 'android.media.audio.common.types-V4-cpp.so'),
    'vendor/lib64/libcamximageformatutils.so': blob_fixup()
        .remove_needed('android.hardware.graphics.allocator-V1-ndk.so'),
    (
        'vendor/lib64/camera/com.qti.ois.ois_dw9781_cerro_ov64b40.so',
        'vendor/lib64/camera/com.qti.ois.ois_dw9784_cerro_imx800.so',
        'vendor/lib64/camera/com.qti.ois.ois_dw9784_cerro_imx906.so',
        'vendor/lib64/camera/com.qti.ois.ois_dw9784_cerro_ov50e40.so',
        'vendor/lib64/camera/com.zte.sensor.imx800_cerro.so',
        'vendor/lib64/camera/com.zte.sensor.imx906_cerro.so',
        'vendor/lib64/camera/com.zte.sensor.ov50e40_cerro.so',
        'vendor/lib64/camera/com.zte.sensor.ov64b40_cerro.so',
    ): blob_fixup().replace_needed(
        'android.hardware.graphics.allocator-V1-ndk.so',
        'android.hardware.graphics.allocator-V2-ndk.so',
    ),
    'system/priv-app/NubiaCamera/NubiaCamera.apk': blob_fixup().apktool_patch(
        'nubia-camera-patches'
    ),
    'vendor/lib64/hw/sensors.hal.tof.so': blob_fixup()
        .binary_regex_replace(b'\x00input\x00', b'\x00fakei\x00'),
}  # fmt: skip

module = ExtractUtilsModule(
    'cerro',
    'nubia',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
