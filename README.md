
This project demonstrates 3D point reconstruction from stereo image correspondences using triangulation and camera projection matrices in OpenCV.

Two camera views observe the same point, and its 3D position is computed by intersecting the corresponding rays from each camera.

## Concepts Used

- Stereo geometry
- Projection matrices
- Triangulation
- 3D reconstruction from two views

## Output

Reconstructed 3D Points (in camera/world units):
Point 1: X=0.000, Y=-0.000, Z=4000.000
Point 2: X=150.000, Y=100.000, Z=4000.000
Point 3: X=400.000, Y=300.000, Z=4000.000

## How to Run

pip install -r requirements.txt  
python main.py
