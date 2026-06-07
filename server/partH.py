import geopandas as gpd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score 

parcels = gpd.read_file("data/parcel.geojson")
roads = gpd.read_file("data/roads.geojson") 
water = gpd.read_file("data/water_network.geojson") 
landuse = gpd.read_file("data/landuse.geojson") 
schools = gpd.read_file("data/schools.geojson") 
tourism = gpd.read_file("data/tourism.geojson") 

# Align Coordinate Reference Systems (CRS)
roads = roads.to_crs(parcels.crs) 
water = water.to_crs(parcels.crs) 
landuse = landuse.to_crs(parcels.crs)
schools = schools.to_crs(parcels.crs) 
tourism = tourism.to_crs(parcels.crs) 

# Geometric Feature Engineering
parcels["area"] = parcels.geometry.area 
parcels["perimeter"] = parcels.geometry.length 
parcels["compactness"] = ( 
    parcels["area"] / 
    (parcels["perimeter"] ** 2) 
) 

parcels["centroid"] = parcels.geometry.centroid 

# Distance to infrastructure / features
parcels["dist_to_road"] = parcels["centroid"].apply( 
    lambda p: roads.distance(p).min() 
) 

parcels["dist_to_water"] = parcels["centroid"].apply( 
    lambda p: water.distance(p).min() 
) 

parcels["dist_to_school"] = parcels["centroid"].apply( 
    lambda p: schools.distance(p).min() 
) 

parcels["dist_to_tourism"] = parcels["centroid"].apply( 
    lambda p: tourism.distance(p).min() 
) 

# --- NEW FEATURES: Tourism Density & Land Use Diversity ---

# 1. Tourism Density: Number of tourism attractions within a 1km neighborhood buffer
parcels["tourism_density"] = parcels["centroid"].apply( 
    lambda p: tourism.intersects(p.buffer(1000)).sum() 
) 

# 2. Land Use Diversity: Shannon Entropy of land use classes within a 1km neighborhood buffer
def calculate_landuse_diversity(centroid, landuse_df, radius=1000):
    buffer = centroid.buffer(radius)
    intersecting_lu = landuse_df[landuse_df.intersects(buffer)]
    if intersecting_lu.empty:
        return 0
    
    # Calculate proportions based on the counts of intersecting landuse categories
    counts = intersecting_lu["Name"].value_counts()
    proportions = counts / counts.sum()
    
    # Shannon Entropy formula: -sum(p * log(p))
    entropy = -sum(proportions * np.log(proportions))
    return entropy

parcels["landuse_diversity"] = parcels["centroid"].apply( 
    lambda c: calculate_landuse_diversity(c, landuse, 1000) 
) 

# --- Data Preparation & Encoding ---

# Spatial join with land use zone
parcels_landuse = gpd.sjoin( 
    parcels, 
    landuse[["Name", "geometry"]], 
    how="left", 
    predicate="intersects" 
)

# Encode land use categories 
parcels_landuse["landuse_code"] = ( 
    parcels_landuse["Name"] 
    .astype("category") 
    .cat.codes 
) 

# Print unique land use categories and their codes 
print( 
    parcels_landuse[ 
        ["Name", "landuse_code"] 
    ] 
    .drop_duplicates() 
    .sort_values("landuse_code") 
)

# Encode target variable (land use class) 
parcels_landuse["target_code"] = ( 
    parcels_landuse["ASS_CLASSI"] 
    .astype("category") 
    .cat.codes 
) 

# Included new spatial features into the training feature list
features = [ 
    "area", 
    "perimeter", 
    "compactness", 
    "dist_to_road", 
    "dist_to_water", 
    "dist_to_school", 
    "dist_to_tourism", 
    "landuse_code",
    "tourism_density",
    "landuse_diversity"
] 

data = parcels_landuse.dropna( 
    subset=features + ["target_code"] 
) 

X = data[features] 
y = data["target_code"] 

X_train, X_test, y_train, y_test = train_test_split( 
    X, 
    y, 
    test_size=0.30, 
    random_state=42 
) 

# --- Model Modification: SVM Classifier Pipeline ---
# Using make_pipeline ensures that feature scaling happens seamlessly 
# and prevents data leakage between train/test splits.
model = make_pipeline(
    StandardScaler(),
    SVC(kernel="rbf", random_state=42)
) 

model.fit(X_train, y_train) 

# Generate predictions 
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred) 

print("Accuracy:", accuracy) 

data["predicted_class"] = model.predict(X) 

categories = ( 
    data["ASS_CLASSI"] 
    .astype("category") 
    .cat.categories 
) 

data["predicted_label"] = data["predicted_class"].apply( 
    lambda code: categories[code] 
)

data["correct_prediction"] = ( 
    data["ASS_CLASSI"] == 
    data["predicted_label"] 
) 
print( 
    data[ 
        [ 
            "ASS_CLASSI",
            "predicted_label", 
            "correct_prediction" 
        ] 
    ].head() 
)

data = data.drop( 
    columns=["centroid"], 
    errors="ignore" 
)

# Export to GeoJSON 
data.to_file( 
    "output/parcel_tourismDensity_landuseDiversity_geoai_prediction.geojson", 
    driver="GeoJSON" 
) 
print("GeoAI output exported.")