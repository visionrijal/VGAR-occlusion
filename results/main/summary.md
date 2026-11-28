# Results: main

## RGB-D (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.858 ± 0.043 | 0.893 ± 0.039 | 0.853 ± 0.023 | 0.106 ± 0.018 | 0.201 ± 0.064 | - | - |
| B1 | - | - | - | 0.870 ± 0.026 | 0.077 ± 0.021 | 0.196 ± 0.060 | - | - |
| B2 | 0.996 ± 0.003 | 0.931 ± 0.025 | 0.953 ± 0.018 | 0.873 ± 0.021 | 0.114 ± 0.023 | 0.143 ± 0.051 | 0.011 ± 0.004 | 0.009 ± 0.005 |
| LR | 0.998 ± 0.002 | 0.930 ± 0.022 | 0.953 ± 0.016 | 0.871 ± 0.020 | 0.117 ± 0.026 | 0.144 ± 0.050 | 0.009 ± 0.003 | 0.015 ± 0.003 |
| MLP | 0.998 ± 0.002 | 0.932 ± 0.023 | 0.955 ± 0.016 | 0.873 ± 0.020 | 0.113 ± 0.017 | 0.145 ± 0.056 | 0.008 ± 0.003 | 0.010 ± 0.003 |
| UNet | 0.998 ± 0.002 | 0.942 ± 0.023 | 0.965 ± 0.016 | 0.881 ± 0.021 | 0.099 ± 0.024 | 0.143 ± 0.057 | 0.006 ± 0.003 | 0.005 ± 0.002 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.995 ± 0.003 | 0.862 ± 0.042 | 0.896 ± 0.037 | 0.855 ± 0.023 | 0.104 ± 0.019 | 0.203 ± 0.068 | - | - |
| B1 | - | - | - | 0.871 ± 0.026 | 0.077 ± 0.021 | 0.198 ± 0.063 | - | - |
| B2 | 0.996 ± 0.003 | 0.932 ± 0.025 | 0.955 ± 0.018 | 0.874 ± 0.022 | 0.112 ± 0.023 | 0.146 ± 0.054 | 0.010 ± 0.004 | 0.009 ± 0.004 |
| LR | 0.998 ± 0.002 | 0.931 ± 0.022 | 0.954 ± 0.016 | 0.872 ± 0.020 | 0.115 ± 0.026 | 0.146 ± 0.053 | 0.009 ± 0.003 | 0.015 ± 0.003 |
| MLP | 0.998 ± 0.002 | 0.932 ± 0.023 | 0.956 ± 0.017 | 0.873 ± 0.021 | 0.112 ± 0.017 | 0.149 ± 0.061 | 0.007 ± 0.003 | 0.010 ± 0.003 |
| UNet | 0.998 ± 0.002 | 0.943 ± 0.023 | 0.965 ± 0.016 | 0.881 ± 0.022 | 0.099 ± 0.025 | 0.148 ± 0.064 | 0.006 ± 0.003 | 0.005 ± 0.002 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.915 ± 0.066 | 0.818 ± 0.059 | 0.851 ± 0.060 | 0.831 ± 0.024 | 0.124 ± 0.028 | 0.190 ± 0.058 | - | - |
| B1 | - | - | - | 0.856 ± 0.026 | 0.077 ± 0.027 | 0.189 ± 0.054 | - | - |
| B2 | 0.973 ± 0.013 | 0.917 ± 0.030 | 0.939 ± 0.024 | 0.859 ± 0.020 | 0.127 ± 0.033 | 0.131 ± 0.046 | 0.039 ± 0.012 | 0.046 ± 0.017 |
| LR | 0.975 ± 0.012 | 0.919 ± 0.025 | 0.942 ± 0.020 | 0.858 ± 0.020 | 0.128 ± 0.035 | 0.130 ± 0.045 | 0.032 ± 0.009 | 0.027 ± 0.009 |
| MLP | 0.977 ± 0.012 | 0.931 ± 0.020 | 0.950 ± 0.016 | 0.866 ± 0.018 | 0.121 ± 0.028 | 0.123 ± 0.038 | 0.030 ± 0.007 | 0.022 ± 0.009 |
| UNet | 0.983 ± 0.009 | 0.942 ± 0.020 | 0.960 ± 0.015 | 0.880 ± 0.018 | 0.102 ± 0.024 | 0.117 ± 0.033 | 0.026 ± 0.008 | 0.019 ± 0.013 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 8/8 scenes, mean difference +0.0115, Wilcoxon p = 0.00781
- scene level, planes: U-Net better in 8/8 scenes, mean difference +0.0103, Wilcoxon p = 0.00781
- scene level, objects: U-Net better in 8/8 scenes, mean difference +0.0250, Wilcoxon p = 0.00781
- view level (all masks, n = 720 views, not independent): median difference +0.0126, U-Net better in 84% of views, p = 2.67e-75

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.076 ms, 2.186 ms per depth slice, exact one-pass A(p,z_v) 2.358 ms, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

## RGB + Depth Anything V2 (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.789 ± 0.061 | 0.822 ± 0.063 | 0.794 ± 0.029 | 0.136 ± 0.031 | 0.312 ± 0.123 | - | - |
| B1 | - | - | - | 0.811 ± 0.029 | 0.106 ± 0.029 | 0.310 ± 0.110 | - | - |
| B2 | 0.991 ± 0.007 | 0.846 ± 0.054 | 0.876 ± 0.053 | 0.810 ± 0.028 | 0.142 ± 0.041 | 0.259 ± 0.112 | 0.019 ± 0.007 | 0.011 ± 0.006 |
| LR | 0.994 ± 0.003 | 0.854 ± 0.053 | 0.883 ± 0.051 | 0.810 ± 0.027 | 0.142 ± 0.045 | 0.260 ± 0.113 | 0.019 ± 0.005 | 0.030 ± 0.007 |
| MLP | 0.995 ± 0.002 | 0.850 ± 0.052 | 0.879 ± 0.051 | 0.810 ± 0.027 | 0.140 ± 0.042 | 0.263 ± 0.108 | 0.019 ± 0.004 | 0.025 ± 0.007 |
| UNet | 0.996 ± 0.002 | 0.846 ± 0.061 | 0.879 ± 0.058 | 0.811 ± 0.029 | 0.133 ± 0.049 | 0.270 ± 0.126 | 0.016 ± 0.005 | 0.012 ± 0.004 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.993 ± 0.003 | 0.795 ± 0.059 | 0.829 ± 0.060 | 0.799 ± 0.029 | 0.130 ± 0.030 | 0.314 ± 0.129 | - | - |
| B1 | - | - | - | 0.815 ± 0.030 | 0.102 ± 0.029 | 0.312 ± 0.117 | - | - |
| B2 | 0.992 ± 0.006 | 0.851 ± 0.053 | 0.881 ± 0.052 | 0.815 ± 0.028 | 0.136 ± 0.040 | 0.262 ± 0.120 | 0.018 ± 0.007 | 0.010 ± 0.005 |
| LR | 0.994 ± 0.003 | 0.859 ± 0.052 | 0.888 ± 0.050 | 0.814 ± 0.027 | 0.136 ± 0.044 | 0.264 ± 0.121 | 0.018 ± 0.005 | 0.030 ± 0.007 |
| MLP | 0.995 ± 0.002 | 0.855 ± 0.052 | 0.884 ± 0.051 | 0.815 ± 0.028 | 0.133 ± 0.042 | 0.267 ± 0.116 | 0.018 ± 0.004 | 0.026 ± 0.007 |
| UNet | 0.996 ± 0.002 | 0.849 ± 0.062 | 0.882 ± 0.058 | 0.815 ± 0.029 | 0.128 ± 0.048 | 0.275 ± 0.136 | 0.016 ± 0.005 | 0.011 ± 0.004 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.790 ± 0.094 | 0.711 ± 0.060 | 0.740 ± 0.068 | 0.739 ± 0.026 | 0.191 ± 0.070 | 0.308 ± 0.105 | - | - |
| B1 | - | - | - | 0.765 ± 0.026 | 0.144 ± 0.060 | 0.310 ± 0.084 | - | - |
| B2 | 0.865 ± 0.075 | 0.787 ± 0.059 | 0.817 ± 0.062 | 0.759 ± 0.032 | 0.199 ± 0.083 | 0.249 ± 0.092 | 0.086 ± 0.027 | 0.088 ± 0.038 |
| LR | 0.872 ± 0.067 | 0.795 ± 0.053 | 0.825 ± 0.056 | 0.758 ± 0.033 | 0.203 ± 0.087 | 0.246 ± 0.094 | 0.073 ± 0.019 | 0.048 ± 0.020 |
| MLP | 0.871 ± 0.055 | 0.791 ± 0.051 | 0.821 ± 0.053 | 0.756 ± 0.033 | 0.205 ± 0.081 | 0.247 ± 0.089 | 0.072 ± 0.016 | 0.042 ± 0.018 |
| UNet | 0.846 ± 0.095 | 0.805 ± 0.058 | 0.834 ± 0.060 | 0.766 ± 0.027 | 0.185 ± 0.082 | 0.252 ± 0.102 | 0.075 ± 0.023 | 0.048 ± 0.024 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 4/8 scenes, mean difference -0.0001, Wilcoxon p = 0.799
- scene level, planes: U-Net better in 4/8 scenes, mean difference -0.0023, Wilcoxon p = 0.945
- scene level, objects: U-Net better in 6/8 scenes, mean difference +0.0183, Wilcoxon p = 0.109
- view level (all masks, n = 720 views, not independent): median difference +0.0047, U-Net better in 65% of views, p = 2.07e-15

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.326 ms, 2.268 ms per depth slice, exact one-pass A(p,z_v) 2.455 ms, U-Net 2.91 ms per 640x480 frame (473,569 parameters).

## RGB-only (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.923 ± 0.097 | 0.726 ± 0.088 | 0.753 ± 0.093 | 0.756 ± 0.029 | 0.164 ± 0.050 | 0.377 ± 0.145 | - | - |
| B1 | - | - | - | 0.785 ± 0.034 | 0.113 ± 0.029 | 0.374 ± 0.133 | - | - |
| B2 | 0.918 ± 0.108 | 0.785 ± 0.090 | 0.813 ± 0.091 | 0.783 ± 0.032 | 0.150 ± 0.040 | 0.325 ± 0.141 | 0.064 ± 0.067 | 0.061 ± 0.078 |
| LR | 0.894 ± 0.133 | 0.792 ± 0.078 | 0.822 ± 0.078 | 0.781 ± 0.030 | 0.156 ± 0.041 | 0.319 ± 0.137 | 0.069 ± 0.041 | 0.108 ± 0.032 |
| MLP | 0.954 ± 0.054 | 0.788 ± 0.080 | 0.816 ± 0.080 | 0.780 ± 0.034 | 0.149 ± 0.033 | 0.332 ± 0.117 | 0.053 ± 0.036 | 0.057 ± 0.030 |
| UNet | 0.959 ± 0.057 | 0.807 ± 0.087 | 0.838 ± 0.089 | 0.781 ± 0.032 | 0.128 ± 0.038 | 0.361 ± 0.120 | 0.054 ± 0.042 | 0.057 ± 0.040 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.925 ± 0.096 | 0.736 ± 0.088 | 0.764 ± 0.093 | 0.763 ± 0.029 | 0.157 ± 0.044 | 0.377 ± 0.147 | - | - |
| B1 | - | - | - | 0.791 ± 0.035 | 0.108 ± 0.025 | 0.373 ± 0.134 | - | - |
| B2 | 0.919 ± 0.107 | 0.793 ± 0.091 | 0.822 ± 0.091 | 0.789 ± 0.033 | 0.144 ± 0.035 | 0.325 ± 0.142 | 0.063 ± 0.068 | 0.060 ± 0.078 |
| LR | 0.896 ± 0.133 | 0.799 ± 0.079 | 0.829 ± 0.078 | 0.787 ± 0.031 | 0.150 ± 0.036 | 0.319 ± 0.137 | 0.069 ± 0.041 | 0.109 ± 0.032 |
| MLP | 0.955 ± 0.054 | 0.794 ± 0.081 | 0.822 ± 0.080 | 0.786 ± 0.034 | 0.141 ± 0.029 | 0.334 ± 0.119 | 0.052 ± 0.037 | 0.057 ± 0.030 |
| UNet | 0.960 ± 0.056 | 0.812 ± 0.089 | 0.843 ± 0.090 | 0.786 ± 0.033 | 0.124 ± 0.034 | 0.362 ± 0.120 | 0.054 ± 0.042 | 0.058 ± 0.040 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.642 ± 0.142 | 0.621 ± 0.074 | 0.634 ± 0.089 | 0.689 ± 0.023 | 0.219 ± 0.083 | 0.396 ± 0.147 | - | - |
| B1 | - | - | - | 0.728 ± 0.027 | 0.148 ± 0.054 | 0.401 ± 0.133 | - | - |
| B2 | 0.728 ± 0.141 | 0.698 ± 0.088 | 0.717 ± 0.098 | 0.722 ± 0.024 | 0.198 ± 0.073 | 0.346 ± 0.146 | 0.133 ± 0.055 | 0.135 ± 0.069 |
| LR | 0.766 ± 0.110 | 0.725 ± 0.071 | 0.747 ± 0.077 | 0.722 ± 0.024 | 0.198 ± 0.075 | 0.344 ± 0.144 | 0.104 ± 0.035 | 0.065 ± 0.049 |
| MLP | 0.761 ± 0.103 | 0.717 ± 0.074 | 0.737 ± 0.082 | 0.714 ± 0.035 | 0.217 ± 0.061 | 0.336 ± 0.109 | 0.103 ± 0.026 | 0.051 ± 0.034 |
| UNet | 0.782 ± 0.124 | 0.752 ± 0.078 | 0.776 ± 0.084 | 0.731 ± 0.026 | 0.161 ± 0.063 | 0.373 ± 0.122 | 0.102 ± 0.036 | 0.056 ± 0.039 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 6/8 scenes, mean difference +0.0221, Wilcoxon p = 0.0781
- scene level, planes: U-Net better in 6/8 scenes, mean difference +0.0185, Wilcoxon p = 0.0781
- scene level, objects: U-Net better in 8/8 scenes, mean difference +0.0538, Wilcoxon p = 0.00781
- view level (all masks, n = 720 views, not independent): median difference +0.0085, U-Net better in 60% of views, p = 1.12e-12

Runtime on NVIDIA A100 80GB PCIe: stats pass 2.902 ms, 2.094 ms per depth slice, exact one-pass A(p,z_v) 2.281 ms, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

## RGB-D, depth fine-tune (control) (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.996 ± 0.003 | 0.893 ± 0.042 | 0.922 ± 0.036 | 0.906 ± 0.024 | 0.080 ± 0.023 | 0.110 ± 0.055 | - | - |
| B1 | - | - | - | 0.911 ± 0.024 | 0.073 ± 0.024 | 0.106 ± 0.045 | - | - |
| B2 | 0.996 ± 0.003 | 0.953 ± 0.022 | 0.970 ± 0.015 | 0.911 ± 0.023 | 0.087 ± 0.027 | 0.091 ± 0.042 | 0.007 ± 0.003 | 0.007 ± 0.002 |
| LR | 0.998 ± 0.002 | 0.956 ± 0.020 | 0.973 ± 0.013 | 0.909 ± 0.022 | 0.089 ± 0.030 | 0.092 ± 0.040 | 0.005 ± 0.003 | 0.007 ± 0.001 |
| MLP | 0.998 ± 0.002 | 0.966 ± 0.015 | 0.979 ± 0.010 | 0.915 ± 0.025 | 0.076 ± 0.030 | 0.094 ± 0.053 | 0.004 ± 0.003 | 0.006 ± 0.002 |
| UNet | 0.999 ± 0.002 | 0.969 ± 0.014 | 0.981 ± 0.009 | 0.913 ± 0.025 | 0.079 ± 0.030 | 0.096 ± 0.061 | 0.004 ± 0.003 | 0.004 ± 0.002 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.996 ± 0.003 | 0.894 ± 0.042 | 0.923 ± 0.035 | 0.904 ± 0.026 | 0.081 ± 0.024 | 0.116 ± 0.063 | - | - |
| B1 | - | - | - | 0.910 ± 0.025 | 0.075 ± 0.024 | 0.112 ± 0.052 | - | - |
| B2 | 0.997 ± 0.003 | 0.953 ± 0.022 | 0.970 ± 0.015 | 0.909 ± 0.024 | 0.088 ± 0.027 | 0.097 ± 0.048 | 0.006 ± 0.003 | 0.007 ± 0.002 |
| LR | 0.998 ± 0.002 | 0.956 ± 0.020 | 0.972 ± 0.014 | 0.907 ± 0.023 | 0.090 ± 0.030 | 0.098 ± 0.047 | 0.005 ± 0.003 | 0.007 ± 0.001 |
| MLP | 0.999 ± 0.002 | 0.965 ± 0.016 | 0.978 ± 0.011 | 0.913 ± 0.027 | 0.078 ± 0.031 | 0.101 ± 0.063 | 0.004 ± 0.003 | 0.006 ± 0.002 |
| UNet | 0.999 ± 0.002 | 0.968 ± 0.015 | 0.981 ± 0.009 | 0.911 ± 0.026 | 0.081 ± 0.031 | 0.102 ± 0.069 | 0.004 ± 0.003 | 0.004 ± 0.002 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.960 ± 0.027 | 0.896 ± 0.045 | 0.918 ± 0.041 | 0.924 ± 0.020 | 0.064 ± 0.023 | 0.074 ± 0.031 | - | - |
| B1 | - | - | - | 0.928 ± 0.020 | 0.058 ± 0.023 | 0.072 ± 0.025 | - | - |
| B2 | 0.987 ± 0.012 | 0.959 ± 0.024 | 0.971 ± 0.019 | 0.928 ± 0.021 | 0.073 ± 0.026 | 0.057 ± 0.021 | 0.019 ± 0.007 | 0.026 ± 0.004 |
| LR | 0.991 ± 0.009 | 0.966 ± 0.018 | 0.977 ± 0.014 | 0.929 ± 0.021 | 0.073 ± 0.028 | 0.056 ± 0.020 | 0.015 ± 0.008 | 0.013 ± 0.003 |
| MLP | 0.992 ± 0.007 | 0.978 ± 0.009 | 0.985 ± 0.007 | 0.934 ± 0.020 | 0.062 ± 0.028 | 0.057 ± 0.022 | 0.014 ± 0.007 | 0.011 ± 0.007 |
| UNet | 0.993 ± 0.008 | 0.977 ± 0.015 | 0.984 ± 0.011 | 0.933 ± 0.021 | 0.060 ± 0.026 | 0.060 ± 0.031 | 0.014 ± 0.008 | 0.013 ± 0.012 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 8/8 scenes, mean difference +0.0155, Wilcoxon p = 0.00781
- scene level, planes: U-Net better in 8/8 scenes, mean difference +0.0147, Wilcoxon p = 0.00781
- scene level, objects: U-Net better in 8/8 scenes, mean difference +0.0181, Wilcoxon p = 0.00781
- view level (all masks, n = 720 views, not independent): median difference +0.0061, U-Net better in 91% of views, p = 1.92e-91

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.105 ms, 2.22 ms per depth slice, exact one-pass A(p,z_v) 2.422 ms, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

## RGB-D, occlusion fine-tune (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.996 ± 0.003 | 0.894 ± 0.043 | 0.922 ± 0.036 | 0.904 ± 0.025 | 0.080 ± 0.025 | 0.114 ± 0.055 | - | - |
| B1 | - | - | - | 0.912 ± 0.024 | 0.071 ± 0.026 | 0.107 ± 0.046 | - | - |
| B2 | 0.997 ± 0.003 | 0.957 ± 0.021 | 0.973 ± 0.014 | 0.912 ± 0.024 | 0.086 ± 0.030 | 0.089 ± 0.042 | 0.006 ± 0.003 | 0.005 ± 0.002 |
| LR | 0.999 ± 0.002 | 0.959 ± 0.019 | 0.975 ± 0.013 | 0.911 ± 0.024 | 0.088 ± 0.033 | 0.089 ± 0.041 | 0.005 ± 0.003 | 0.007 ± 0.001 |
| MLP | 0.999 ± 0.002 | 0.968 ± 0.015 | 0.980 ± 0.010 | 0.914 ± 0.025 | 0.076 ± 0.029 | 0.097 ± 0.053 | 0.004 ± 0.003 | 0.006 ± 0.002 |
| UNet | 0.999 ± 0.002 | 0.969 ± 0.015 | 0.982 ± 0.010 | 0.913 ± 0.025 | 0.080 ± 0.033 | 0.095 ± 0.063 | 0.004 ± 0.003 | 0.004 ± 0.002 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.997 ± 0.003 | 0.894 ± 0.043 | 0.923 ± 0.036 | 0.902 ± 0.026 | 0.082 ± 0.025 | 0.119 ± 0.063 | - | - |
| B1 | - | - | - | 0.910 ± 0.025 | 0.072 ± 0.026 | 0.113 ± 0.053 | - | - |
| B2 | 0.997 ± 0.003 | 0.957 ± 0.021 | 0.973 ± 0.014 | 0.910 ± 0.025 | 0.088 ± 0.030 | 0.094 ± 0.048 | 0.006 ± 0.003 | 0.005 ± 0.002 |
| LR | 0.999 ± 0.002 | 0.959 ± 0.020 | 0.974 ± 0.013 | 0.908 ± 0.025 | 0.090 ± 0.033 | 0.095 ± 0.047 | 0.005 ± 0.003 | 0.007 ± 0.001 |
| MLP | 0.999 ± 0.002 | 0.967 ± 0.016 | 0.980 ± 0.011 | 0.912 ± 0.027 | 0.077 ± 0.029 | 0.104 ± 0.062 | 0.004 ± 0.003 | 0.006 ± 0.002 |
| UNet | 0.999 ± 0.002 | 0.968 ± 0.016 | 0.981 ± 0.010 | 0.911 ± 0.026 | 0.082 ± 0.033 | 0.101 ± 0.072 | 0.004 ± 0.003 | 0.004 ± 0.002 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.962 ± 0.025 | 0.896 ± 0.044 | 0.918 ± 0.039 | 0.922 ± 0.021 | 0.061 ± 0.027 | 0.079 ± 0.031 | - | - |
| B1 | - | - | - | 0.929 ± 0.022 | 0.053 ± 0.026 | 0.074 ± 0.026 | - | - |
| B2 | 0.989 ± 0.010 | 0.965 ± 0.022 | 0.975 ± 0.017 | 0.931 ± 0.022 | 0.068 ± 0.029 | 0.056 ± 0.022 | 0.017 ± 0.007 | 0.022 ± 0.004 |
| LR | 0.992 ± 0.008 | 0.970 ± 0.016 | 0.980 ± 0.012 | 0.932 ± 0.022 | 0.069 ± 0.031 | 0.055 ± 0.021 | 0.014 ± 0.007 | 0.013 ± 0.003 |
| MLP | 0.993 ± 0.007 | 0.980 ± 0.010 | 0.986 ± 0.008 | 0.933 ± 0.022 | 0.063 ± 0.033 | 0.057 ± 0.025 | 0.014 ± 0.007 | 0.012 ± 0.006 |
| UNet | 0.994 ± 0.007 | 0.979 ± 0.013 | 0.986 ± 0.010 | 0.935 ± 0.022 | 0.058 ± 0.032 | 0.059 ± 0.030 | 0.012 ± 0.007 | 0.010 ± 0.008 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 8/8 scenes, mean difference +0.0116, Wilcoxon p = 0.00781
- scene level, planes: U-Net better in 8/8 scenes, mean difference +0.0108, Wilcoxon p = 0.00781
- scene level, objects: U-Net better in 8/8 scenes, mean difference +0.0149, Wilcoxon p = 0.00781
- view level (all masks, n = 720 views, not independent): median difference +0.0043, U-Net better in 86% of views, p = 2.84e-79

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.096 ms, 2.148 ms per depth slice, exact one-pass A(p,z_v) 2.353 ms, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

## Depth Anything, depth fine-tune (control) (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.985 ± 0.006 | 0.716 ± 0.070 | 0.745 ± 0.077 | 0.721 ± 0.028 | 0.178 ± 0.106 | 0.451 ± 0.189 | - | - |
| B1 | - | - | - | 0.747 ± 0.027 | 0.148 ± 0.080 | 0.423 ± 0.167 | - | - |
| B2 | 0.981 ± 0.009 | 0.793 ± 0.055 | 0.824 ± 0.057 | 0.743 ± 0.032 | 0.202 ± 0.102 | 0.343 ± 0.172 | 0.039 ± 0.019 | 0.031 ± 0.026 |
| LR | 0.987 ± 0.007 | 0.793 ± 0.067 | 0.824 ± 0.070 | 0.733 ± 0.037 | 0.229 ± 0.121 | 0.321 ± 0.177 | 0.042 ± 0.012 | 0.067 ± 0.014 |
| MLP | 0.987 ± 0.005 | 0.788 ± 0.063 | 0.819 ± 0.066 | 0.742 ± 0.032 | 0.214 ± 0.095 | 0.325 ± 0.151 | 0.040 ± 0.012 | 0.043 ± 0.014 |
| UNet | 0.990 ± 0.004 | 0.786 ± 0.080 | 0.817 ± 0.084 | 0.755 ± 0.033 | 0.185 ± 0.089 | 0.340 ± 0.155 | 0.032 ± 0.013 | 0.026 ± 0.013 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.986 ± 0.006 | 0.725 ± 0.069 | 0.755 ± 0.076 | 0.730 ± 0.026 | 0.171 ± 0.101 | 0.445 ± 0.188 | - | - |
| B1 | - | - | - | 0.756 ± 0.025 | 0.142 ± 0.075 | 0.419 ± 0.168 | - | - |
| B2 | 0.983 ± 0.009 | 0.801 ± 0.055 | 0.833 ± 0.056 | 0.752 ± 0.030 | 0.194 ± 0.098 | 0.340 ± 0.173 | 0.037 ± 0.018 | 0.029 ± 0.025 |
| LR | 0.988 ± 0.006 | 0.802 ± 0.066 | 0.833 ± 0.067 | 0.742 ± 0.035 | 0.222 ± 0.118 | 0.318 ± 0.178 | 0.041 ± 0.012 | 0.068 ± 0.014 |
| MLP | 0.988 ± 0.005 | 0.796 ± 0.063 | 0.827 ± 0.065 | 0.750 ± 0.031 | 0.204 ± 0.093 | 0.328 ± 0.157 | 0.039 ± 0.011 | 0.043 ± 0.013 |
| UNet | 0.991 ± 0.004 | 0.792 ± 0.082 | 0.823 ± 0.084 | 0.763 ± 0.031 | 0.176 ± 0.087 | 0.340 ± 0.160 | 0.031 ± 0.012 | 0.026 ± 0.013 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.646 ± 0.110 | 0.603 ± 0.050 | 0.617 ± 0.062 | 0.620 ± 0.076 | 0.254 ± 0.183 | 0.505 ± 0.206 | - | - |
| B1 | - | - | - | 0.659 ± 0.061 | 0.217 ± 0.157 | 0.465 ± 0.178 | - | - |
| B2 | 0.760 ± 0.100 | 0.692 ± 0.044 | 0.717 ± 0.052 | 0.648 ± 0.076 | 0.286 ± 0.172 | 0.371 ± 0.179 | 0.162 ± 0.062 | 0.168 ± 0.089 |
| LR | 0.757 ± 0.112 | 0.688 ± 0.056 | 0.712 ± 0.065 | 0.640 ± 0.085 | 0.305 ± 0.184 | 0.355 ± 0.184 | 0.125 ± 0.030 | 0.105 ± 0.045 |
| MLP | 0.751 ± 0.088 | 0.692 ± 0.046 | 0.714 ± 0.054 | 0.642 ± 0.076 | 0.331 ± 0.158 | 0.313 ± 0.143 | 0.123 ± 0.024 | 0.086 ± 0.035 |
| UNet | 0.719 ± 0.133 | 0.702 ± 0.063 | 0.722 ± 0.075 | 0.665 ± 0.064 | 0.273 ± 0.158 | 0.352 ± 0.163 | 0.123 ± 0.028 | 0.088 ± 0.035 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 4/8 scenes, mean difference -0.0064, Wilcoxon p = 1
- scene level, planes: U-Net better in 4/8 scenes, mean difference -0.0095, Wilcoxon p = 1
- scene level, objects: U-Net better in 5/8 scenes, mean difference +0.0099, Wilcoxon p = 0.383
- view level (all masks, n = 720 views, not independent): median difference +0.0044, U-Net better in 55% of views, p = 2.34e-03

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.277 ms, 2.244 ms per depth slice, exact one-pass A(p,z_v) 2.484 ms, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

## Depth Anything, occlusion fine-tune (8 test scenes: office_0, office_1, office_2, office_3, office_4, room_0, room_1, room_2)

**all** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.986 ± 0.005 | 0.715 ± 0.067 | 0.745 ± 0.075 | 0.718 ± 0.025 | 0.177 ± 0.105 | 0.462 ± 0.197 | - | - |
| B1 | - | - | - | 0.746 ± 0.026 | 0.142 ± 0.078 | 0.437 ± 0.177 | - | - |
| B2 | 0.985 ± 0.007 | 0.792 ± 0.055 | 0.826 ± 0.057 | 0.738 ± 0.033 | 0.217 ± 0.117 | 0.330 ± 0.182 | 0.037 ± 0.018 | 0.030 ± 0.025 |
| LR | 0.988 ± 0.005 | 0.792 ± 0.062 | 0.824 ± 0.064 | 0.731 ± 0.035 | 0.225 ± 0.126 | 0.332 ± 0.182 | 0.039 ± 0.012 | 0.063 ± 0.010 |
| MLP | 0.987 ± 0.004 | 0.790 ± 0.064 | 0.821 ± 0.067 | 0.743 ± 0.029 | 0.208 ± 0.097 | 0.332 ± 0.160 | 0.038 ± 0.012 | 0.042 ± 0.010 |
| UNet | 0.991 ± 0.004 | 0.790 ± 0.076 | 0.824 ± 0.078 | 0.762 ± 0.028 | 0.181 ± 0.082 | 0.326 ± 0.150 | 0.031 ± 0.012 | 0.025 ± 0.013 |

**planes** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.987 ± 0.005 | 0.723 ± 0.066 | 0.755 ± 0.073 | 0.727 ± 0.022 | 0.169 ± 0.101 | 0.458 ± 0.197 | - | - |
| B1 | - | - | - | 0.754 ± 0.024 | 0.136 ± 0.074 | 0.434 ± 0.179 | - | - |
| B2 | 0.986 ± 0.007 | 0.800 ± 0.054 | 0.834 ± 0.056 | 0.746 ± 0.031 | 0.209 ± 0.114 | 0.329 ± 0.184 | 0.035 ± 0.017 | 0.028 ± 0.024 |
| LR | 0.989 ± 0.005 | 0.800 ± 0.062 | 0.832 ± 0.064 | 0.739 ± 0.033 | 0.218 ± 0.124 | 0.331 ± 0.184 | 0.038 ± 0.012 | 0.063 ± 0.010 |
| MLP | 0.988 ± 0.004 | 0.797 ± 0.064 | 0.829 ± 0.066 | 0.752 ± 0.027 | 0.195 ± 0.096 | 0.337 ± 0.166 | 0.037 ± 0.011 | 0.042 ± 0.010 |
| UNet | 0.992 ± 0.004 | 0.795 ± 0.077 | 0.829 ± 0.078 | 0.770 ± 0.027 | 0.170 ± 0.083 | 0.330 ± 0.163 | 0.030 ± 0.012 | 0.024 ± 0.013 |

**objects** (AP mean ± std over scenes; F1 / missed / false occlusion in the 3 px band)

| Method | AP all | AP band 3 px | AP band 5 px | F1 band 3 | missed occ. band 3 | false occ. band 3 | Brier | ECE |
|---|---|---|---|---|---|---|---|---|
| B0 | 0.666 ± 0.113 | 0.607 ± 0.050 | 0.624 ± 0.063 | 0.618 ± 0.071 | 0.258 ± 0.183 | 0.505 ± 0.216 | - | - |
| B1 | - | - | - | 0.662 ± 0.053 | 0.211 ± 0.148 | 0.469 ± 0.185 | - | - |
| B2 | 0.793 ± 0.076 | 0.704 ± 0.046 | 0.731 ± 0.054 | 0.644 ± 0.080 | 0.307 ± 0.180 | 0.346 ± 0.190 | 0.156 ± 0.062 | 0.164 ± 0.095 |
| LR | 0.790 ± 0.081 | 0.699 ± 0.050 | 0.726 ± 0.057 | 0.641 ± 0.082 | 0.303 ± 0.186 | 0.358 ± 0.193 | 0.119 ± 0.028 | 0.104 ± 0.043 |
| MLP | 0.767 ± 0.075 | 0.698 ± 0.047 | 0.722 ± 0.055 | 0.645 ± 0.065 | 0.335 ± 0.149 | 0.301 ± 0.155 | 0.117 ± 0.022 | 0.087 ± 0.036 |
| UNet | 0.748 ± 0.123 | 0.717 ± 0.066 | 0.741 ± 0.077 | 0.674 ± 0.057 | 0.285 ± 0.137 | 0.317 ± 0.143 | 0.115 ± 0.029 | 0.086 ± 0.034 |

Paired tests, U-Net vs the better training-free baseline (B2, band-3 AP). The scene-level test is the primary one; views within a scene are not independent.

- scene level, all: U-Net better in 5/8 scenes, mean difference -0.0021, Wilcoxon p = 0.945
- scene level, planes: U-Net better in 5/8 scenes, mean difference -0.0043, Wilcoxon p = 0.945
- scene level, objects: U-Net better in 5/8 scenes, mean difference +0.0130, Wilcoxon p = 0.312
- view level (all masks, n = 720 views, not independent): median difference +0.0065, U-Net better in 59% of views, p = 2.26e-06

Runtime on NVIDIA A100 80GB PCIe: stats pass 3.477 ms, 2.31 ms per depth slice, exact one-pass A(p,z_v) 2.579 ms, U-Net 2.90 ms per 640x480 frame (473,569 parameters).

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
