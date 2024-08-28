import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_skeleton_data(filepath):
    """Read skeleton data from a given file."""
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            print(f"Read {len(lines)} lines from file.")
            return lines
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def parse_skeleton_data(lines):
    """Parse skeleton data from a list of lines."""
    parsed_frames = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) < 4:  # Ensure each line has at least frame number and one joint data
            print(f"Skipping malformed line: {line.strip()}")
            continue
        frame_number = int(parts[0])
        joints = []
        for i in range(1, len(parts), 3):
            if i + 2 < len(parts):
                x = float(parts[i])
                y = float(parts[i+1])
                z = float(parts[i+2])
                joints.append((x, y, z))
        if joints:
            parsed_frames.append((frame_number, joints))
    print(f"Parsed {len(parsed_frames)} frames.")
    return parsed_frames

def visualize_skeleton(frame_number, joints, save_path=None):
    """Visualize skeleton data for a given frame."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xs, ys, zs = zip(*joints)
    ax.scatter(xs, ys, zs)
    
    # Plot lines connecting the joints
    ax.plot(xs, ys, zs, color='blue', marker='o')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Frame {frame_number}')
    
    if save_path:
        plt.savefig(save_path)
    
    plt.show()

# Main function
def main(skeleton_file_path, save_path=None):
    frames = read_skeleton_data(skeleton_file_path)
    if not frames:
        print("No data was read from the file. Please check the file content and format.")
        return
    
    parsed_frames = parse_skeleton_data(frames)
    
    if not parsed_frames:
        print("No frames were parsed. Please check the data format.")
        return
    
    # Visualize the first frame's data
    frame_number, joints = parsed_frames[0]
    visualize_skeleton(frame_number, joints, save_path)

if __name__ == '__main__':
    skeleton_file_path = r'/usr/local/inter-rel-net-hockey/data02/sbu/s01s02/01/001/skeleton_pos.txt' # Skeleton data file path
    save_path = r'/demo/ARN-LSTM/visualize/results/sbu/001.png'  # Path to save the visualization
    main(skeleton_file_path, save_path)
