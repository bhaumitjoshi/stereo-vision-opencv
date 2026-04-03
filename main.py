import cv2
import numpy as np


def main():
    # Example corresponding points in left and right images
    pts_left = np.array([
        [320.0, 240.0],
        [350.0, 260.0],
        [400.0, 300.0]
    ], dtype=np.float64)

    pts_right = np.array([
        [300.0, 240.0],
        [330.0, 260.0],
        [380.0, 300.0]
    ], dtype=np.float64)

    # Example camera intrinsics
    fx = 800.0
    fy = 800.0
    cx = 320.0
    cy = 240.0

    K = np.array([
        [fx, 0, cx],
        [0, fy, cy],
        [0, 0, 1]
    ], dtype=np.float64)

    # Example stereo extrinsics
    R_left = np.eye(3, dtype=np.float64)
    t_left = np.zeros((3, 1), dtype=np.float64)

    R_right = np.eye(3, dtype=np.float64)
    t_right = np.array([[-100.0], [0.0], [0.0]], dtype=np.float64)  # baseline = 100 mm

    # Projection matrices: P = K [R | t]
    P_left = K @ np.hstack((R_left, t_left))
    P_right = K @ np.hstack((R_right, t_right))

    # Triangulate points
    pts_4d_h = cv2.triangulatePoints(
        P_left,
        P_right,
        pts_left.T,
        pts_right.T
    )

    pts_3d = (pts_4d_h[:3] / pts_4d_h[3]).T

    print("Reconstructed 3D Points (in camera/world units):")
    for i, pt in enumerate(pts_3d):
        print(f"Point {i+1}: X={pt[0]:.3f}, Y={pt[1]:.3f}, Z={pt[2]:.3f}")


if __name__ == "__main__":
    main()
