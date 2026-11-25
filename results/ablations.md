# Ablations

3 px boundary-band AP, mean over the 8 leave-one-scene-out test scenes. Each cell: soft opacity B2 (training-free, recomputed with that run's slices) / U-Net, and in brackets the number of scenes where that U-Net beats the main run's B2. Defaults: all 10 inputs, 32-depth global grid, 16 slices per object.

## planes

| Variant | RGB-D | Depth Anything | RGB-only |
|---|---|---|---|
| U-Net, all inputs (main) | 0.932 / 0.945 [8/8] | 0.851 / 0.849 [6/8] | 0.793 / 0.809 [5/8] |
| no RGB input | 0.932 / 0.946 [8/8] | 0.851 / 0.858 [7/8] | 0.793 / 0.811 [5/8] |
| depth statistics only (no opacity) | 0.932 / 0.926 [3/8] | 0.851 / 0.843 [3/8] | 0.793 / 0.795 [3/8] |
| opacity only (no depth statistics) | 0.932 / 0.936 [7/8] | 0.851 / 0.842 [3/8] | 0.793 / 0.823 [6/8] |
| objects: global 32-depth grid | 0.932 / 0.941 [7/8] | 0.851 / 0.847 [5/8] | 0.793 / 0.802 [6/8] |
| objects: 4 slices per object | 0.932 / 0.944 [7/8] | 0.851 / 0.851 [6/8] | 0.793 / 0.804 [5/8] |
| objects: 8 slices per object | 0.932 / 0.944 [7/8] | 0.851 / 0.845 [6/8] | 0.793 / 0.817 [6/8] |
| planes: 4-depth global grid | 0.723 / 0.935 [6/8] | 0.699 / 0.843 [3/8] | 0.661 / 0.784 [5/8] |
| planes: 8-depth global grid | 0.904 / 0.940 [6/8] | 0.826 / 0.845 [3/8] | 0.771 / 0.795 [5/8] |
| planes: 16-depth global grid | 0.904 / 0.940 [6/8] | 0.841 / 0.846 [4/8] | 0.784 / 0.796 [4/8] |

## objects

| Variant | RGB-D | Depth Anything | RGB-only |
|---|---|---|---|
| U-Net, all inputs (main) | 0.916 / 0.939 [8/8] | 0.787 / 0.808 [8/8] | 0.698 / 0.764 [7/8] |
| no RGB input | 0.916 / 0.941 [8/8] | 0.787 / 0.831 [8/8] | 0.698 / 0.771 [8/8] |
| depth statistics only (no opacity) | 0.916 / 0.915 [3/8] | 0.787 / 0.783 [2/8] | 0.698 / 0.725 [6/8] |
| opacity only (no depth statistics) | 0.916 / 0.928 [7/8] | 0.787 / 0.797 [5/8] | 0.698 / 0.790 [8/8] |
| objects: global 32-depth grid | 0.821 / 0.920 [4/8] | 0.740 / 0.782 [4/8] | 0.660 / 0.714 [6/8] |
| objects: 4 slices per object | 0.881 / 0.926 [6/8] | 0.768 / 0.792 [4/8] | 0.682 / 0.730 [5/8] |
| objects: 8 slices per object | 0.907 / 0.932 [8/8] | 0.783 / 0.786 [4/8] | 0.694 / 0.746 [7/8] |
| planes: 4-depth global grid | 0.916 / 0.931 [8/8] | 0.787 / 0.788 [4/8] | 0.698 / 0.712 [5/8] |
| planes: 8-depth global grid | 0.916 / 0.938 [8/8] | 0.787 / 0.793 [6/8] | 0.698 / 0.731 [6/8] |
| planes: 16-depth global grid | 0.916 / 0.935 [8/8] | 0.787 / 0.803 [6/8] | 0.698 / 0.753 [6/8] |
