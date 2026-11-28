# Results: abl_objK_grid

## RGB-D (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.858 ± 0.043 | 0.893 ± 0.039 | 0.852 ± 0.022 | 0.109 ± 0.017 | 0.199 ± 0.066 | - | - |
| B1 | - | - | - | 0.859 ± 0.026 | 0.088 ± 0.019 | 0.208 ± 0.061 | - | - |
| B2 | 0.996 ± 0.003 | 0.925 ± 0.026 | 0.949 ± 0.019 | 0.860 ± 0.021 | 0.136 ± 0.022 | 0.145 ± 0.054 | 0.011 ± 0.004 | 0.010 ± 0.005 |
| UNet | 0.998 ± 0.002 | 0.940 ± 0.022 | 0.963 ± 0.015 | 0.876 ± 0.021 | 0.110 ± 0.022 | 0.140 ± 0.061 | 0.006 ± 0.003 | 0.005 ± 0.002 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.862 ± 0.042 | 0.896 ± 0.037 | 0.854 ± 0.023 | 0.107 ± 0.017 | 0.202 ± 0.069 | - | - |
| B1 | - | - | - | 0.871 ± 0.026 | 0.077 ± 0.021 | 0.198 ± 0.063 | - | - |
| B2 | 0.996 ± 0.003 | 0.932 ± 0.025 | 0.955 ± 0.018 | 0.874 ± 0.022 | 0.114 ± 0.025 | 0.144 ± 0.056 | 0.010 ± 0.004 | 0.009 ± 0.004 |
| UNet | 0.998 ± 0.002 | 0.941 ± 0.022 | 0.964 ± 0.015 | 0.878 ± 0.021 | 0.107 ± 0.024 | 0.144 ± 0.066 | 0.006 ± 0.003 | 0.005 ± 0.002 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.914 ± 0.064 | 0.818 ± 0.059 | 0.851 ± 0.060 | 0.829 ± 0.023 | 0.130 ± 0.030 | 0.188 ± 0.062 | - | - |
| B1 | - | - | - | 0.741 ± 0.016 | 0.195 ± 0.029 | 0.298 ± 0.050 | - | - |
| B2 | 0.941 ± 0.015 | 0.821 ± 0.032 | 0.860 ± 0.027 | 0.710 ± 0.016 | 0.342 ± 0.046 | 0.157 ± 0.054 | 0.064 ± 0.010 | 0.067 ± 0.015 |
| UNet | 0.978 ± 0.011 | 0.920 ± 0.028 | 0.944 ± 0.022 | 0.855 ± 0.020 | 0.139 ± 0.019 | 0.125 ± 0.042 | 0.030 ± 0.009 | 0.021 ± 0.014 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 8/8 scenes, mean difference +0.0142, Wilcoxon p = 0.00781
- scene level, planes: U-Net better in 7/8 scenes, mean difference +0.0092, Wilcoxon p = 0.0156
- scene level, objects: U-Net better in 8/8 scenes, mean difference +0.0986, Wilcoxon p = 0.00781
- view level (all masks, n = 720 views, not independent): median difference +0.0171, U-Net better in 87% of views, p = 7.21e-85

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.076 ms, 2.186 ms per depth slice, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

## RGB + Depth Anything V2 (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.789 ± 0.061 | 0.822 ± 0.063 | 0.794 ± 0.029 | 0.133 ± 0.031 | 0.315 ± 0.119 | - | - |
| B1 | - | - | - | 0.806 ± 0.030 | 0.111 ± 0.028 | 0.315 ± 0.110 | - | - |
| B2 | 0.991 ± 0.007 | 0.844 ± 0.055 | 0.874 ± 0.054 | 0.804 ± 0.028 | 0.153 ± 0.037 | 0.258 ± 0.111 | 0.019 ± 0.007 | 0.011 ± 0.006 |
| UNet | 0.996 ± 0.002 | 0.842 ± 0.070 | 0.874 ± 0.069 | 0.808 ± 0.029 | 0.145 ± 0.041 | 0.260 ± 0.118 | 0.017 ± 0.006 | 0.012 ± 0.005 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.795 ± 0.059 | 0.829 ± 0.060 | 0.799 ± 0.029 | 0.128 ± 0.030 | 0.317 ± 0.126 | - | - |
| B1 | - | - | - | 0.815 ± 0.030 | 0.102 ± 0.029 | 0.312 ± 0.117 | - | - |
| B2 | 0.992 ± 0.006 | 0.851 ± 0.053 | 0.881 ± 0.052 | 0.815 ± 0.028 | 0.137 ± 0.038 | 0.260 ± 0.118 | 0.018 ± 0.007 | 0.010 ± 0.005 |
| UNet | 0.996 ± 0.002 | 0.847 ± 0.070 | 0.879 ± 0.068 | 0.815 ± 0.028 | 0.137 ± 0.042 | 0.263 ± 0.126 | 0.016 ± 0.005 | 0.011 ± 0.005 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.791 ± 0.095 | 0.711 ± 0.060 | 0.740 ± 0.068 | 0.741 ± 0.029 | 0.186 ± 0.066 | 0.311 ± 0.097 | - | - |
| B1 | - | - | - | 0.710 ± 0.019 | 0.205 ± 0.056 | 0.360 ± 0.081 | - | - |
| B2 | 0.847 ± 0.081 | 0.740 ± 0.051 | 0.776 ± 0.057 | 0.683 ± 0.028 | 0.318 ± 0.085 | 0.250 ± 0.093 | 0.098 ± 0.026 | 0.102 ± 0.035 |
| UNet | 0.849 ± 0.091 | 0.782 ± 0.068 | 0.814 ± 0.075 | 0.741 ± 0.026 | 0.227 ± 0.067 | 0.253 ± 0.094 | 0.079 ± 0.027 | 0.051 ± 0.033 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 5/8 scenes, mean difference -0.0012, Wilcoxon p = 0.547
- scene level, planes: U-Net better in 5/8 scenes, mean difference -0.0038, Wilcoxon p = 0.742
- scene level, objects: U-Net better in 7/8 scenes, mean difference +0.0420, Wilcoxon p = 0.0156
- view level (all masks, n = 720 views, not independent): median difference +0.0067, U-Net better in 67% of views, p = 3.61e-17

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.326 ms, 2.268 ms per depth slice, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

## RGB-only (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.923 ± 0.097 | 0.726 ± 0.088 | 0.753 ± 0.093 | 0.756 ± 0.029 | 0.160 ± 0.049 | 0.382 ± 0.145 | - | - |
| B1 | - | - | - | 0.781 ± 0.033 | 0.118 ± 0.032 | 0.377 ± 0.132 | - | - |
| B2 | 0.918 ± 0.108 | 0.783 ± 0.090 | 0.812 ± 0.091 | 0.778 ± 0.032 | 0.157 ± 0.044 | 0.326 ± 0.139 | 0.064 ± 0.068 | 0.061 ± 0.078 |
| UNet | 0.962 ± 0.052 | 0.795 ± 0.081 | 0.827 ± 0.082 | 0.778 ± 0.030 | 0.132 ± 0.029 | 0.363 ± 0.106 | 0.052 ± 0.039 | 0.054 ± 0.038 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.925 ± 0.096 | 0.736 ± 0.088 | 0.764 ± 0.093 | 0.763 ± 0.029 | 0.153 ± 0.044 | 0.382 ± 0.146 | - | - |
| B1 | - | - | - | 0.791 ± 0.035 | 0.108 ± 0.025 | 0.373 ± 0.134 | - | - |
| B2 | 0.919 ± 0.108 | 0.793 ± 0.091 | 0.822 ± 0.091 | 0.789 ± 0.033 | 0.143 ± 0.035 | 0.325 ± 0.140 | 0.063 ± 0.068 | 0.060 ± 0.078 |
| UNet | 0.963 ± 0.052 | 0.802 ± 0.084 | 0.834 ± 0.084 | 0.787 ± 0.031 | 0.121 ± 0.021 | 0.363 ± 0.109 | 0.052 ± 0.040 | 0.055 ± 0.038 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.642 ± 0.141 | 0.621 ± 0.074 | 0.634 ± 0.089 | 0.690 ± 0.023 | 0.212 ± 0.081 | 0.403 ± 0.146 | - | - |
| B1 | - | - | - | 0.687 ± 0.016 | 0.198 ± 0.068 | 0.433 ± 0.127 | - | - |
| B2 | 0.710 ± 0.137 | 0.660 ± 0.078 | 0.682 ± 0.090 | 0.668 ± 0.021 | 0.282 ± 0.096 | 0.350 ± 0.144 | 0.141 ± 0.053 | 0.144 ± 0.068 |
| UNet | 0.766 ± 0.110 | 0.714 ± 0.057 | 0.743 ± 0.063 | 0.693 ± 0.024 | 0.220 ± 0.068 | 0.380 ± 0.094 | 0.106 ± 0.028 | 0.051 ± 0.030 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 6/8 scenes, mean difference +0.0121, Wilcoxon p = 0.312
- scene level, planes: U-Net better in 6/8 scenes, mean difference +0.0091, Wilcoxon p = 0.383
- scene level, objects: U-Net better in 8/8 scenes, mean difference +0.0535, Wilcoxon p = 0.00781
- view level (all masks, n = 720 views, not independent): median difference +0.0040, U-Net better in 54% of views, p = 6.04e-03

Runtime on NVIDIA A100 80GB PCIe: stats pass 2.902 ms, 2.094 ms per depth slice, U-Net 2.91 ms per 640x480 frame (473,569 parameters).

## Maps (Sequence_2 test views, mean over scenes)

| Condition | PSNR (dB) | median depth error (cm) | depth within 5 cm | Gaussians |
|---|---|---|---|---|
| RGB-D | 29.59 | 2.20 | 81.4% | 342,914 |
| RGB + Depth Anything V2 | 27.70 | 4.35 | 60.4% | 361,215 |
| RGB-only | 25.41 | 15.94 | 43.0% | 153,719 |
| RGB-D, depth fine-tune (control) | 29.89 | 0.90 | 95.3% | 342,914 |
| RGB-D, occlusion fine-tune | 29.63 | 0.93 | 94.9% | 342,914 |
| Depth Anything, depth fine-tune (control) | 25.24 | 12.14 | 28.1% | 361,215 |
| Depth Anything, occlusion fine-tune | 25.12 | 11.64 | 29.6% | 361,215 |

Per scene: office_0/rgbd 1.3 cm; office_1/rgbd 1.7 cm; office_2/rgbd 2.5 cm; office_3/rgbd 3.0 cm; office_4/rgbd 3.8 cm; room_0/rgbd 2.2 cm; room_1/rgbd 1.6 cm; room_2/rgbd 1.6 cm; office_0/mono 4.1 cm; office_1/mono 5.3 cm; office_2/mono 3.8 cm; office_3/mono 4.6 cm; office_4/mono 5.4 cm; room_0/mono 4.1 cm; room_1/mono 5.0 cm; room_2/mono 2.6 cm; office_0/rgbonly 4.6 cm; office_1/rgbonly 4.6 cm; office_2/rgbonly 9.1 cm; office_3/rgbonly 25.4 cm; office_4/rgbonly 62.4 cm; room_0/rgbonly 8.2 cm; room_1/rgbonly 6.9 cm; room_2/rgbonly 6.4 cm; office_0/rgbd_ctl 0.5 cm; office_1/rgbd_ctl 0.6 cm; office_2/rgbd_ctl 0.8 cm; office_3/rgbd_ctl 0.8 cm; office_4/rgbd_ctl 2.6 cm; room_0/rgbd_ctl 0.7 cm; room_1/rgbd_ctl 0.6 cm; room_2/rgbd_ctl 0.6 cm; office_0/rgbd_occ 0.5 cm; office_1/rgbd_occ 0.7 cm; office_2/rgbd_occ 0.8 cm; office_3/rgbd_occ 0.9 cm; office_4/rgbd_occ 2.6 cm; room_0/rgbd_occ 0.8 cm; room_1/rgbd_occ 0.6 cm; room_2/rgbd_occ 0.6 cm; office_0/mono_ctl 13.2 cm; office_1/mono_ctl 19.2 cm; office_2/mono_ctl 8.3 cm; office_3/mono_ctl 12.2 cm; office_4/mono_ctl 10.5 cm; room_0/mono_ctl 6.7 cm; room_1/mono_ctl 18.1 cm; room_2/mono_ctl 9.0 cm; office_0/mono_occ 14.5 cm; office_1/mono_occ 17.6 cm; office_2/mono_occ 6.9 cm; office_3/mono_occ 11.2 cm; office_4/mono_occ 9.7 cm; room_0/mono_occ 7.4 cm; room_1/mono_occ 17.6 cm; room_2/mono_occ 8.2 cm
