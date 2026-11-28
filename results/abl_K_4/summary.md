# Results: abl_K_4

## RGB-D (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.858 ± 0.043 | 0.893 ± 0.039 | 0.852 ± 0.022 | 0.109 ± 0.017 | 0.199 ± 0.066 | - | - |
| B1 | - | - | - | 0.632 ± 0.025 | 0.399 ± 0.039 | 0.293 ± 0.061 | - | - |
| B2 | 0.930 ± 0.014 | 0.749 ± 0.028 | 0.762 ± 0.029 | 0.644 ± 0.026 | 0.345 ± 0.056 | 0.371 ± 0.081 | 0.089 ± 0.010 | 0.041 ± 0.011 |
| UNet | 0.998 ± 0.002 | 0.935 ± 0.022 | 0.960 ± 0.015 | 0.868 ± 0.022 | 0.108 ± 0.026 | 0.161 ± 0.068 | 0.007 ± 0.002 | 0.005 ± 0.002 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.862 ± 0.042 | 0.896 ± 0.037 | 0.854 ± 0.023 | 0.107 ± 0.017 | 0.202 ± 0.069 | - | - |
| B1 | - | - | - | 0.606 ± 0.031 | 0.432 ± 0.037 | 0.309 ± 0.077 | - | - |
| B2 | 0.930 ± 0.014 | 0.723 ± 0.039 | 0.736 ± 0.040 | 0.623 ± 0.032 | 0.376 ± 0.056 | 0.383 ± 0.099 | 0.089 ± 0.010 | 0.042 ± 0.011 |
| UNet | 0.998 ± 0.002 | 0.935 ± 0.022 | 0.960 ± 0.016 | 0.868 ± 0.022 | 0.109 ± 0.025 | 0.165 ± 0.074 | 0.006 ± 0.002 | 0.004 ± 0.002 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.914 ± 0.064 | 0.818 ± 0.059 | 0.851 ± 0.060 | 0.829 ± 0.023 | 0.130 ± 0.030 | 0.188 ± 0.062 | - | - |
| B1 | - | - | - | 0.856 ± 0.026 | 0.077 ± 0.027 | 0.189 ± 0.054 | - | - |
| B2 | 0.972 ± 0.013 | 0.917 ± 0.030 | 0.939 ± 0.024 | 0.821 ± 0.029 | 0.035 ± 0.019 | 0.313 ± 0.065 | 0.039 ± 0.012 | 0.046 ± 0.017 |
| UNet | 0.981 ± 0.009 | 0.933 ± 0.021 | 0.954 ± 0.016 | 0.866 ± 0.022 | 0.105 ± 0.031 | 0.140 ± 0.049 | 0.028 ± 0.010 | 0.019 ± 0.016 |

Paired tests, U-Net vs the better training-free baseline (B0, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 8/8 scenes, mean difference +0.0767, Wilcoxon p = 0.00781
- scene level, planes: U-Net better in 8/8 scenes, mean difference +0.0732, Wilcoxon p = 0.00781
- scene level, objects: U-Net better in 8/8 scenes, mean difference +0.1150, Wilcoxon p = 0.00781
- view level (all masks, n = 720 views, not independent): median difference +0.0596, U-Net better in 99% of views, p = 6.88e-118

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.076 ms, 2.186 ms per depth slice, exact one-pass A(p,z_v) 2.358 ms, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

## RGB + Depth Anything V2 (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.789 ± 0.061 | 0.822 ± 0.063 | 0.794 ± 0.029 | 0.133 ± 0.031 | 0.315 ± 0.119 | - | - |
| B1 | - | - | - | 0.623 ± 0.028 | 0.394 ± 0.042 | 0.332 ± 0.083 | - | - |
| B2 | 0.934 ± 0.014 | 0.708 ± 0.047 | 0.724 ± 0.048 | 0.642 ± 0.026 | 0.315 ± 0.066 | 0.440 ± 0.116 | 0.088 ± 0.009 | 0.038 ± 0.008 |
| UNet | 0.995 ± 0.003 | 0.841 ± 0.061 | 0.874 ± 0.059 | 0.800 ± 0.030 | 0.149 ± 0.041 | 0.277 ± 0.130 | 0.017 ± 0.006 | 0.011 ± 0.005 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.795 ± 0.059 | 0.829 ± 0.060 | 0.799 ± 0.029 | 0.128 ± 0.030 | 0.317 ± 0.126 | - | - |
| B1 | - | - | - | 0.607 ± 0.033 | 0.420 ± 0.041 | 0.336 ± 0.088 | - | - |
| B2 | 0.935 ± 0.014 | 0.699 ± 0.052 | 0.715 ± 0.052 | 0.630 ± 0.029 | 0.339 ± 0.067 | 0.438 ± 0.125 | 0.088 ± 0.009 | 0.039 ± 0.008 |
| UNet | 0.996 ± 0.002 | 0.845 ± 0.063 | 0.878 ± 0.060 | 0.804 ± 0.031 | 0.144 ± 0.039 | 0.282 ± 0.139 | 0.017 ± 0.006 | 0.011 ± 0.005 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.791 ± 0.095 | 0.711 ± 0.060 | 0.740 ± 0.068 | 0.741 ± 0.029 | 0.186 ± 0.066 | 0.311 ± 0.097 | - | - |
| B1 | - | - | - | 0.765 ± 0.026 | 0.144 ± 0.060 | 0.310 ± 0.084 | - | - |
| B2 | 0.866 ± 0.077 | 0.787 ± 0.059 | 0.817 ± 0.062 | 0.740 ± 0.023 | 0.070 ± 0.041 | 0.473 ± 0.083 | 0.087 ± 0.028 | 0.088 ± 0.038 |
| UNet | 0.847 ± 0.094 | 0.798 ± 0.047 | 0.827 ± 0.051 | 0.752 ± 0.026 | 0.202 ± 0.087 | 0.261 ± 0.104 | 0.077 ± 0.026 | 0.049 ± 0.029 |

Paired tests, U-Net vs the better training-free baseline (B0, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 8/8 scenes, mean difference +0.0525, Wilcoxon p = 0.00781
- scene level, planes: U-Net better in 8/8 scenes, mean difference +0.0496, Wilcoxon p = 0.00781
- scene level, objects: U-Net better in 8/8 scenes, mean difference +0.0862, Wilcoxon p = 0.00781
- view level (all masks, n = 720 views, not independent): median difference +0.0370, U-Net better in 88% of views, p = 1.19e-89

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.326 ms, 2.268 ms per depth slice, exact one-pass A(p,z_v) 2.455 ms, U-Net 2.91 ms per 640x480 frame (473,569 parameters).

## RGB-only (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.923 ± 0.097 | 0.726 ± 0.088 | 0.753 ± 0.093 | 0.756 ± 0.029 | 0.160 ± 0.049 | 0.382 ± 0.145 | - | - |
| B1 | - | - | - | 0.622 ± 0.025 | 0.366 ± 0.073 | 0.394 ± 0.098 | - | - |
| B2 | 0.870 ± 0.107 | 0.665 ± 0.048 | 0.681 ± 0.049 | 0.606 ± 0.026 | 0.420 ± 0.075 | 0.326 ± 0.103 | 0.118 ± 0.049 | 0.073 ± 0.061 |
| UNet | 0.960 ± 0.057 | 0.789 ± 0.082 | 0.821 ± 0.085 | 0.766 ± 0.030 | 0.136 ± 0.043 | 0.388 ± 0.099 | 0.054 ± 0.042 | 0.055 ± 0.042 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.925 ± 0.096 | 0.736 ± 0.088 | 0.764 ± 0.093 | 0.763 ± 0.029 | 0.153 ± 0.044 | 0.382 ± 0.146 | - | - |
| B1 | - | - | - | 0.609 ± 0.031 | 0.387 ± 0.078 | 0.397 ± 0.103 | - | - |
| B2 | 0.871 ± 0.107 | 0.661 ± 0.047 | 0.677 ± 0.048 | 0.591 ± 0.033 | 0.441 ± 0.080 | 0.328 ± 0.108 | 0.118 ± 0.049 | 0.074 ± 0.061 |
| UNet | 0.961 ± 0.057 | 0.794 ± 0.084 | 0.826 ± 0.087 | 0.771 ± 0.030 | 0.130 ± 0.038 | 0.390 ± 0.099 | 0.054 ± 0.042 | 0.055 ± 0.042 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.642 ± 0.141 | 0.621 ± 0.074 | 0.634 ± 0.089 | 0.690 ± 0.023 | 0.212 ± 0.081 | 0.403 ± 0.146 | - | - |
| B1 | - | - | - | 0.728 ± 0.027 | 0.148 ± 0.054 | 0.401 ± 0.133 | - | - |
| B2 | 0.731 ± 0.140 | 0.698 ± 0.088 | 0.717 ± 0.098 | 0.723 ± 0.026 | 0.197 ± 0.064 | 0.344 ± 0.137 | 0.133 ± 0.056 | 0.135 ± 0.070 |
| UNet | 0.772 ± 0.133 | 0.726 ± 0.072 | 0.752 ± 0.084 | 0.710 ± 0.027 | 0.183 ± 0.069 | 0.395 ± 0.111 | 0.106 ± 0.036 | 0.053 ± 0.039 |

Paired tests, U-Net vs the better training-free baseline (B0, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 8/8 scenes, mean difference +0.0625, Wilcoxon p = 0.00781
- scene level, planes: U-Net better in 7/8 scenes, mean difference +0.0578, Wilcoxon p = 0.0156
- scene level, objects: U-Net better in 8/8 scenes, mean difference +0.1048, Wilcoxon p = 0.00781
- view level (all masks, n = 720 views, not independent): median difference +0.0329, U-Net better in 76% of views, p = 1.46e-55

Runtime on NVIDIA A100 80GB PCIe: stats pass 2.902 ms, 2.094 ms per depth slice, exact one-pass A(p,z_v) 2.281 ms, U-Net 2.91 ms per 640x480 frame (473,569 parameters).

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
