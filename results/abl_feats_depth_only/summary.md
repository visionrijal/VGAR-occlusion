# Results: abl_feats_depth_only

## RGB-D (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.858 ± 0.043 | 0.893 ± 0.039 | 0.852 ± 0.022 | 0.109 ± 0.017 | 0.199 ± 0.066 | - | - |
| B1 | - | - | - | 0.870 ± 0.026 | 0.077 ± 0.021 | 0.196 ± 0.060 | - | - |
| B2 | 0.996 ± 0.003 | 0.931 ± 0.025 | 0.953 ± 0.018 | 0.873 ± 0.022 | 0.115 ± 0.023 | 0.143 ± 0.055 | 0.011 ± 0.004 | 0.009 ± 0.005 |
| UNet | 0.998 ± 0.002 | 0.926 ± 0.025 | 0.953 ± 0.019 | 0.867 ± 0.022 | 0.111 ± 0.019 | 0.161 ± 0.055 | 0.007 ± 0.003 | 0.006 ± 0.002 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.862 ± 0.042 | 0.896 ± 0.037 | 0.854 ± 0.023 | 0.107 ± 0.017 | 0.202 ± 0.069 | - | - |
| B1 | - | - | - | 0.871 ± 0.026 | 0.077 ± 0.021 | 0.198 ± 0.063 | - | - |
| B2 | 0.996 ± 0.003 | 0.932 ± 0.025 | 0.955 ± 0.018 | 0.874 ± 0.023 | 0.113 ± 0.023 | 0.146 ± 0.058 | 0.010 ± 0.004 | 0.009 ± 0.004 |
| UNet | 0.998 ± 0.002 | 0.926 ± 0.025 | 0.954 ± 0.019 | 0.868 ± 0.023 | 0.109 ± 0.019 | 0.165 ± 0.060 | 0.007 ± 0.003 | 0.006 ± 0.002 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.914 ± 0.064 | 0.818 ± 0.059 | 0.851 ± 0.060 | 0.829 ± 0.023 | 0.130 ± 0.030 | 0.188 ± 0.062 | - | - |
| B1 | - | - | - | 0.857 ± 0.027 | 0.077 ± 0.027 | 0.189 ± 0.055 | - | - |
| B2 | 0.973 ± 0.013 | 0.916 ± 0.031 | 0.939 ± 0.024 | 0.858 ± 0.022 | 0.131 ± 0.034 | 0.127 ± 0.049 | 0.039 ± 0.012 | 0.047 ± 0.016 |
| UNet | 0.974 ± 0.017 | 0.915 ± 0.029 | 0.939 ± 0.024 | 0.856 ± 0.022 | 0.123 ± 0.026 | 0.142 ± 0.045 | 0.030 ± 0.008 | 0.018 ± 0.006 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 3/8 scenes, mean difference -0.0051, Wilcoxon p = 0.312
- scene level, planes: U-Net better in 3/8 scenes, mean difference -0.0059, Wilcoxon p = 0.25
- scene level, objects: U-Net better in 3/8 scenes, mean difference -0.0015, Wilcoxon p = 0.461
- view level (all masks, n = 720 views, not independent): median difference +0.0001, U-Net better in 50% of views, p = 2.04e-01

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.076 ms, 2.186 ms per depth slice, U-Net 2.87 ms per 640x480 frame (472,129 parameters).

## RGB + Depth Anything V2 (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.789 ± 0.061 | 0.822 ± 0.063 | 0.794 ± 0.029 | 0.133 ± 0.031 | 0.315 ± 0.119 | - | - |
| B1 | - | - | - | 0.811 ± 0.029 | 0.106 ± 0.029 | 0.310 ± 0.110 | - | - |
| B2 | 0.991 ± 0.007 | 0.846 ± 0.054 | 0.876 ± 0.053 | 0.811 ± 0.027 | 0.144 ± 0.038 | 0.256 ± 0.110 | 0.019 ± 0.007 | 0.011 ± 0.006 |
| UNet | 0.995 ± 0.002 | 0.838 ± 0.063 | 0.872 ± 0.060 | 0.803 ± 0.029 | 0.148 ± 0.035 | 0.270 ± 0.109 | 0.017 ± 0.005 | 0.010 ± 0.005 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.795 ± 0.059 | 0.829 ± 0.060 | 0.799 ± 0.029 | 0.128 ± 0.030 | 0.317 ± 0.126 | - | - |
| B1 | - | - | - | 0.815 ± 0.030 | 0.102 ± 0.029 | 0.312 ± 0.117 | - | - |
| B2 | 0.992 ± 0.006 | 0.851 ± 0.053 | 0.881 ± 0.052 | 0.815 ± 0.028 | 0.138 ± 0.037 | 0.259 ± 0.118 | 0.018 ± 0.007 | 0.010 ± 0.005 |
| UNet | 0.996 ± 0.002 | 0.843 ± 0.063 | 0.877 ± 0.060 | 0.808 ± 0.028 | 0.143 ± 0.034 | 0.271 ± 0.114 | 0.016 ± 0.005 | 0.010 ± 0.005 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.791 ± 0.095 | 0.711 ± 0.060 | 0.740 ± 0.068 | 0.741 ± 0.029 | 0.186 ± 0.066 | 0.311 ± 0.097 | - | - |
| B1 | - | - | - | 0.765 ± 0.027 | 0.144 ± 0.061 | 0.309 ± 0.085 | - | - |
| B2 | 0.867 ± 0.077 | 0.787 ± 0.060 | 0.818 ± 0.063 | 0.759 ± 0.032 | 0.205 ± 0.079 | 0.242 ± 0.089 | 0.086 ± 0.028 | 0.089 ± 0.038 |
| UNet | 0.866 ± 0.066 | 0.783 ± 0.063 | 0.816 ± 0.065 | 0.748 ± 0.029 | 0.205 ± 0.070 | 0.268 ± 0.098 | 0.075 ± 0.021 | 0.041 ± 0.024 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 2/8 scenes, mean difference -0.0076, Wilcoxon p = 0.195
- scene level, planes: U-Net better in 3/8 scenes, mean difference -0.0083, Wilcoxon p = 0.195
- scene level, objects: U-Net better in 2/8 scenes, mean difference -0.0046, Wilcoxon p = 0.547
- view level (all masks, n = 720 views, not independent): median difference -0.0014, U-Net better in 46% of views, p = 9.35e-03

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.326 ms, 2.268 ms per depth slice, U-Net 2.88 ms per 640x480 frame (472,129 parameters).

## RGB-only (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.923 ± 0.097 | 0.726 ± 0.088 | 0.753 ± 0.093 | 0.756 ± 0.029 | 0.160 ± 0.049 | 0.382 ± 0.145 | - | - |
| B1 | - | - | - | 0.785 ± 0.034 | 0.113 ± 0.029 | 0.374 ± 0.133 | - | - |
| B2 | 0.918 ± 0.108 | 0.785 ± 0.090 | 0.813 ± 0.091 | 0.782 ± 0.033 | 0.153 ± 0.043 | 0.321 ± 0.141 | 0.064 ± 0.068 | 0.061 ± 0.078 |
| UNet | 0.960 ± 0.050 | 0.789 ± 0.073 | 0.820 ± 0.075 | 0.765 ± 0.031 | 0.114 ± 0.036 | 0.426 ± 0.080 | 0.049 ± 0.032 | 0.044 ± 0.027 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.925 ± 0.096 | 0.736 ± 0.088 | 0.764 ± 0.093 | 0.763 ± 0.029 | 0.153 ± 0.044 | 0.382 ± 0.146 | - | - |
| B1 | - | - | - | 0.791 ± 0.035 | 0.108 ± 0.025 | 0.373 ± 0.134 | - | - |
| B2 | 0.919 ± 0.108 | 0.793 ± 0.091 | 0.822 ± 0.091 | 0.788 ± 0.033 | 0.147 ± 0.038 | 0.321 ± 0.142 | 0.063 ± 0.068 | 0.060 ± 0.078 |
| UNet | 0.961 ± 0.049 | 0.795 ± 0.073 | 0.825 ± 0.074 | 0.770 ± 0.031 | 0.110 ± 0.033 | 0.426 ± 0.081 | 0.048 ± 0.032 | 0.044 ± 0.027 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.642 ± 0.141 | 0.621 ± 0.074 | 0.634 ± 0.089 | 0.690 ± 0.023 | 0.212 ± 0.081 | 0.403 ± 0.146 | - | - |
| B1 | - | - | - | 0.729 ± 0.027 | 0.147 ± 0.055 | 0.402 ± 0.134 | - | - |
| B2 | 0.732 ± 0.140 | 0.698 ± 0.089 | 0.718 ± 0.099 | 0.720 ± 0.026 | 0.205 ± 0.078 | 0.340 ± 0.147 | 0.132 ± 0.056 | 0.135 ± 0.069 |
| UNet | 0.774 ± 0.108 | 0.725 ± 0.073 | 0.753 ± 0.084 | 0.710 ± 0.026 | 0.147 ± 0.055 | 0.447 ± 0.096 | 0.104 ± 0.028 | 0.054 ± 0.027 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 4/8 scenes, mean difference +0.0042, Wilcoxon p = 0.945
- scene level, planes: U-Net better in 3/8 scenes, mean difference +0.0017, Wilcoxon p = 0.945
- scene level, objects: U-Net better in 6/8 scenes, mean difference +0.0266, Wilcoxon p = 0.25
- view level (all masks, n = 720 views, not independent): median difference -0.0088, U-Net better in 37% of views, p = 1.26e-08

Runtime on NVIDIA A100 80GB PCIe: stats pass 2.902 ms, 2.094 ms per depth slice, U-Net 2.87 ms per 640x480 frame (472,129 parameters).

## Maps (Sequence_2 test views, mean over scenes)

| Condition | PSNR (dB) | median depth error (cm) | depth within 5 cm | Gaussians |
|---|---|---|---|---|
| RGB-D | 29.59 | 2.20 | 81.4% | 342,914 |
| RGB + Depth Anything V2 | 27.70 | 4.35 | 60.4% | 361,215 |
| RGB-only | 25.41 | 15.94 | 43.0% | 153,719 |

Per scene: office_0/rgbd 1.3 cm; office_1/rgbd 1.7 cm; office_2/rgbd 2.5 cm; office_3/rgbd 3.0 cm; office_4/rgbd 3.8 cm; room_0/rgbd 2.2 cm; room_1/rgbd 1.6 cm; room_2/rgbd 1.6 cm; office_0/mono 4.1 cm; office_1/mono 5.3 cm; office_2/mono 3.8 cm; office_3/mono 4.6 cm; office_4/mono 5.4 cm; room_0/mono 4.1 cm; room_1/mono 5.0 cm; room_2/mono 2.6 cm; office_0/rgbonly 4.6 cm; office_1/rgbonly 4.6 cm; office_2/rgbonly 9.1 cm; office_3/rgbonly 25.4 cm; office_4/rgbonly 62.4 cm; room_0/rgbonly 8.2 cm; room_1/rgbonly 6.9 cm; room_2/rgbonly 6.4 cm
