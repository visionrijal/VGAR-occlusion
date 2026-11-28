# Results: abl_K_8

## RGB-D (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.858 ± 0.043 | 0.893 ± 0.039 | 0.852 ± 0.022 | 0.109 ± 0.017 | 0.199 ± 0.066 | - | - |
| B1 | - | - | - | 0.817 ± 0.029 | 0.187 ± 0.034 | 0.175 ± 0.054 | - | - |
| B2 | 0.993 ± 0.003 | 0.905 ± 0.027 | 0.930 ± 0.023 | 0.817 ± 0.028 | 0.198 ± 0.031 | 0.160 ± 0.055 | 0.024 ± 0.006 | 0.020 ± 0.003 |
| UNet | 0.998 ± 0.002 | 0.941 ± 0.020 | 0.964 ± 0.014 | 0.875 ± 0.022 | 0.110 ± 0.025 | 0.143 ± 0.066 | 0.007 ± 0.003 | 0.006 ± 0.003 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.862 ± 0.042 | 0.896 ± 0.037 | 0.854 ± 0.023 | 0.107 ± 0.017 | 0.202 ± 0.069 | - | - |
| B1 | - | - | - | 0.811 ± 0.034 | 0.200 ± 0.042 | 0.174 ± 0.055 | - | - |
| B2 | 0.993 ± 0.003 | 0.904 ± 0.029 | 0.929 ± 0.025 | 0.811 ± 0.033 | 0.211 ± 0.039 | 0.159 ± 0.056 | 0.024 ± 0.006 | 0.020 ± 0.003 |
| UNet | 0.998 ± 0.002 | 0.941 ± 0.021 | 0.964 ± 0.014 | 0.875 ± 0.023 | 0.111 ± 0.025 | 0.147 ± 0.072 | 0.006 ± 0.003 | 0.006 ± 0.002 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.914 ± 0.064 | 0.818 ± 0.059 | 0.851 ± 0.060 | 0.829 ± 0.023 | 0.130 ± 0.030 | 0.188 ± 0.062 | - | - |
| B1 | - | - | - | 0.856 ± 0.026 | 0.077 ± 0.027 | 0.189 ± 0.054 | - | - |
| B2 | 0.972 ± 0.013 | 0.917 ± 0.030 | 0.939 ± 0.024 | 0.858 ± 0.024 | 0.091 ± 0.032 | 0.171 ± 0.053 | 0.039 ± 0.012 | 0.046 ± 0.017 |
| UNet | 0.982 ± 0.010 | 0.939 ± 0.021 | 0.958 ± 0.016 | 0.874 ± 0.020 | 0.104 ± 0.028 | 0.125 ± 0.044 | 0.027 ± 0.008 | 0.019 ± 0.016 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 8/8 scenes, mean difference +0.0357, Wilcoxon p = 0.00781
- scene level, planes: U-Net better in 8/8 scenes, mean difference +0.0374, Wilcoxon p = 0.00781
- scene level, objects: U-Net better in 8/8 scenes, mean difference +0.0223, Wilcoxon p = 0.00781
- view level (all masks, n = 720 views, not independent): median difference +0.0327, U-Net better in 95% of views, p = 8.98e-114

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.076 ms, 2.186 ms per depth slice, exact one-pass A(p,z_v) 2.358 ms, U-Net 2.91 ms per 640x480 frame (473,569 parameters).

## RGB + Depth Anything V2 (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.789 ± 0.061 | 0.822 ± 0.063 | 0.794 ± 0.029 | 0.133 ± 0.031 | 0.315 ± 0.119 | - | - |
| B1 | - | - | - | 0.768 ± 0.034 | 0.200 ± 0.008 | 0.282 ± 0.092 | - | - |
| B2 | 0.989 ± 0.005 | 0.822 ± 0.059 | 0.853 ± 0.060 | 0.768 ± 0.034 | 0.194 ± 0.009 | 0.293 ± 0.099 | 0.030 ± 0.008 | 0.022 ± 0.004 |
| UNet | 0.995 ± 0.002 | 0.841 ± 0.060 | 0.875 ± 0.058 | 0.804 ± 0.031 | 0.145 ± 0.043 | 0.270 ± 0.121 | 0.017 ± 0.006 | 0.012 ± 0.005 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.795 ± 0.059 | 0.829 ± 0.060 | 0.799 ± 0.029 | 0.128 ± 0.030 | 0.317 ± 0.126 | - | - |
| B1 | - | - | - | 0.768 ± 0.038 | 0.207 ± 0.013 | 0.279 ± 0.095 | - | - |
| B2 | 0.990 ± 0.005 | 0.826 ± 0.060 | 0.856 ± 0.060 | 0.768 ± 0.037 | 0.201 ± 0.009 | 0.290 ± 0.101 | 0.029 ± 0.008 | 0.021 ± 0.004 |
| UNet | 0.996 ± 0.002 | 0.846 ± 0.060 | 0.880 ± 0.057 | 0.808 ± 0.032 | 0.142 ± 0.040 | 0.271 ± 0.127 | 0.017 ± 0.006 | 0.011 ± 0.005 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.791 ± 0.095 | 0.711 ± 0.060 | 0.740 ± 0.068 | 0.741 ± 0.029 | 0.186 ± 0.066 | 0.311 ± 0.097 | - | - |
| B1 | - | - | - | 0.765 ± 0.026 | 0.144 ± 0.060 | 0.310 ± 0.084 | - | - |
| B2 | 0.866 ± 0.077 | 0.787 ± 0.059 | 0.817 ± 0.062 | 0.763 ± 0.026 | 0.138 ± 0.066 | 0.322 ± 0.092 | 0.087 ± 0.028 | 0.088 ± 0.038 |
| UNet | 0.857 ± 0.089 | 0.788 ± 0.063 | 0.820 ± 0.065 | 0.762 ± 0.030 | 0.176 ± 0.090 | 0.273 ± 0.111 | 0.077 ± 0.029 | 0.055 ± 0.036 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 8/8 scenes, mean difference +0.0187, Wilcoxon p = 0.00781
- scene level, planes: U-Net better in 8/8 scenes, mean difference +0.0199, Wilcoxon p = 0.00781
- scene level, objects: U-Net better in 3/8 scenes, mean difference +0.0013, Wilcoxon p = 0.742
- view level (all masks, n = 720 views, not independent): median difference +0.0214, U-Net better in 83% of views, p = 2.56e-69

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.326 ms, 2.268 ms per depth slice, exact one-pass A(p,z_v) 2.455 ms, U-Net 2.91 ms per 640x480 frame (473,569 parameters).

## RGB-only (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.923 ± 0.097 | 0.726 ± 0.088 | 0.753 ± 0.093 | 0.756 ± 0.029 | 0.160 ± 0.049 | 0.382 ± 0.145 | - | - |
| B1 | - | - | - | 0.745 ± 0.032 | 0.199 ± 0.063 | 0.347 ± 0.134 | - | - |
| B2 | 0.918 ± 0.106 | 0.764 ± 0.083 | 0.793 ± 0.084 | 0.744 ± 0.033 | 0.205 ± 0.070 | 0.341 ± 0.140 | 0.072 ± 0.064 | 0.070 ± 0.074 |
| UNet | 0.959 ± 0.060 | 0.791 ± 0.085 | 0.823 ± 0.089 | 0.771 ± 0.031 | 0.139 ± 0.038 | 0.372 ± 0.106 | 0.055 ± 0.044 | 0.055 ± 0.045 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.925 ± 0.096 | 0.736 ± 0.088 | 0.764 ± 0.093 | 0.763 ± 0.029 | 0.153 ± 0.044 | 0.382 ± 0.146 | - | - |
| B1 | - | - | - | 0.746 ± 0.034 | 0.205 ± 0.066 | 0.343 ± 0.135 | - | - |
| B2 | 0.919 ± 0.106 | 0.771 ± 0.083 | 0.800 ± 0.084 | 0.745 ± 0.035 | 0.210 ± 0.073 | 0.336 ± 0.141 | 0.071 ± 0.064 | 0.070 ± 0.073 |
| UNet | 0.960 ± 0.059 | 0.795 ± 0.087 | 0.827 ± 0.090 | 0.775 ± 0.031 | 0.137 ± 0.036 | 0.370 ± 0.107 | 0.054 ± 0.044 | 0.056 ± 0.045 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.642 ± 0.141 | 0.621 ± 0.074 | 0.634 ± 0.089 | 0.690 ± 0.023 | 0.212 ± 0.081 | 0.403 ± 0.146 | - | - |
| B1 | - | - | - | 0.728 ± 0.027 | 0.148 ± 0.054 | 0.401 ± 0.133 | - | - |
| B2 | 0.731 ± 0.140 | 0.698 ± 0.088 | 0.717 ± 0.098 | 0.727 ± 0.026 | 0.155 ± 0.063 | 0.394 ± 0.142 | 0.133 ± 0.056 | 0.135 ± 0.070 |
| UNet | 0.774 ± 0.135 | 0.746 ± 0.079 | 0.768 ± 0.089 | 0.726 ± 0.028 | 0.155 ± 0.049 | 0.394 ± 0.103 | 0.104 ± 0.039 | 0.055 ± 0.040 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 6/8 scenes, mean difference +0.0267, Wilcoxon p = 0.0781
- scene level, planes: U-Net better in 5/8 scenes, mean difference +0.0242, Wilcoxon p = 0.109
- scene level, objects: U-Net better in 7/8 scenes, mean difference +0.0474, Wilcoxon p = 0.0156
- view level (all masks, n = 720 views, not independent): median difference +0.0168, U-Net better in 66% of views, p = 1.00e-22

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
