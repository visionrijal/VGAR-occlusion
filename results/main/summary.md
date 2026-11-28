# Results: main

## RGB-D (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.858 ± 0.043 | 0.893 ± 0.039 | 0.853 ± 0.023 | 0.106 ± 0.018 | 0.201 ± 0.064 | - | - |
| B1 | - | - | - | 0.870 ± 0.026 | 0.077 ± 0.021 | 0.196 ± 0.060 | - | - |
| B2 | 0.996 ± 0.003 | 0.931 ± 0.025 | 0.953 ± 0.018 | 0.873 ± 0.021 | 0.114 ± 0.022 | 0.143 ± 0.051 | 0.011 ± 0.004 | 0.009 ± 0.005 |
| LR | 0.998 ± 0.002 | 0.930 ± 0.022 | 0.953 ± 0.016 | 0.871 ± 0.020 | 0.117 ± 0.026 | 0.143 ± 0.050 | 0.009 ± 0.003 | 0.015 ± 0.003 |
| MLP | 0.998 ± 0.002 | 0.932 ± 0.022 | 0.956 ± 0.016 | 0.873 ± 0.020 | 0.114 ± 0.016 | 0.143 ± 0.054 | 0.008 ± 0.003 | 0.010 ± 0.003 |
| UNet | 0.998 ± 0.002 | 0.944 ± 0.021 | 0.966 ± 0.014 | 0.880 ± 0.023 | 0.101 ± 0.030 | 0.142 ± 0.063 | 0.006 ± 0.003 | 0.005 ± 0.002 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.862 ± 0.042 | 0.896 ± 0.037 | 0.855 ± 0.023 | 0.104 ± 0.019 | 0.203 ± 0.068 | - | - |
| B1 | - | - | - | 0.871 ± 0.026 | 0.077 ± 0.021 | 0.198 ± 0.063 | - | - |
| B2 | 0.996 ± 0.003 | 0.932 ± 0.025 | 0.955 ± 0.018 | 0.874 ± 0.022 | 0.112 ± 0.023 | 0.146 ± 0.054 | 0.010 ± 0.004 | 0.009 ± 0.004 |
| LR | 0.998 ± 0.002 | 0.931 ± 0.022 | 0.954 ± 0.016 | 0.872 ± 0.020 | 0.115 ± 0.027 | 0.147 ± 0.053 | 0.009 ± 0.003 | 0.015 ± 0.003 |
| MLP | 0.998 ± 0.002 | 0.932 ± 0.023 | 0.956 ± 0.017 | 0.873 ± 0.021 | 0.112 ± 0.016 | 0.148 ± 0.060 | 0.007 ± 0.003 | 0.010 ± 0.003 |
| UNet | 0.998 ± 0.002 | 0.945 ± 0.021 | 0.967 ± 0.014 | 0.880 ± 0.024 | 0.101 ± 0.030 | 0.146 ± 0.069 | 0.006 ± 0.003 | 0.005 ± 0.002 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.915 ± 0.066 | 0.818 ± 0.059 | 0.851 ± 0.060 | 0.831 ± 0.024 | 0.124 ± 0.028 | 0.190 ± 0.058 | - | - |
| B1 | - | - | - | 0.857 ± 0.027 | 0.077 ± 0.027 | 0.189 ± 0.055 | - | - |
| B2 | 0.973 ± 0.013 | 0.916 ± 0.031 | 0.939 ± 0.024 | 0.858 ± 0.020 | 0.131 ± 0.033 | 0.127 ± 0.046 | 0.039 ± 0.012 | 0.047 ± 0.017 |
| LR | 0.976 ± 0.012 | 0.919 ± 0.025 | 0.942 ± 0.020 | 0.858 ± 0.020 | 0.132 ± 0.036 | 0.127 ± 0.045 | 0.032 ± 0.009 | 0.027 ± 0.009 |
| MLP | 0.977 ± 0.012 | 0.932 ± 0.021 | 0.952 ± 0.016 | 0.867 ± 0.017 | 0.123 ± 0.028 | 0.119 ± 0.039 | 0.030 ± 0.007 | 0.023 ± 0.010 |
| UNet | 0.983 ± 0.008 | 0.939 ± 0.021 | 0.958 ± 0.016 | 0.877 ± 0.021 | 0.104 ± 0.031 | 0.119 ± 0.038 | 0.026 ± 0.007 | 0.019 ± 0.013 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 8/8 scenes, mean difference +0.0137, Wilcoxon p = 0.00781
- scene level, planes: U-Net better in 8/8 scenes, mean difference +0.0127, Wilcoxon p = 0.00781
- scene level, objects: U-Net better in 8/8 scenes, mean difference +0.0229, Wilcoxon p = 0.00781
- view level (all masks, n = 720 views, not independent): median difference +0.0122, U-Net better in 85% of views, p = 1.46e-77

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.076 ms, 2.186 ms per depth slice, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

## RGB + Depth Anything V2 (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.789 ± 0.061 | 0.822 ± 0.063 | 0.794 ± 0.029 | 0.136 ± 0.031 | 0.312 ± 0.123 | - | - |
| B1 | - | - | - | 0.811 ± 0.029 | 0.106 ± 0.029 | 0.310 ± 0.110 | - | - |
| B2 | 0.991 ± 0.007 | 0.846 ± 0.054 | 0.876 ± 0.053 | 0.810 ± 0.028 | 0.142 ± 0.041 | 0.259 ± 0.112 | 0.019 ± 0.007 | 0.011 ± 0.006 |
| LR | 0.994 ± 0.003 | 0.854 ± 0.053 | 0.883 ± 0.051 | 0.810 ± 0.027 | 0.142 ± 0.045 | 0.260 ± 0.113 | 0.019 ± 0.005 | 0.030 ± 0.007 |
| MLP | 0.995 ± 0.003 | 0.849 ± 0.053 | 0.879 ± 0.053 | 0.810 ± 0.028 | 0.140 ± 0.040 | 0.261 ± 0.108 | 0.019 ± 0.005 | 0.023 ± 0.007 |
| UNet | 0.996 ± 0.002 | 0.846 ± 0.067 | 0.879 ± 0.064 | 0.810 ± 0.030 | 0.135 ± 0.048 | 0.270 ± 0.133 | 0.017 ± 0.006 | 0.013 ± 0.006 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.795 ± 0.059 | 0.829 ± 0.060 | 0.799 ± 0.029 | 0.130 ± 0.030 | 0.314 ± 0.129 | - | - |
| B1 | - | - | - | 0.815 ± 0.030 | 0.102 ± 0.029 | 0.312 ± 0.117 | - | - |
| B2 | 0.992 ± 0.006 | 0.851 ± 0.053 | 0.881 ± 0.052 | 0.815 ± 0.028 | 0.136 ± 0.040 | 0.262 ± 0.120 | 0.018 ± 0.007 | 0.010 ± 0.005 |
| LR | 0.994 ± 0.003 | 0.859 ± 0.052 | 0.888 ± 0.050 | 0.814 ± 0.027 | 0.136 ± 0.044 | 0.264 ± 0.121 | 0.018 ± 0.005 | 0.030 ± 0.007 |
| MLP | 0.995 ± 0.002 | 0.854 ± 0.053 | 0.883 ± 0.052 | 0.816 ± 0.028 | 0.133 ± 0.039 | 0.265 ± 0.116 | 0.018 ± 0.005 | 0.023 ± 0.007 |
| UNet | 0.996 ± 0.002 | 0.849 ± 0.068 | 0.882 ± 0.065 | 0.814 ± 0.030 | 0.130 ± 0.048 | 0.275 ± 0.144 | 0.016 ± 0.005 | 0.012 ± 0.006 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.790 ± 0.094 | 0.711 ± 0.060 | 0.740 ± 0.068 | 0.739 ± 0.026 | 0.191 ± 0.070 | 0.308 ± 0.105 | - | - |
| B1 | - | - | - | 0.765 ± 0.027 | 0.144 ± 0.061 | 0.309 ± 0.085 | - | - |
| B2 | 0.866 ± 0.076 | 0.787 ± 0.060 | 0.818 ± 0.063 | 0.759 ± 0.033 | 0.202 ± 0.084 | 0.246 ± 0.093 | 0.086 ± 0.027 | 0.089 ± 0.037 |
| LR | 0.873 ± 0.067 | 0.796 ± 0.054 | 0.826 ± 0.056 | 0.757 ± 0.034 | 0.205 ± 0.089 | 0.244 ± 0.095 | 0.073 ± 0.019 | 0.048 ± 0.020 |
| MLP | 0.865 ± 0.061 | 0.794 ± 0.052 | 0.824 ± 0.055 | 0.755 ± 0.034 | 0.209 ± 0.085 | 0.243 ± 0.092 | 0.073 ± 0.017 | 0.039 ± 0.013 |
| UNet | 0.852 ± 0.100 | 0.808 ± 0.058 | 0.838 ± 0.061 | 0.765 ± 0.028 | 0.190 ± 0.084 | 0.248 ± 0.105 | 0.075 ± 0.027 | 0.051 ± 0.034 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 6/8 scenes, mean difference +0.0005, Wilcoxon p = 0.383
- scene level, planes: U-Net better in 6/8 scenes, mean difference -0.0017, Wilcoxon p = 0.547
- scene level, objects: U-Net better in 8/8 scenes, mean difference +0.0212, Wilcoxon p = 0.00781
- view level (all masks, n = 720 views, not independent): median difference +0.0066, U-Net better in 67% of views, p = 2.48e-18

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.326 ms, 2.268 ms per depth slice, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

## RGB-only (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.923 ± 0.097 | 0.726 ± 0.088 | 0.753 ± 0.093 | 0.756 ± 0.029 | 0.164 ± 0.050 | 0.377 ± 0.145 | - | - |
| B1 | - | - | - | 0.785 ± 0.034 | 0.113 ± 0.029 | 0.374 ± 0.133 | - | - |
| B2 | 0.918 ± 0.108 | 0.785 ± 0.090 | 0.813 ± 0.091 | 0.782 ± 0.032 | 0.151 ± 0.040 | 0.323 ± 0.143 | 0.064 ± 0.067 | 0.061 ± 0.078 |
| LR | 0.894 ± 0.133 | 0.792 ± 0.078 | 0.822 ± 0.077 | 0.781 ± 0.030 | 0.156 ± 0.041 | 0.319 ± 0.137 | 0.069 ± 0.042 | 0.107 ± 0.032 |
| MLP | 0.956 ± 0.056 | 0.789 ± 0.080 | 0.816 ± 0.080 | 0.778 ± 0.036 | 0.150 ± 0.021 | 0.334 ± 0.102 | 0.054 ± 0.036 | 0.058 ± 0.027 |
| UNet | 0.961 ± 0.056 | 0.805 ± 0.085 | 0.835 ± 0.088 | 0.783 ± 0.031 | 0.133 ± 0.033 | 0.348 ± 0.112 | 0.054 ± 0.043 | 0.060 ± 0.044 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.925 ± 0.096 | 0.736 ± 0.088 | 0.764 ± 0.093 | 0.763 ± 0.029 | 0.157 ± 0.044 | 0.377 ± 0.147 | - | - |
| B1 | - | - | - | 0.791 ± 0.035 | 0.108 ± 0.025 | 0.373 ± 0.134 | - | - |
| B2 | 0.919 ± 0.107 | 0.793 ± 0.091 | 0.822 ± 0.091 | 0.789 ± 0.033 | 0.145 ± 0.036 | 0.323 ± 0.143 | 0.063 ± 0.068 | 0.060 ± 0.078 |
| LR | 0.895 ± 0.133 | 0.799 ± 0.079 | 0.828 ± 0.077 | 0.787 ± 0.031 | 0.150 ± 0.036 | 0.319 ± 0.137 | 0.069 ± 0.042 | 0.108 ± 0.032 |
| MLP | 0.957 ± 0.056 | 0.794 ± 0.081 | 0.822 ± 0.081 | 0.785 ± 0.036 | 0.142 ± 0.017 | 0.336 ± 0.105 | 0.053 ± 0.036 | 0.058 ± 0.027 |
| UNet | 0.962 ± 0.055 | 0.809 ± 0.087 | 0.839 ± 0.090 | 0.788 ± 0.032 | 0.128 ± 0.028 | 0.348 ± 0.113 | 0.054 ± 0.043 | 0.060 ± 0.044 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.642 ± 0.142 | 0.621 ± 0.074 | 0.634 ± 0.089 | 0.689 ± 0.023 | 0.219 ± 0.083 | 0.396 ± 0.147 | - | - |
| B1 | - | - | - | 0.729 ± 0.027 | 0.147 ± 0.055 | 0.402 ± 0.134 | - | - |
| B2 | 0.729 ± 0.142 | 0.698 ± 0.089 | 0.718 ± 0.099 | 0.721 ± 0.024 | 0.202 ± 0.074 | 0.342 ± 0.148 | 0.133 ± 0.055 | 0.135 ± 0.069 |
| LR | 0.769 ± 0.110 | 0.726 ± 0.071 | 0.749 ± 0.076 | 0.722 ± 0.025 | 0.200 ± 0.077 | 0.342 ± 0.145 | 0.104 ± 0.035 | 0.065 ± 0.049 |
| MLP | 0.772 ± 0.100 | 0.718 ± 0.074 | 0.740 ± 0.082 | 0.715 ± 0.039 | 0.216 ± 0.056 | 0.333 ± 0.092 | 0.101 ± 0.024 | 0.053 ± 0.024 |
| UNet | 0.786 ± 0.120 | 0.764 ± 0.060 | 0.789 ± 0.067 | 0.730 ± 0.024 | 0.166 ± 0.065 | 0.370 ± 0.116 | 0.101 ± 0.035 | 0.055 ± 0.034 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 5/8 scenes, mean difference +0.0198, Wilcoxon p = 0.25
- scene level, planes: U-Net better in 5/8 scenes, mean difference +0.0160, Wilcoxon p = 0.25
- scene level, objects: U-Net better in 7/8 scenes, mean difference +0.0655, Wilcoxon p = 0.0156
- view level (all masks, n = 720 views, not independent): median difference +0.0064, U-Net better in 57% of views, p = 5.47e-09

Runtime on NVIDIA A100 80GB PCIe: stats pass 2.902 ms, 2.094 ms per depth slice, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

## Maps (Sequence_2 test views, mean over scenes)

| Condition | PSNR (dB) | median depth error (cm) | depth within 5 cm | Gaussians |
|---|---|---|---|---|
| RGB-D | 29.59 | 2.20 | 81.4% | 342,914 |
| RGB + Depth Anything V2 | 27.70 | 4.35 | 60.4% | 361,215 |
| RGB-only | 25.41 | 15.94 | 43.0% | 153,719 |

Per scene: office_0/rgbd 1.3 cm; office_1/rgbd 1.7 cm; office_2/rgbd 2.5 cm; office_3/rgbd 3.0 cm; office_4/rgbd 3.8 cm; room_0/rgbd 2.2 cm; room_1/rgbd 1.6 cm; room_2/rgbd 1.6 cm; office_0/mono 4.1 cm; office_1/mono 5.3 cm; office_2/mono 3.8 cm; office_3/mono 4.6 cm; office_4/mono 5.4 cm; room_0/mono 4.1 cm; room_1/mono 5.0 cm; room_2/mono 2.6 cm; office_0/rgbonly 4.6 cm; office_1/rgbonly 4.6 cm; office_2/rgbonly 9.1 cm; office_3/rgbonly 25.4 cm; office_4/rgbonly 62.4 cm; room_0/rgbonly 8.2 cm; room_1/rgbonly 6.9 cm; room_2/rgbonly 6.4 cm
