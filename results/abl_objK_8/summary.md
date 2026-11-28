# Results: abl_objK_8

## RGB-D (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.858 ± 0.043 | 0.893 ± 0.039 | 0.852 ± 0.022 | 0.109 ± 0.017 | 0.199 ± 0.066 | - | - |
| B1 | - | - | - | 0.869 ± 0.026 | 0.078 ± 0.021 | 0.197 ± 0.060 | - | - |
| B2 | 0.996 ± 0.003 | 0.930 ± 0.025 | 0.953 ± 0.019 | 0.870 ± 0.020 | 0.119 ± 0.023 | 0.142 ± 0.057 | 0.011 ± 0.004 | 0.009 ± 0.005 |
| UNet | 0.998 ± 0.002 | 0.943 ± 0.021 | 0.965 ± 0.014 | 0.879 ± 0.020 | 0.102 ± 0.026 | 0.143 ± 0.060 | 0.006 ± 0.003 | 0.005 ± 0.002 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.862 ± 0.042 | 0.896 ± 0.037 | 0.854 ± 0.023 | 0.107 ± 0.017 | 0.202 ± 0.069 | - | - |
| B1 | - | - | - | 0.871 ± 0.026 | 0.077 ± 0.021 | 0.198 ± 0.063 | - | - |
| B2 | 0.996 ± 0.003 | 0.932 ± 0.025 | 0.955 ± 0.018 | 0.873 ± 0.021 | 0.114 ± 0.023 | 0.146 ± 0.060 | 0.010 ± 0.004 | 0.009 ± 0.004 |
| UNet | 0.998 ± 0.002 | 0.944 ± 0.021 | 0.966 ± 0.014 | 0.880 ± 0.021 | 0.101 ± 0.027 | 0.146 ± 0.066 | 0.006 ± 0.003 | 0.005 ± 0.002 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.914 ± 0.064 | 0.818 ± 0.059 | 0.851 ± 0.060 | 0.829 ± 0.023 | 0.130 ± 0.030 | 0.188 ± 0.062 | - | - |
| B1 | - | - | - | 0.847 ± 0.025 | 0.087 ± 0.027 | 0.198 ± 0.055 | - | - |
| B2 | 0.970 ± 0.014 | 0.907 ± 0.032 | 0.932 ± 0.026 | 0.841 ± 0.017 | 0.162 ± 0.042 | 0.126 ± 0.052 | 0.042 ± 0.011 | 0.050 ± 0.015 |
| UNet | 0.980 ± 0.010 | 0.932 ± 0.023 | 0.953 ± 0.018 | 0.870 ± 0.019 | 0.113 ± 0.027 | 0.124 ± 0.039 | 0.028 ± 0.007 | 0.020 ± 0.010 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 8/8 scenes, mean difference +0.0127, Wilcoxon p = 0.00781
- scene level, planes: U-Net better in 7/8 scenes, mean difference +0.0114, Wilcoxon p = 0.0156
- scene level, objects: U-Net better in 8/8 scenes, mean difference +0.0256, Wilcoxon p = 0.00781
- view level (all masks, n = 720 views, not independent): median difference +0.0122, U-Net better in 83% of views, p = 9.19e-74

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.076 ms, 2.186 ms per depth slice, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

## RGB + Depth Anything V2 (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.789 ± 0.061 | 0.822 ± 0.063 | 0.794 ± 0.029 | 0.133 ± 0.031 | 0.315 ± 0.119 | - | - |
| B1 | - | - | - | 0.810 ± 0.029 | 0.106 ± 0.029 | 0.310 ± 0.110 | - | - |
| B2 | 0.991 ± 0.007 | 0.845 ± 0.054 | 0.876 ± 0.053 | 0.810 ± 0.028 | 0.144 ± 0.038 | 0.256 ± 0.110 | 0.019 ± 0.007 | 0.011 ± 0.006 |
| UNet | 0.995 ± 0.002 | 0.840 ± 0.073 | 0.873 ± 0.070 | 0.810 ± 0.029 | 0.140 ± 0.045 | 0.262 ± 0.131 | 0.017 ± 0.006 | 0.011 ± 0.005 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.795 ± 0.059 | 0.829 ± 0.060 | 0.799 ± 0.029 | 0.128 ± 0.030 | 0.317 ± 0.126 | - | - |
| B1 | - | - | - | 0.815 ± 0.030 | 0.102 ± 0.029 | 0.312 ± 0.117 | - | - |
| B2 | 0.992 ± 0.006 | 0.851 ± 0.053 | 0.881 ± 0.052 | 0.815 ± 0.028 | 0.138 ± 0.037 | 0.259 ± 0.118 | 0.018 ± 0.007 | 0.010 ± 0.005 |
| UNet | 0.996 ± 0.002 | 0.845 ± 0.073 | 0.878 ± 0.069 | 0.815 ± 0.029 | 0.135 ± 0.044 | 0.266 ± 0.140 | 0.016 ± 0.006 | 0.011 ± 0.005 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.791 ± 0.095 | 0.711 ± 0.060 | 0.740 ± 0.068 | 0.741 ± 0.029 | 0.186 ± 0.066 | 0.311 ± 0.097 | - | - |
| B1 | - | - | - | 0.762 ± 0.027 | 0.148 ± 0.060 | 0.312 ± 0.087 | - | - |
| B2 | 0.867 ± 0.077 | 0.783 ± 0.061 | 0.815 ± 0.065 | 0.754 ± 0.032 | 0.215 ± 0.079 | 0.240 ± 0.090 | 0.087 ± 0.028 | 0.090 ± 0.037 |
| UNet | 0.835 ± 0.109 | 0.786 ± 0.072 | 0.814 ± 0.076 | 0.759 ± 0.029 | 0.201 ± 0.084 | 0.248 ± 0.113 | 0.079 ± 0.028 | 0.057 ± 0.036 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 6/8 scenes, mean difference -0.0054, Wilcoxon p = 0.742
- scene level, planes: U-Net better in 6/8 scenes, mean difference -0.0063, Wilcoxon p = 0.742
- scene level, objects: U-Net better in 5/8 scenes, mean difference +0.0024, Wilcoxon p = 0.742
- view level (all masks, n = 720 views, not independent): median difference +0.0047, U-Net better in 63% of views, p = 2.58e-11

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.326 ms, 2.268 ms per depth slice, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

## RGB-only (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.923 ± 0.097 | 0.726 ± 0.088 | 0.753 ± 0.093 | 0.756 ± 0.029 | 0.160 ± 0.049 | 0.382 ± 0.145 | - | - |
| B1 | - | - | - | 0.785 ± 0.034 | 0.113 ± 0.029 | 0.374 ± 0.133 | - | - |
| B2 | 0.918 ± 0.108 | 0.785 ± 0.090 | 0.813 ± 0.091 | 0.781 ± 0.033 | 0.153 ± 0.045 | 0.323 ± 0.143 | 0.064 ± 0.068 | 0.061 ± 0.078 |
| UNet | 0.963 ± 0.054 | 0.811 ± 0.083 | 0.841 ± 0.084 | 0.784 ± 0.032 | 0.131 ± 0.033 | 0.347 ± 0.114 | 0.053 ± 0.040 | 0.056 ± 0.038 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.925 ± 0.096 | 0.736 ± 0.088 | 0.764 ± 0.093 | 0.763 ± 0.029 | 0.153 ± 0.044 | 0.382 ± 0.146 | - | - |
| B1 | - | - | - | 0.791 ± 0.035 | 0.108 ± 0.025 | 0.373 ± 0.134 | - | - |
| B2 | 0.919 ± 0.108 | 0.793 ± 0.091 | 0.822 ± 0.091 | 0.788 ± 0.033 | 0.145 ± 0.040 | 0.323 ± 0.143 | 0.063 ± 0.068 | 0.060 ± 0.078 |
| UNet | 0.964 ± 0.053 | 0.817 ± 0.085 | 0.847 ± 0.087 | 0.790 ± 0.033 | 0.124 ± 0.027 | 0.349 ± 0.116 | 0.052 ± 0.040 | 0.056 ± 0.038 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.642 ± 0.141 | 0.621 ± 0.074 | 0.634 ± 0.089 | 0.690 ± 0.023 | 0.212 ± 0.081 | 0.403 ± 0.146 | - | - |
| B1 | - | - | - | 0.725 ± 0.026 | 0.152 ± 0.057 | 0.403 ± 0.133 | - | - |
| B2 | 0.731 ± 0.141 | 0.694 ± 0.088 | 0.715 ± 0.098 | 0.715 ± 0.026 | 0.213 ± 0.084 | 0.340 ± 0.149 | 0.132 ± 0.056 | 0.136 ± 0.069 |
| UNet | 0.784 ± 0.105 | 0.746 ± 0.058 | 0.772 ± 0.065 | 0.724 ± 0.030 | 0.189 ± 0.065 | 0.351 ± 0.103 | 0.098 ± 0.029 | 0.050 ± 0.027 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 6/8 scenes, mean difference +0.0262, Wilcoxon p = 0.0547
- scene level, planes: U-Net better in 6/8 scenes, mean difference +0.0234, Wilcoxon p = 0.0781
- scene level, objects: U-Net better in 7/8 scenes, mean difference +0.0517, Wilcoxon p = 0.0781
- view level (all masks, n = 720 views, not independent): median difference +0.0091, U-Net better in 62% of views, p = 6.79e-15

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
