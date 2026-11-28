# Ablations

3 px boundary-band AP, mean over the 8 leave-one-scene-out test scenes. Each cell: soft opacity B2 (training-free, recomputed with that run's slices) / U-Net, and in brackets the number of scenes where that U-Net beats the main run's B2. Defaults: all 10 inputs, 32-depth global grid, 16 slices per object.

## planes

| Variant | RGB-D | Depth Anything | RGB-only |
|---|---|---|---|
| U-Net, all inputs (main) | 0.932 / 0.943 [8/8] | 0.851 / 0.849 [4/8] | 0.793 / 0.812 [6/8] |
| no RGB input | 0.932 / 0.943 [7/8] | 0.851 / 0.852 [5/8] | 0.793 / 0.814 [6/8] |
| depth statistics only (no opacity) | 0.932 / 0.928 [4/8] | 0.851 / 0.842 [4/8] | 0.793 / 0.795 [4/8] |
| opacity only (no depth statistics) | 0.932 / 0.936 [6/8] | 0.851 / 0.850 [3/8] | 0.793 / 0.816 [6/8] |
| objects: global 32-depth grid | 0.932 / 0.941 [7/8] | 0.851 / 0.847 [5/8] | 0.793 / 0.802 [6/8] |
| objects: 4 slices per object | 0.932 / 0.944 [7/8] | 0.851 / 0.851 [6/8] | 0.793 / 0.804 [5/8] |
| objects: 8 slices per object | 0.932 / 0.944 [7/8] | 0.851 / 0.845 [6/8] | 0.793 / 0.817 [6/8] |
| planes: 4-depth global grid | 0.723 / 0.935 [5/8] | 0.699 / 0.845 [5/8] | 0.661 / 0.794 [5/8] |
| planes: 8-depth global grid | 0.904 / 0.941 [7/8] | 0.826 / 0.846 [4/8] | 0.771 / 0.795 [4/8] |
| planes: 16-depth global grid | 0.904 / 0.937 [6/8] | 0.841 / 0.850 [4/8] | 0.784 / 0.803 [5/8] |

## objects

| Variant | RGB-D | Depth Anything | RGB-only |
|---|---|---|---|
| U-Net, all inputs (main) | 0.917 / 0.942 [8/8] | 0.787 / 0.805 [6/8] | 0.698 / 0.752 [8/8] |
| no RGB input | 0.917 / 0.937 [8/8] | 0.787 / 0.833 [8/8] | 0.698 / 0.795 [8/8] |
| depth statistics only (no opacity) | 0.917 / 0.916 [2/8] | 0.787 / 0.796 [6/8] | 0.698 / 0.729 [6/8] |
| opacity only (no depth statistics) | 0.917 / 0.927 [7/8] | 0.787 / 0.808 [7/8] | 0.698 / 0.792 [8/8] |
| objects: global 32-depth grid | 0.821 / 0.920 [4/8] | 0.740 / 0.782 [4/8] | 0.660 / 0.714 [6/8] |
| objects: 4 slices per object | 0.881 / 0.926 [6/8] | 0.768 / 0.792 [4/8] | 0.682 / 0.730 [5/8] |
| objects: 8 slices per object | 0.907 / 0.932 [8/8] | 0.783 / 0.786 [4/8] | 0.694 / 0.746 [7/8] |
| planes: 4-depth global grid | 0.917 / 0.933 [7/8] | 0.787 / 0.798 [6/8] | 0.698 / 0.726 [6/8] |
| planes: 8-depth global grid | 0.917 / 0.939 [8/8] | 0.787 / 0.788 [3/8] | 0.698 / 0.746 [7/8] |
| planes: 16-depth global grid | 0.917 / 0.933 [8/8] | 0.787 / 0.803 [5/8] | 0.698 / 0.749 [6/8] |
