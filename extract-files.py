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
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'vendor/nubia/sm8650-common',
    'hardware/qcom-caf/sm8650',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'libtensorflowlite_jni',
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/lib64/camera/com.qti.ois.ois_dw9781_cerro_ov64b40.so',
        'vendor/lib64/camera/com.qti.ois.ois_dw9784_cerro_imx800.so',
        'vendor/lib64/camera/com.qti.ois.ois_dw9784_cerro_imx906.so',
        'vendor/lib64/camera/com.qti.ois.ois_dw9784_cerro_ov50e40.so',
        'vendor/lib64/camera/com.zte.sensor.imx800_cerro.so',
        'vendor/lib64/camera/com.zte.sensor.imx906_cerro.so',
        'vendor/lib64/camera/com.zte.sensor.ov50e40_cerro.so',
        'vendor/lib64/camera/com.zte.sensor.ov64b40_cerro.so',
        'vendor/lib64/com.qti.feature2.fusion.so',
        'vendor/lib64/hw/camera.qcom.sm8650.so',
        'vendor/lib64/hw/camera.qcom.so',
        'vendor/lib64/libchifeature2.so',
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
    utils = ExtractUtils.device_with_common(module, 'sm8650-common', module.vendor)
    utils.run()
