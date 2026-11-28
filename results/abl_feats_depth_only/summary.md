# Results: abl_feats_depth_only

## RGB-D (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.858 ± 0.043 | 0.893 ± 0.039 | 0.852 ± 0.022 | 0.109 ± 0.017 | 0.199 ± 0.066 | - | - |
| B1 | - | - | - | 0.870 ± 0.026 | 0.077 ± 0.021 | 0.196 ± 0.060 | - | - |
| B2 | 0.996 ± 0.003 | 0.931 ± 0.025 | 0.953 ± 0.018 | 0.872 ± 0.020 | 0.117 ± 0.024 | 0.142 ± 0.057 | 0.011 ± 0.004 | 0.009 ± 0.005 |
| UNet | 0.998 ± 0.002 | 0.927 ± 0.024 | 0.954 ± 0.017 | 0.869 ± 0.022 | 0.109 ± 0.019 | 0.158 ± 0.051 | 0.007 ± 0.003 | 0.006 ± 0.002 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.862 ± 0.042 | 0.896 ± 0.037 | 0.854 ± 0.023 | 0.107 ± 0.017 | 0.202 ± 0.069 | - | - |
| B1 | - | - | - | 0.871 ± 0.026 | 0.077 ± 0.021 | 0.198 ± 0.063 | - | - |
| B2 | 0.996 ± 0.003 | 0.932 ± 0.025 | 0.955 ± 0.018 | 0.873 ± 0.021 | 0.115 ± 0.023 | 0.144 ± 0.060 | 0.010 ± 0.004 | 0.009 ± 0.004 |
| UNet | 0.998 ± 0.002 | 0.928 ± 0.024 | 0.954 ± 0.017 | 0.870 ± 0.022 | 0.108 ± 0.018 | 0.162 ± 0.055 | 0.007 ± 0.003 | 0.006 ± 0.002 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.914 ± 0.064 | 0.818 ± 0.059 | 0.851 ± 0.060 | 0.829 ± 0.023 | 0.130 ± 0.030 | 0.188 ± 0.062 | - | - |
| B1 | - | - | - | 0.856 ± 0.026 | 0.077 ± 0.027 | 0.189 ± 0.054 | - | - |
| B2 | 0.972 ± 0.013 | 0.917 ± 0.030 | 0.939 ± 0.024 | 0.857 ± 0.019 | 0.131 ± 0.038 | 0.129 ± 0.051 | 0.039 ± 0.012 | 0.046 ± 0.017 |
| UNet | 0.974 ± 0.017 | 0.916 ± 0.030 | 0.941 ± 0.024 | 0.857 ± 0.022 | 0.119 ± 0.028 | 0.142 ± 0.043 | 0.031 ± 0.009 | 0.020 ± 0.009 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 4/8 scenes, mean difference -0.0040, Wilcoxon p = 0.641
- scene level, planes: U-Net better in 4/8 scenes, mean difference -0.0047, Wilcoxon p = 0.641
- scene level, objects: U-Net better in 2/8 scenes, mean difference -0.0007, Wilcoxon p = 0.641
- view level (all masks, n = 720 views, not independent): median difference +0.0015, U-Net better in 55% of views, p = 1.29e-01

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.076 ms, 2.186 ms per depth slice, exact one-pass A(p,z_v) 2.358 ms, U-Net 2.88 ms per 640x480 frame (472,129 parameters).

## RGB + Depth Anything V2 (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.789 ± 0.061 | 0.822 ± 0.063 | 0.794 ± 0.029 | 0.133 ± 0.031 | 0.315 ± 0.119 | - | - |
| B1 | - | - | - | 0.811 ± 0.029 | 0.106 ± 0.029 | 0.310 ± 0.110 | - | - |
| B2 | 0.991 ± 0.007 | 0.846 ± 0.054 | 0.876 ± 0.053 | 0.810 ± 0.027 | 0.144 ± 0.038 | 0.256 ± 0.110 | 0.019 ± 0.007 | 0.011 ± 0.006 |
| UNet | 0.995 ± 0.003 | 0.838 ± 0.059 | 0.872 ± 0.057 | 0.801 ± 0.030 | 0.151 ± 0.031 | 0.268 ± 0.108 | 0.017 ± 0.005 | 0.009 ± 0.005 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.795 ± 0.059 | 0.829 ± 0.060 | 0.799 ± 0.029 | 0.128 ± 0.030 | 0.317 ± 0.126 | - | - |
| B1 | - | - | - | 0.815 ± 0.030 | 0.102 ± 0.029 | 0.312 ± 0.117 | - | - |
| B2 | 0.992 ± 0.006 | 0.851 ± 0.053 | 0.881 ± 0.052 | 0.815 ± 0.028 | 0.138 ± 0.037 | 0.259 ± 0.118 | 0.018 ± 0.007 | 0.010 ± 0.005 |
| UNet | 0.996 ± 0.003 | 0.842 ± 0.060 | 0.875 ± 0.057 | 0.807 ± 0.029 | 0.145 ± 0.029 | 0.272 ± 0.114 | 0.016 ± 0.005 | 0.009 ± 0.005 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.791 ± 0.095 | 0.711 ± 0.060 | 0.740 ± 0.068 | 0.741 ± 0.029 | 0.186 ± 0.066 | 0.311 ± 0.097 | - | - |
| B1 | - | - | - | 0.765 ± 0.026 | 0.144 ± 0.060 | 0.310 ± 0.084 | - | - |
| B2 | 0.866 ± 0.077 | 0.787 ± 0.059 | 0.817 ± 0.062 | 0.759 ± 0.031 | 0.203 ± 0.078 | 0.245 ± 0.087 | 0.087 ± 0.028 | 0.088 ± 0.038 |
| UNet | 0.863 ± 0.073 | 0.796 ± 0.053 | 0.828 ± 0.056 | 0.747 ± 0.030 | 0.217 ± 0.073 | 0.252 ± 0.096 | 0.075 ± 0.020 | 0.039 ± 0.017 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 3/8 scenes, mean difference -0.0075, Wilcoxon p = 0.176
- scene level, planes: U-Net better in 4/8 scenes, mean difference -0.0094, Wilcoxon p = 0.312
- scene level, objects: U-Net better in 6/8 scenes, mean difference +0.0093, Wilcoxon p = 0.0781
- view level (all masks, n = 720 views, not independent): median difference -0.0021, U-Net better in 45% of views, p = 2.58e-03

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.326 ms, 2.268 ms per depth slice, exact one-pass A(p,z_v) 2.455 ms, U-Net 2.87 ms per 640x480 frame (472,129 parameters).

## RGB-only (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.923 ± 0.097 | 0.726 ± 0.088 | 0.753 ± 0.093 | 0.756 ± 0.029 | 0.160 ± 0.049 | 0.382 ± 0.145 | - | - |
| B1 | - | - | - | 0.785 ± 0.034 | 0.113 ± 0.029 | 0.374 ± 0.133 | - | - |
| B2 | 0.918 ± 0.108 | 0.785 ± 0.090 | 0.813 ± 0.091 | 0.782 ± 0.033 | 0.151 ± 0.041 | 0.323 ± 0.140 | 0.064 ± 0.068 | 0.061 ± 0.078 |
| UNet | 0.964 ± 0.042 | 0.789 ± 0.066 | 0.821 ± 0.068 | 0.763 ± 0.031 | 0.128 ± 0.042 | 0.409 ± 0.079 | 0.048 ± 0.029 | 0.042 ± 0.025 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.925 ± 0.096 | 0.736 ± 0.088 | 0.764 ± 0.093 | 0.763 ± 0.029 | 0.153 ± 0.044 | 0.382 ± 0.146 | - | - |
| B1 | - | - | - | 0.791 ± 0.035 | 0.108 ± 0.025 | 0.373 ± 0.134 | - | - |
| B2 | 0.919 ± 0.108 | 0.793 ± 0.091 | 0.822 ± 0.091 | 0.789 ± 0.033 | 0.145 ± 0.036 | 0.323 ± 0.140 | 0.063 ± 0.068 | 0.060 ± 0.078 |
| UNet | 0.965 ± 0.042 | 0.795 ± 0.067 | 0.826 ± 0.069 | 0.769 ± 0.032 | 0.121 ± 0.038 | 0.412 ± 0.078 | 0.047 ± 0.029 | 0.042 ± 0.025 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.642 ± 0.141 | 0.621 ± 0.074 | 0.634 ± 0.089 | 0.690 ± 0.023 | 0.212 ± 0.081 | 0.403 ± 0.146 | - | - |
| B1 | - | - | - | 0.728 ± 0.027 | 0.148 ± 0.054 | 0.401 ± 0.133 | - | - |
| B2 | 0.731 ± 0.140 | 0.698 ± 0.088 | 0.717 ± 0.098 | 0.721 ± 0.026 | 0.200 ± 0.074 | 0.344 ± 0.145 | 0.133 ± 0.056 | 0.135 ± 0.070 |
| UNet | 0.780 ± 0.095 | 0.729 ± 0.059 | 0.758 ± 0.067 | 0.707 ± 0.028 | 0.178 ± 0.071 | 0.408 ± 0.106 | 0.101 ± 0.022 | 0.050 ± 0.019 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 5/8 scenes, mean difference +0.0042, Wilcoxon p = 0.641
- scene level, planes: U-Net better in 4/8 scenes, mean difference +0.0014, Wilcoxon p = 0.945
- scene level, objects: U-Net better in 6/8 scenes, mean difference +0.0312, Wilcoxon p = 0.195
- view level (all masks, n = 720 views, not independent): median difference -0.0079, U-Net better in 40% of views, p = 1.30e-05

Runtime on NVIDIA A100 80GB PCIe: stats pass 2.902 ms, 2.094 ms per depth slice, exact one-pass A(p,z_v) 2.281 ms, U-Net 2.87 ms per 640x480 frame (472,129 parameters).

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
