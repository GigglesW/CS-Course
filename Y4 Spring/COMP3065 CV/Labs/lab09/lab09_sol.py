import cv2
import numpy as np
import os
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import webbrowser
import tempfile

def load_images(image_folder):
    images = []
    for filename in os.listdir(image_folder):
        path = os.path.join(image_folder, filename)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
    return images

def extract_features(images):
    sift = cv2.SIFT_create()
    descriptors_list = []
    keypoints_list = []
    for img in images:
        keypoints, descriptors = sift.detectAndCompute(img, None)
        if descriptors is not None:
            descriptors_list.append(descriptors)
            keypoints_list.append(keypoints)
    return keypoints_list, descriptors_list

def build_codebook(descriptors_list, codebook_size=1000):
    all_descriptors = np.vstack(descriptors_list)
    kmeans = KMeans(n_clusters=codebook_size, random_state=0).fit(all_descriptors)
    return kmeans

def encode_features(descriptors_list, kmeans):
    histograms = []
    for descriptors in descriptors_list:
        histogram = np.zeros(kmeans.n_clusters)
        if descriptors is not None:
            clusters = kmeans.predict(descriptors)
            histogram[clusters] += 1
        histogram /= descriptors.shape[0]  # Normalization
        histograms.append(histogram)
    return histograms

def find_similar_images(query_histogram, histograms):
    nn = NearestNeighbors(n_neighbors=10, metric='euclidean').fit(histograms)
    distances, indices = nn.kneighbors([query_histogram])
    return indices[0]

def error_visualize_results(image_paths, indices):
    plt.figure(figsize=(15, 10))
    for i, index in enumerate(indices, start=1):
        img = cv2.imread(image_paths[index], 0)
        plt.subplot(2, 5, i)
        plt.imshow(img, cmap='gray')
        plt.title(f"Image {index}")
        plt.axis('off')
    plt.show()

def visualize_results(image_paths, indices):
    plt.figure(figsize=(15, 10))
    for i, index in enumerate(indices, start=1):
        img = cv2.imread(image_paths[index], cv2.IMREAD_GRAYSCALE)
        if img is not None and img.dtype == np.uint8:  # Ensure img is loaded and correct dtype
            plt.subplot(2, 5, i)
            plt.imshow(img, cmap='gray')
            plt.title(f"Image {index}")
            plt.axis('off')
        else:
            print(f"Error loading or incorrect dtype for image at {image_paths[index]}")
    plt.show()


def main():
    image_folder = './images/data1/'
    images = load_images(image_folder)
    _, descriptors_list = extract_features(images)
    kmeans = build_codebook(descriptors_list)
    histograms = encode_features(descriptors_list, kmeans)
    query_histogram = histograms[0]  # Assuming first image is the query
    indices = find_similar_images(query_histogram, histograms)
    image_paths = [os.path.join(image_folder, f) for f in os.listdir(image_folder)]
    visualize_results(image_paths, indices)

if __name__ == '__main__':
    main()