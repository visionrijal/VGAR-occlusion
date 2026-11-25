# Results: abl_K_16

## RGB-D (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.858 ± 0.043 | 0.893 ± 0.039 | 0.852 ± 0.022 | 0.109 ± 0.017 | 0.199 ± 0.066 | - | - |
| B1 | - | - | - | 0.832 ± 0.022 | 0.089 ± 0.016 | 0.276 ± 0.057 | - | - |
| B2 | 0.995 ± 0.003 | 0.906 ± 0.026 | 0.931 ± 0.021 | 0.838 ± 0.019 | 0.129 ± 0.018 | 0.206 ± 0.056 | 0.016 ± 0.004 | 0.015 ± 0.003 |
| UNet | 0.998 ± 0.002 | 0.939 ± 0.021 | 0.963 ± 0.014 | 0.872 ± 0.021 | 0.114 ± 0.023 | 0.146 ± 0.068 | 0.007 ± 0.003 | 0.005 ± 0.002 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.862 ± 0.042 | 0.896 ± 0.037 | 0.854 ± 0.023 | 0.107 ± 0.017 | 0.202 ± 0.069 | - | - |
| B1 | - | - | - | 0.829 ± 0.022 | 0.091 ± 0.015 | 0.289 ± 0.061 | - | - |
| B2 | 0.995 ± 0.003 | 0.904 ± 0.027 | 0.930 ± 0.021 | 0.835 ± 0.020 | 0.132 ± 0.018 | 0.214 ± 0.059 | 0.016 ± 0.003 | 0.015 ± 0.003 |
| UNet | 0.998 ± 0.002 | 0.940 ± 0.021 | 0.963 ± 0.015 | 0.872 ± 0.022 | 0.114 ± 0.022 | 0.150 ± 0.073 | 0.006 ± 0.003 | 0.005 ± 0.002 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.914 ± 0.064 | 0.818 ± 0.059 | 0.851 ± 0.060 | 0.829 ± 0.023 | 0.130 ± 0.030 | 0.188 ± 0.062 | - | - |
| B1 | - | - | - | 0.857 ± 0.027 | 0.077 ± 0.027 | 0.189 ± 0.055 | - | - |
| B2 | 0.973 ± 0.013 | 0.916 ± 0.031 | 0.939 ± 0.024 | 0.860 ± 0.024 | 0.107 ± 0.031 | 0.149 ± 0.049 | 0.039 ± 0.012 | 0.047 ± 0.016 |
| UNet | 0.982 ± 0.008 | 0.935 ± 0.021 | 0.956 ± 0.016 | 0.869 ± 0.020 | 0.114 ± 0.029 | 0.125 ± 0.047 | 0.028 ± 0.010 | 0.020 ± 0.017 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 8/8 scenes, mean difference +0.0336, Wilcoxon p = 0.00781
- scene level, planes: U-Net better in 8/8 scenes, mean difference +0.0353, Wilcoxon p = 0.00781
- scene level, objects: U-Net better in 8/8 scenes, mean difference +0.0187, Wilcoxon p = 0.00781
- view level (all masks, n = 720 views, not independent): median difference +0.0353, U-Net better in 93% of views, p = 8.67e-106

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.076 ms, 2.186 ms per depth slice, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

## RGB + Depth Anything V2 (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.789 ± 0.061 | 0.822 ± 0.063 | 0.794 ± 0.029 | 0.133 ± 0.031 | 0.315 ± 0.119 | - | - |
| B1 | - | - | - | 0.793 ± 0.027 | 0.110 ± 0.019 | 0.352 ± 0.097 | - | - |
| B2 | 0.991 ± 0.005 | 0.835 ± 0.053 | 0.865 ± 0.052 | 0.794 ± 0.025 | 0.149 ± 0.022 | 0.291 ± 0.100 | 0.022 ± 0.007 | 0.015 ± 0.003 |
| UNet | 0.996 ± 0.002 | 0.842 ± 0.062 | 0.875 ± 0.060 | 0.803 ± 0.028 | 0.147 ± 0.039 | 0.271 ± 0.118 | 0.017 ± 0.006 | 0.012 ± 0.005 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.795 ± 0.059 | 0.829 ± 0.060 | 0.799 ± 0.029 | 0.128 ± 0.030 | 0.317 ± 0.126 | - | - |
| B1 | - | - | - | 0.795 ± 0.027 | 0.107 ± 0.018 | 0.359 ± 0.104 | - | - |
| B2 | 0.992 ± 0.005 | 0.841 ± 0.052 | 0.870 ± 0.051 | 0.797 ± 0.026 | 0.146 ± 0.020 | 0.296 ± 0.107 | 0.022 ± 0.007 | 0.015 ± 0.002 |
| UNet | 0.996 ± 0.002 | 0.846 ± 0.062 | 0.878 ± 0.060 | 0.807 ± 0.029 | 0.142 ± 0.038 | 0.276 ± 0.125 | 0.016 ± 0.005 | 0.012 ± 0.005 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.791 ± 0.095 | 0.711 ± 0.060 | 0.740 ± 0.068 | 0.741 ± 0.029 | 0.186 ± 0.066 | 0.311 ± 0.097 | - | - |
| B1 | - | - | - | 0.765 ± 0.027 | 0.144 ± 0.061 | 0.309 ± 0.085 | - | - |
| B2 | 0.867 ± 0.077 | 0.787 ± 0.060 | 0.818 ± 0.063 | 0.763 ± 0.029 | 0.186 ± 0.069 | 0.259 ± 0.084 | 0.086 ± 0.028 | 0.089 ± 0.038 |
| UNet | 0.844 ± 0.104 | 0.803 ± 0.055 | 0.832 ± 0.058 | 0.760 ± 0.029 | 0.199 ± 0.078 | 0.249 ± 0.096 | 0.077 ± 0.025 | 0.048 ± 0.031 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 6/8 scenes, mean difference +0.0069, Wilcoxon p = 0.312
- scene level, planes: U-Net better in 6/8 scenes, mean difference +0.0052, Wilcoxon p = 0.383
- scene level, objects: U-Net better in 6/8 scenes, mean difference +0.0157, Wilcoxon p = 0.0391
- view level (all masks, n = 720 views, not independent): median difference +0.0125, U-Net better in 71% of views, p = 6.44e-30

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.326 ms, 2.268 ms per depth slice, U-Net 2.91 ms per 640x480 frame (473,569 parameters).

## RGB-only (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.923 ± 0.097 | 0.726 ± 0.088 | 0.753 ± 0.093 | 0.756 ± 0.029 | 0.160 ± 0.049 | 0.382 ± 0.145 | - | - |
| B1 | - | - | - | 0.770 ± 0.030 | 0.122 ± 0.036 | 0.404 ± 0.127 | - | - |
| B2 | 0.915 ± 0.112 | 0.775 ± 0.088 | 0.802 ± 0.090 | 0.766 ± 0.029 | 0.159 ± 0.050 | 0.354 ± 0.136 | 0.066 ± 0.066 | 0.064 ± 0.076 |
| UNet | 0.960 ± 0.055 | 0.793 ± 0.079 | 0.823 ± 0.082 | 0.771 ± 0.034 | 0.138 ± 0.049 | 0.369 ± 0.110 | 0.058 ± 0.042 | 0.063 ± 0.046 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.925 ± 0.096 | 0.736 ± 0.088 | 0.764 ± 0.093 | 0.763 ± 0.029 | 0.153 ± 0.044 | 0.382 ± 0.146 | - | - |
| B1 | - | - | - | 0.774 ± 0.030 | 0.118 ± 0.033 | 0.407 ± 0.127 | - | - |
| B2 | 0.916 ± 0.112 | 0.784 ± 0.089 | 0.811 ± 0.090 | 0.771 ± 0.029 | 0.155 ± 0.046 | 0.356 ± 0.136 | 0.065 ± 0.066 | 0.064 ± 0.076 |
| UNet | 0.960 ± 0.055 | 0.796 ± 0.081 | 0.826 ± 0.084 | 0.776 ± 0.035 | 0.135 ± 0.048 | 0.371 ± 0.112 | 0.057 ± 0.042 | 0.063 ± 0.046 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.642 ± 0.141 | 0.621 ± 0.074 | 0.634 ± 0.089 | 0.690 ± 0.023 | 0.212 ± 0.081 | 0.403 ± 0.146 | - | - |
| B1 | - | - | - | 0.729 ± 0.027 | 0.147 ± 0.055 | 0.402 ± 0.134 | - | - |
| B2 | 0.732 ± 0.140 | 0.698 ± 0.089 | 0.718 ± 0.099 | 0.725 ± 0.026 | 0.183 ± 0.069 | 0.360 ± 0.142 | 0.132 ± 0.056 | 0.135 ± 0.069 |
| UNet | 0.776 ± 0.111 | 0.753 ± 0.053 | 0.778 ± 0.058 | 0.729 ± 0.025 | 0.167 ± 0.056 | 0.370 ± 0.099 | 0.101 ± 0.031 | 0.052 ± 0.029 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 6/8 scenes, mean difference +0.0178, Wilcoxon p = 0.25
- scene level, planes: U-Net better in 6/8 scenes, mean difference +0.0126, Wilcoxon p = 0.25
- scene level, objects: U-Net better in 6/8 scenes, mean difference +0.0549, Wilcoxon p = 0.0547
- view level (all masks, n = 720 views, not independent): median difference +0.0071, U-Net better in 59% of views, p = 4.29e-09

Runtime on NVIDIA A100 80GB PCIe: stats pass 2.902 ms, 2.094 ms per depth slice, U-Net 2.91 ms per 640x480 frame (473,569 parameters).

## Maps (Sequence_2 test views, mean over scenes)

| Condition | PSNR (dB) | median depth error (cm) | depth within 5 cm | Gaussians |
|---|---|---|---|---|
| RGB-D | 29.59 | 2.20 | 81.4% | 342,914 |
| RGB + Depth Anything V2 | 27.70 | 4.35 | 60.4% | 361,215 |
| RGB-only | 25.41 | 15.94 | 43.0% | 153,719 |

Per scene: office_0/rgbd 1.3 cm; office_1/rgbd 1.7 cm; office_2/rgbd 2.5 cm; office_3/rgbd 3.0 cm; office_4/rgbd 3.8 cm; room_0/rgbd 2.2 cm; room_1/rgbd 1.6 cm; room_2/rgbd 1.6 cm; office_0/mono 4.1 cm; office_1/mono 5.3 cm; office_2/mono 3.8 cm; office_3/mono 4.6 cm; office_4/mono 5.4 cm; room_0/mono 4.1 cm; room_1/mono 5.0 cm; room_2/mono 2.6 cm; office_0/rgbonly 4.6 cm; office_1/rgbonly 4.6 cm; office_2/rgbonly 9.1 cm; office_3/rgbonly 25.4 cm; office_4/rgbonly 62.4 cm; room_0/rgbonly 8.2 cm; room_1/rgbonly 6.9 cm; room_2/rgbonly 6.4 cm
