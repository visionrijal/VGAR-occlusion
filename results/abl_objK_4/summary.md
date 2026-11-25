# Results: abl_objK_4

## RGB-D (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.858 ± 0.043 | 0.893 ± 0.039 | 0.852 ± 0.022 | 0.109 ± 0.017 | 0.199 ± 0.066 | - | - |
| B1 | - | - | - | 0.866 ± 0.026 | 0.082 ± 0.020 | 0.201 ± 0.061 | - | - |
| B2 | 0.996 ± 0.003 | 0.928 ± 0.026 | 0.951 ± 0.019 | 0.868 ± 0.022 | 0.121 ± 0.021 | 0.146 ± 0.056 | 0.011 ± 0.004 | 0.010 ± 0.005 |
| UNet | 0.998 ± 0.002 | 0.942 ± 0.020 | 0.965 ± 0.014 | 0.876 ± 0.022 | 0.106 ± 0.028 | 0.146 ± 0.074 | 0.006 ± 0.003 | 0.005 ± 0.002 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.862 ± 0.042 | 0.896 ± 0.037 | 0.854 ± 0.023 | 0.107 ± 0.017 | 0.202 ± 0.069 | - | - |
| B1 | - | - | - | 0.871 ± 0.026 | 0.077 ± 0.021 | 0.198 ± 0.063 | - | - |
| B2 | 0.996 ± 0.003 | 0.932 ± 0.025 | 0.955 ± 0.018 | 0.874 ± 0.023 | 0.110 ± 0.023 | 0.149 ± 0.058 | 0.010 ± 0.004 | 0.009 ± 0.004 |
| UNet | 0.998 ± 0.002 | 0.944 ± 0.020 | 0.966 ± 0.013 | 0.878 ± 0.022 | 0.104 ± 0.029 | 0.148 ± 0.079 | 0.006 ± 0.003 | 0.005 ± 0.002 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.914 ± 0.064 | 0.818 ± 0.059 | 0.851 ± 0.060 | 0.829 ± 0.023 | 0.130 ± 0.030 | 0.188 ± 0.062 | - | - |
| B1 | - | - | - | 0.816 ± 0.021 | 0.120 ± 0.027 | 0.226 ± 0.054 | - | - |
| B2 | 0.958 ± 0.017 | 0.881 ± 0.034 | 0.912 ± 0.028 | 0.802 ± 0.014 | 0.221 ± 0.041 | 0.133 ± 0.050 | 0.052 ± 0.011 | 0.060 ± 0.014 |
| UNet | 0.979 ± 0.010 | 0.926 ± 0.021 | 0.950 ± 0.017 | 0.857 ± 0.020 | 0.128 ± 0.033 | 0.132 ± 0.054 | 0.030 ± 0.009 | 0.022 ± 0.018 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 8/8 scenes, mean difference +0.0139, Wilcoxon p = 0.00781
- scene level, planes: U-Net better in 7/8 scenes, mean difference +0.0113, Wilcoxon p = 0.0156
- scene level, objects: U-Net better in 8/8 scenes, mean difference +0.0455, Wilcoxon p = 0.00781
- view level (all masks, n = 720 views, not independent): median difference +0.0141, U-Net better in 86% of views, p = 7.33e-85

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.076 ms, 2.186 ms per depth slice, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

## RGB + Depth Anything V2 (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.789 ± 0.061 | 0.822 ± 0.063 | 0.794 ± 0.029 | 0.133 ± 0.031 | 0.315 ± 0.119 | - | - |
| B1 | - | - | - | 0.809 ± 0.030 | 0.108 ± 0.029 | 0.312 ± 0.111 | - | - |
| B2 | 0.991 ± 0.007 | 0.845 ± 0.055 | 0.875 ± 0.054 | 0.808 ± 0.028 | 0.147 ± 0.037 | 0.257 ± 0.110 | 0.019 ± 0.007 | 0.011 ± 0.006 |
| UNet | 0.996 ± 0.002 | 0.847 ± 0.064 | 0.881 ± 0.059 | 0.809 ± 0.029 | 0.141 ± 0.045 | 0.263 ± 0.124 | 0.017 ± 0.006 | 0.012 ± 0.005 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.795 ± 0.059 | 0.829 ± 0.060 | 0.799 ± 0.029 | 0.128 ± 0.030 | 0.317 ± 0.126 | - | - |
| B1 | - | - | - | 0.815 ± 0.030 | 0.102 ± 0.029 | 0.312 ± 0.117 | - | - |
| B2 | 0.992 ± 0.006 | 0.851 ± 0.053 | 0.881 ± 0.052 | 0.815 ± 0.028 | 0.137 ± 0.037 | 0.260 ± 0.118 | 0.018 ± 0.007 | 0.010 ± 0.005 |
| UNet | 0.996 ± 0.002 | 0.852 ± 0.064 | 0.885 ± 0.058 | 0.815 ± 0.029 | 0.134 ± 0.045 | 0.267 ± 0.133 | 0.016 ± 0.005 | 0.012 ± 0.005 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.791 ± 0.095 | 0.711 ± 0.060 | 0.740 ± 0.068 | 0.741 ± 0.029 | 0.186 ± 0.066 | 0.311 ± 0.097 | - | - |
| B1 | - | - | - | 0.747 ± 0.027 | 0.165 ± 0.059 | 0.324 ± 0.090 | - | - |
| B2 | 0.857 ± 0.080 | 0.768 ± 0.060 | 0.801 ± 0.065 | 0.732 ± 0.031 | 0.249 ± 0.080 | 0.240 ± 0.092 | 0.092 ± 0.027 | 0.096 ± 0.035 |
| UNet | 0.844 ± 0.101 | 0.792 ± 0.053 | 0.823 ± 0.055 | 0.750 ± 0.026 | 0.215 ± 0.073 | 0.250 ± 0.098 | 0.079 ± 0.026 | 0.051 ± 0.031 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 6/8 scenes, mean difference +0.0025, Wilcoxon p = 0.312
- scene level, planes: U-Net better in 6/8 scenes, mean difference +0.0004, Wilcoxon p = 0.383
- scene level, objects: U-Net better in 7/8 scenes, mean difference +0.0242, Wilcoxon p = 0.0156
- view level (all masks, n = 720 views, not independent): median difference +0.0071, U-Net better in 68% of views, p = 1.54e-20

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.326 ms, 2.268 ms per depth slice, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

## RGB-only (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.923 ± 0.097 | 0.726 ± 0.088 | 0.753 ± 0.093 | 0.756 ± 0.029 | 0.160 ± 0.049 | 0.382 ± 0.145 | - | - |
| B1 | - | - | - | 0.784 ± 0.034 | 0.115 ± 0.031 | 0.375 ± 0.133 | - | - |
| B2 | 0.918 ± 0.108 | 0.784 ± 0.090 | 0.813 ± 0.091 | 0.780 ± 0.032 | 0.156 ± 0.045 | 0.322 ± 0.141 | 0.064 ± 0.068 | 0.061 ± 0.078 |
| UNet | 0.959 ± 0.058 | 0.798 ± 0.084 | 0.829 ± 0.086 | 0.779 ± 0.032 | 0.131 ± 0.034 | 0.360 ± 0.117 | 0.056 ± 0.044 | 0.059 ± 0.046 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.925 ± 0.096 | 0.736 ± 0.088 | 0.764 ± 0.093 | 0.763 ± 0.029 | 0.153 ± 0.044 | 0.382 ± 0.146 | - | - |
| B1 | - | - | - | 0.791 ± 0.035 | 0.108 ± 0.025 | 0.373 ± 0.134 | - | - |
| B2 | 0.919 ± 0.108 | 0.793 ± 0.091 | 0.822 ± 0.091 | 0.788 ± 0.033 | 0.146 ± 0.038 | 0.322 ± 0.142 | 0.063 ± 0.068 | 0.060 ± 0.078 |
| UNet | 0.960 ± 0.058 | 0.804 ± 0.086 | 0.834 ± 0.088 | 0.786 ± 0.033 | 0.124 ± 0.027 | 0.361 ± 0.118 | 0.055 ± 0.044 | 0.059 ± 0.046 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.642 ± 0.141 | 0.621 ± 0.074 | 0.634 ± 0.089 | 0.690 ± 0.023 | 0.212 ± 0.081 | 0.403 ± 0.146 | - | - |
| B1 | - | - | - | 0.712 ± 0.024 | 0.169 ± 0.064 | 0.411 ± 0.131 | - | - |
| B2 | 0.721 ± 0.138 | 0.682 ± 0.084 | 0.704 ± 0.095 | 0.698 ± 0.025 | 0.242 ± 0.092 | 0.339 ± 0.148 | 0.136 ± 0.055 | 0.139 ± 0.069 |
| UNet | 0.772 ± 0.126 | 0.730 ± 0.073 | 0.757 ± 0.082 | 0.715 ± 0.027 | 0.189 ± 0.071 | 0.373 ± 0.120 | 0.105 ± 0.035 | 0.056 ± 0.036 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 5/8 scenes, mean difference +0.0138, Wilcoxon p = 0.383
- scene level, planes: U-Net better in 5/8 scenes, mean difference +0.0106, Wilcoxon p = 0.383
- scene level, objects: U-Net better in 7/8 scenes, mean difference +0.0476, Wilcoxon p = 0.0156
- view level (all masks, n = 720 views, not independent): median difference +0.0038, U-Net better in 55% of views, p = 5.26e-04

Runtime on NVIDIA A100 80GB PCIe: stats pass 2.902 ms, 2.094 ms per depth slice, U-Net 2.91 ms per 640x480 frame (473,569 parameters).

## Maps (Sequence_2 test views, mean over scenes)

| Condition | PSNR (dB) | median depth error (cm) | depth within 5 cm | Gaussians |
|---|---|---|---|---|
| RGB-D | 29.59 | 2.20 | 81.4% | 342,914 |
| RGB + Depth Anything V2 | 27.70 | 4.35 | 60.4% | 361,215 |
| RGB-only | 25.41 | 15.94 | 43.0% | 153,719 |

Per scene: office_0/rgbd 1.3 cm; office_1/rgbd 1.7 cm; office_2/rgbd 2.5 cm; office_3/rgbd 3.0 cm; office_4/rgbd 3.8 cm; room_0/rgbd 2.2 cm; room_1/rgbd 1.6 cm; room_2/rgbd 1.6 cm; office_0/mono 4.1 cm; office_1/mono 5.3 cm; office_2/mono 3.8 cm; office_3/mono 4.6 cm; office_4/mono 5.4 cm; room_0/mono 4.1 cm; room_1/mono 5.0 cm; room_2/mono 2.6 cm; office_0/rgbonly 4.6 cm; office_1/rgbonly 4.6 cm; office_2/rgbonly 9.1 cm; office_3/rgbonly 25.4 cm; office_4/rgbonly 62.4 cm; room_0/rgbonly 8.2 cm; room_1/rgbonly 6.9 cm; room_2/rgbonly 6.4 cm
